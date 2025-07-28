import os
import json

def load_dummy_data():
    # 현재 스크립트 파일의 절대 경로를 기준으로 JSON 파일 경로 구성
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, '..', '3_llm_integration', 'ai_lecture_dummy_data.json')
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {json_path}")
        return None
    

if __name__ == "__main__":
    data = load_dummy_data()
    if data:
        print("JSON 데이터 로드 성공")
        print(data)
    else:
        print("JSON 데이터 로드 실패")