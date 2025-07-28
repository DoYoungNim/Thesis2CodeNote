import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.load_dummy_data import load_dummy_data


def webRAG_result(keywords, max_results=5):
    """
    웹 검색 결과를 가져오는 함수 (WebRAG 사용)

    Args:
        query (str): 검색 쿼리
        max_results (int): 가져올 최대 결과 수

    Returns:
        dict: 웹 검색 결과
    """
    try:
        # WebRAG를 사용한 검색 수행
        results = webRAG.search(keywords, num_results=max_results)
        return results
    except Exception as e:
        print(f"WebRAG 검색 중 오류 발생: {str(e)}")
        return {"results": [], "error": str(e)}


def test():
    """
    webRAG_result 함수의 테스트용 함수
    """
    testdata = None # 기본값 설정

    try:
        # 더미 데이터를 로드
        dummy_data = load_dummy_data()
        testdata = dummy_data.get("webRAG_results", [])
    except Exception as e:  
        print(f"테스트 중 오류 발생: {str(e)}")
        testdata = {"error": str(e), "results": []}

    return testdata



if __name__ == "__main__":
    testdata = test()
    print(testdata[0]['query'])
    print(testdata[0]['results'][0]['title'])
    print(testdata[0]['results'][0]['url'])
    print(testdata[0]['results'][0]['snippet'])