import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.load_dummy_data import load_dummy_data


def test():
    """
    webRAG_result 함수의 테스트용 함수
    """
    testdata = None # 기본값 설정

    try:
        # 더미 데이터를 로드
        dummy_data = load_dummy_data()
        testdata = dummy_data.get("arxiv_results", [])
    except Exception as e:  
        print(f"테스트 중 오류 발생: {str(e)}")
        testdata = {"error": str(e), "results": []}

    return testdata



if __name__ == "__main__":
    testdata = test()

    print(testdata[0]['query'])
    print(testdata[0]['papers'][0]['title'])
    print(testdata[0]['papers'][0]['url'])
    print(testdata[0]['papers'][0]['abstract'])