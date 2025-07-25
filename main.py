# 단계 0 : User Interface 가능한 gradio 채팅과 간단한 버튼이 뜨는 프론트 구현
# 단계 1 : 링크를 통해 스크립트를 받아와 json으로 키워드와 요약문을 넘겨주기
# 단계 2 : 키워드를 입력값으로 (1)webRAG.py , (2)arxiv.py 를 병렬로 실행시킵니다. (3) websearch.py 에서 실행하고, 결과값으로 json 객체를 반환합니다.
# 단계 3 : llm으로 문서 요약과 웹서치 결과물을 통합한 json 객체를 만듭니다.
# 단계 4 : mcp를 기반으로 사용자의 참고자료에 맞도록 자동으로 판단하여 노션 정리 문서를 만드는 Agent를 제작합니다.
# 단계 0 : Agent 와 UI 동기화를 구현합니다.


# src : 모델 정의, 모델 서비스 모듈 등 핵심 소스 코드 (추후 넣어도 됨..)
# util : 잡다한 로그, 문자 처리 모듈 등 편하게 만들어서 사용하십시오.


def main():
    """메인 함수"""
    print("main is running...")
    
    # 의존성 및 데이터 파일 확인
    #if not check_dependencies():
    #    return
    
    #if not check_data_files():
    #    return
    
    #print("✅ 모든 의존성과 데이터 파일이 확인되었습니다.")
    



if __name__ == "__main__":
    main() 