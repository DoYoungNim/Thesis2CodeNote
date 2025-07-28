import requests, uuid, json
from openai import OpenAI

client = OpenAI(
    api_key=''
)

MCP_URL = "http://localhost:8000/mcp"

session_id = None


def init_session():
    """
    MCP 세션 획득
    :return: session_id
    """
    global session_id

    # MCP 서버 연결요청 및 세션 획득
    payload = {
        "jsonrpc": "2.0",
        "id": str(uuid.uuid4()),
        "method": "initialize",
        "params": {
            "protocolVersion": 1,
            "capabilities": {"tools": True},
            "clientInfo": {"name": "gpt-mcp-client", "version": "0.1"}
        }
    }
    headers = {"Content-Type": "application/json", "Accept": "text/event-stream"}
    r = requests.post(MCP_URL, json=payload, headers=headers)
    session_id = r.headers.get("Mcp-Session-Id")
    if not session_id:
        raise RuntimeError("Can not get Session ID from MCP-server")
    print(f"MCP Session aquired!! :: {session_id}")

    return session_id


def chat_loop():
    global session_id
    if not session_id:
        init_session()

    messages = [
        {
            "role": "system",
            "content": "너는 MCP 툴을 호출해 노션 데이터를 처리하는 도우미야. 사용자의 일반 대화에 답변하다가, 상황에 따라 노션 페이지를 생성해줘"
        }
    ]

    while True:
        user_input = input("\n🧑 User: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("👋 종료합니다.")
            break

        messages.append({"role": "user", "content": user_input})

        chat_kwargs = {
            "model": 'gpt-4',
            "messages": messages,
            "tool_choice": "auto",
            "tools": [
                {
                    "type": "function",
                    "function": {
                        "name": "make_page",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "query": {
                                    "type": "string",
                                    "description": "강의 정보, 요약, 키워드, 추천 자료 등을 포함하는 JSON 문자열"
                                }
                            },
                            "returns": {
                                "type": "object",
                                "properties": {
                                    "analysis": {"type": "string"}
                                }
                            }
                        }
                    }
                }
            ]
        }

        # GPT 응답
        response = client.chat.completions.create(**chat_kwargs)
        ai_msg = response.choices[0].message

        # 툴 호출 없으면 출력 후 대화 계속
        if not ai_msg.tool_calls:
            print(f"\n🤖 GPT: {ai_msg.content}")
            messages.append({"role": "assistant", "content": ai_msg.content})
            continue

        # 툴 호출 처리
        for call in ai_msg.tool_calls:
            fn_name = call.function.name
            fn_args = json.loads(call.function.arguments or "{}")

            payload = {
                "jsonrpc": "2.0",
                "id": str(uuid.uuid4()),
                "method": "tools/call",
                "params": {"name": fn_name, "arguments": fn_args}
            }

            headers = {
                "Accept": "application/json, text/event-stream",
                "Content-Type": "application/json; charset=utf-8",
                "Mcp-Session-Id": session_id
            }

            print(f"\n[📡 MCP 호출] {fn_name} {fn_args}")
            resp = requests.post(MCP_URL, json=payload, headers=headers, timeout=30)
            print(f"[✅ status] {resp.status_code}")
            print(f"[📦 body ] {resp.text}")
            resp.raise_for_status()

            tool_output = parse_mcp_response(resp)

            # 툴 결과를 GPT에 전달
            messages += [
                {"role": "assistant", "content": None, "tool_calls": [call.model_dump()]},
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "name": fn_name,
                    "content": json.dumps(tool_output, ensure_ascii=False, separators=(",", ":"))
                }
            ]


def parse_mcp_response(resp):
    if resp.headers.get("Content-Type", "").startswith("text/event-stream"):
        # 스트림 응답 처리
        lines = [line[5:].lstrip() for line in resp.text.splitlines() if line.startswith("data:")]
        raw = "\n".join(lines)
        data = json.loads(raw)
    else:
        data = resp.json()
    return data.get("result", data)


if __name__ == '__main__':
    chat_loop()
