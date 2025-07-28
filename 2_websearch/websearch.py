from arxiv import test
from webRAG import test

def websearch_result(arxiv_results, webRAG_results, max_arxiv_results=5, max_web_results=5):
    """
    arxiv와 web 검색 결과를 통합하여 반환하는 함수
    
    Args:
        arxiv_results (json): arxiv 검색 결과
        webRAG_results (json): webRAG 검색 결과

    Returns:
        dict: arxiv_search_results와 web_search_results를 포함한 딕셔너리
    """
    try:

        # 결과 통합
        combined_results = {
            "webRAG_results": webRAG_results,
            "arxiv_results": arxiv_results,
        }
        
        return combined_results
        
    except Exception as e:
        print(f"검색 중 오류 발생: {str(e)}")
        return {"error": str(e), "results": []}




if __name__ == "__main__":
    # 테스트 실행
    arxiv_results = test()
    webRAG_results = test()
    websearch_results = websearch_result(arxiv_results, webRAG_results, max_arxiv_results=5, max_web_results=5)
    
    print("\n=== 검색 결과 요약 ===")
    print(f"\n RAG 서치의 0번째 쿼리와 결과: {websearch_results['webRAG_results'][0]}")
    print(f"\n ARXIV 서치의 0번째 쿼리와 결과: {websearch_results['arxiv_results'][0]}")


    if websearch_results.get('error'):
        print(f"에러: {websearch_results['error']}")
    else:
        print("\n검색이 성공적으로 완료되었습니다.")