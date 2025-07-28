from notion_client import Client
from fastmcp import FastMCP


notion = Client(auth="")
db_id = ""

mcp = FastMCP(
    name="notion-mcp-server",
    instructions="Notion page 생성 도구"
)


@mcp.tool()
def make_page(query: dict) -> str:
    """
    특정 json 포멧형태를 가진 Args가 입력되면 Notion에 페이지를 생성 합니다.

    Args:
        query(dict): 전체 json 입력. 'lecture_info', 'transcript_summary', 'keywords' 등을 포함 합니다.

    Returns:
        str: 생성된 노션 페이지의 링크

    """

    # 쿼리 데이터 추출
    info = query.get('lecture_info',{})
    summary = query.get('transcript_summary',{})
    timeline = query.get('timeline',[])
    keywords = query.get('keywords', {})
    search_results = query.get('web_search_results', [])
    arxiv_results = query.get('arxiv_search_results', [])
    additional_resuorces = query.get('additional_resuorces', {})
    metadata = query.get('metadata', {})

    page_title = info['title', ""]

    # 페이지 생성
    response = notion.pages.create(
        parent={"database_id": db_id},
        icon={"emoji": "🤖"},
        properties={
            "title": {
                "title": [{"text": {"content": page_title}}]
            },
            "instructor": {
                "rich_text": [{"text": {"content": info["speaker"]}}]
            },
            "channel": {
                "rich_text": [{"text": {"content": info["channel"]}}]
            },
            "duration" : {
                "rich_text": [{ "text": { "content": info["duration"]}}]
            },
            "upload": {
                "date": { "start": info["upload_date"] }
            },
            "views": {
                "number": int(info["views"].replace(",", ""))
            }
        }

    )

    return response["url"]


if __name__ == '__main__':
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000,
        path="/mcp"
    )