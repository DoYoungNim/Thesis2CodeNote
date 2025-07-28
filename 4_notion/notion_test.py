from notion_client import Client

notion = Client(auth="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")
db_id = "23ebd53bd26080a3a6b4c676ada6842c"


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

    page_title = info.get('title', '')

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
    query = {
        "lecture_info": {
            "title": "AI란 무엇인가? - 인공지능의 기초부터 응용까지",
            "url": "https://youtube.com/watch?v=dummy_ai_lecture",
            "duration": "45:32",
            "speaker": "김인공 교수",
            "channel": "AI 아카데미",
            "upload_date": "2024-12-15",
            "views": "125,847",
            "description": "인공지능의 기본 개념부터 최신 딥러닝 기술까지 포괄적으로 다루는 강의"
        },
        "transcript_summary": {
            "full_summary": "이 강의는 인공지능의 정의와 역사부터 시작하여 현재까지의 발전 과정을 설명합니다. 1950년대 앨런 튜링의 튜링 테스트부터 현재의 ChatGPT까지, AI의 진화 과정을 체계적으로 다룹니다. 머신러닝과 딥러닝의 차이점을 명확히 하고, 지도학습, 비지도학습, 강화학습의 세 가지 주요 학습 방법을 실제 사례와 함께 설명합니다. 특히 신경망의 구조와 작동 원리를 시각적으로 설명하며, CNN, RNN, Transformer 등 주요 아키텍처의 특징과 응용 분야를 소개합니다. 마지막으로 AI의 윤리적 문제와 미래 전망에 대해 논의합니다.",
            "key_points": [
                "인공지능은 인간의 학습능력과 추론능력, 지각능력, 언어이해능력 등을 컴퓨터 프로그램으로 실현한 기술",
                "AI 역사: 1956년 다트머스 회의에서 'Artificial Intelligence' 용어 최초 사용",
                "머신러닝은 AI의 하위 분야이며, 딥러닝은 머신러닝의 하위 분야",
                "지도학습: 레이블이 있는 데이터로 학습 (분류, 회귀)",
                "비지도학습: 레이블이 없는 데이터에서 패턴 발견 (클러스터링, 차원축소)",
                "강화학습: 환경과의 상호작용을 통한 최적 행동 학습",
                "신경망: 인간 뇌의 뉴런을 모방한 연결 구조",
                "CNN: 이미지 처리에 특화된 합성곱 신경망",
                "RNN: 순차 데이터 처리에 적합한 순환 신경망",
                "Transformer: 자연어 처리 혁신을 이끈 어텐션 메커니즘 기반 모델"
            ],
            "timeline": [
                {"time": "00:00-05:30", "content": "AI 정의와 개념 소개"},
                {"time": "05:30-12:15", "content": "AI 발전사와 주요 이정표"},
                {"time": "12:15-20:45", "content": "머신러닝 vs 딥러닝 차이점"},
                {"time": "20:45-30:20", "content": "학습 방법론 (지도/비지도/강화학습)"},
                {"time": "30:20-38:50", "content": "신경망과 딥러닝 아키텍처"},
                {"time": "38:50-45:32", "content": "AI 윤리와 미래 전망"}
            ]
        },
        "keywords": {
            "primary_keywords": [
                "인공지능",
                "머신러닝",
                "딥러닝",
                "신경망",
                "지도학습",
                "비지도학습",
                "강화학습",
                "CNN",
                "RNN",
                "Transformer"
            ],
            "secondary_keywords": [
                "튜링테스트",
                "다트머스회의",
                "퍼셉트론",
                "역전파",
                "경사하강법",
                "활성화함수",
                "합성곱",
                "어텐션메커니즘",
                "자연어처리",
                "컴퓨터비전"
            ],
            "technical_terms": [
                "Artificial Neural Network",
                "Convolutional Neural Network",
                "Recurrent Neural Network",
                "Long Short-Term Memory",
                "Gradient Descent",
                "Backpropagation",
                "Feature Engineering",
                "Overfitting",
                "Regularization",
                "Cross-validation"
            ]
        },
        "web_search_results": [
            {
                "query": "인공지능 정의 기본 개념",
                "results": [
                    {
                        "title": "인공지능(AI)의 정의와 분류 체계 - 네이버 블로그",
                        "url": "https://blog.naver.com/ai_definition_2024",
                        "snippet": "인공지능은 인간의 인지능력을 컴퓨터로 구현한 기술로, 좁은 AI와 일반 AI로 분류할 수 있습니다. 현재는 특정 작업에 특화된 좁은 AI 단계에 있습니다.",
                        "relevance_score": 0.95,
                        "source_type": "blog"
                    },
                    {
                        "title": "AI 발전사: 1950년대부터 현재까지 - 한국과학기술원",
                        "url": "https://kaist.ac.kr/ai_history_timeline",
                        "snippet": "1956년 다트머스 컨퍼런스에서 시작된 AI 연구는 여러 차례의 겨울을 거쳐 2010년대 딥러닝 혁명으로 새로운 전성기를 맞았습니다.",
                        "relevance_score": 0.92,
                        "source_type": "academic"
                    },
                    {
                        "title": "머신러닝과 딥러닝의 차이점 완벽 정리 - TechCrunch Korea",
                        "url": "https://techcrunch.kr/ml_vs_dl_comparison",
                        "snippet": "머신러닝은 데이터로부터 패턴을 학습하는 방법론이며, 딥러닝은 다층 신경망을 사용하는 머신러닝의 하위 분야입니다.",
                        "relevance_score": 0.88,
                        "source_type": "tech_news"
                    }
                ]
            },
            {
                "query": "딥러닝 CNN RNN Transformer 비교",
                "results": [
                    {
                        "title": "딥러닝 아키텍처 비교: CNN vs RNN vs Transformer - 인공지능신문",
                        "url": "https://ainews.co.kr/architecture_comparison_2024",
                        "snippet": "CNN은 이미지 처리, RNN은 시계열 데이터, Transformer는 자연어 처리에 각각 최적화된 구조를 가지고 있습니다.",
                        "relevance_score": 0.94,
                        "source_type": "tech_news"
                    },
                    {
                        "title": "Transformer 모델이 AI를 바꾼 방법 - MIT Technology Review",
                        "url": "https://mit-tr.com/transformer_revolution",
                        "snippet": "2017년 등장한 Transformer는 어텐션 메커니즘을 통해 자연어 처리 분야에 혁명을 일으켰으며, GPT와 BERT의 기반이 되었습니다.",
                        "relevance_score": 0.91,
                        "source_type": "tech_magazine"
                    }
                ]
            }
        ],
        "arxiv_search_results": [
            {
                "query": "artificial intelligence introduction survey",
                "papers": [
                    {
                        "title": "A Comprehensive Survey of Artificial Intelligence: From Classical to Modern Approaches",
                        "authors": ["Zhang, Wei", "Li, Ming", "Johnson, Robert"],
                        "arxiv_id": "2024.12345",
                        "published": "2024-11-15",
                        "abstract": "This survey provides a comprehensive overview of artificial intelligence from its classical foundations to modern deep learning approaches. We cover the evolution of AI paradigms, key algorithmic contributions, and current challenges in the field.",
                        "url": "https://arxiv.org/abs/2024.12345",
                        "categories": ["cs.AI", "cs.LG"],
                        "relevance_score": 0.96
                    },
                    {
                        "title": "Deep Learning Architectures: A Systematic Review and Future Directions",
                        "authors": ["Park, Sung-Ho", "Chen, Yu", "Schmidt, Michael"],
                        "arxiv_id": "2024.54321",
                        "published": "2024-10-22",
                        "abstract": "We present a systematic review of deep learning architectures including CNNs, RNNs, and Transformers. Our analysis covers architectural innovations, performance comparisons, and emerging trends in neural network design.",
                        "url": "https://arxiv.org/abs/2024.54321",
                        "categories": ["cs.LG", "cs.CV", "cs.CL"],
                        "relevance_score": 0.93
                    },
                    {
                        "title": "Machine Learning Fundamentals: Theory and Practice",
                        "authors": ["Brown, Sarah", "Kim, Jae-Won", "Mueller, Hans"],
                        "arxiv_id": "2024.67890",
                        "published": "2024-09-08",
                        "abstract": "This paper presents fundamental concepts in machine learning including supervised, unsupervised, and reinforcement learning paradigms. We provide theoretical foundations and practical implementation guidelines.",
                        "url": "https://arxiv.org/abs/2024.67890",
                        "categories": ["cs.LG", "stat.ML"],
                        "relevance_score": 0.89
                    }
                ]
            },
            {
                "query": "neural networks CNN RNN transformer",
                "papers": [
                    {
                        "title": "Attention Is All You Need: Revisiting the Transformer Architecture",
                        "authors": ["Vaswani, Ashish", "Shazeer, Noam", "Parmar, Niki"],
                        "arxiv_id": "1706.03762",
                        "published": "2017-06-12",
                        "abstract": "We propose the Transformer, a novel neural network architecture based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.",
                        "url": "https://arxiv.org/abs/1706.03762",
                        "categories": ["cs.CL", "cs.LG"],
                        "relevance_score": 0.98
                    },
                    {
                        "title": "Convolutional Neural Networks for Visual Recognition: A Survey",
                        "authors": ["LeCun, Yann", "Bengio, Yoshua", "Hinton, Geoffrey"],
                        "arxiv_id": "2024.11111",
                        "published": "2024-08-15",
                        "abstract": "This survey reviews the development and applications of convolutional neural networks in computer vision, covering key innovations from LeNet to modern architectures.",
                        "url": "https://arxiv.org/abs/2024.11111",
                        "categories": ["cs.CV", "cs.LG"],
                        "relevance_score": 0.91
                    }
                ]
            }
        ],
        "additional_resources": {
            "recommended_books": [
                {
                    "title": "패턴 인식과 머신 러닝",
                    "author": "Christopher Bishop",
                    "description": "머신러닝의 수학적 기초를 체계적으로 다룬 교과서"
                },
                {
                    "title": "딥러닝",
                    "author": "Ian Goodfellow, Yoshua Bengio, Aaron Courville",
                    "description": "딥러닝의 이론과 실제를 포괄적으로 다룬 바이블"
                }
            ],
            "online_courses": [
                {
                    "title": "CS229: Machine Learning",
                    "provider": "Stanford University",
                    "url": "https://cs229.stanford.edu/",
                    "description": "앤드류 응 교수의 머신러닝 강의"
                },
                {
                    "title": "Deep Learning Specialization",
                    "provider": "Coursera",
                    "url": "https://coursera.org/deeplearning-ai",
                    "description": "딥러닝의 기초부터 응용까지 단계별 학습"
                }
            ],
            "practical_tools": [
                {
                    "name": "TensorFlow",
                    "description": "구글에서 개발한 오픈소스 머신러닝 플랫폼",
                    "url": "https://tensorflow.org"
                },
                {
                    "name": "PyTorch",
                    "description": "페이스북에서 개발한 딥러닝 프레임워크",
                    "url": "https://pytorch.org"
                }
            ]
        },
        "metadata": {
            "processing_date": "2024-12-20",
            "version": "1.0",
            "confidence_score": 0.92,
            "total_processing_time": "3.4 seconds",
            "language": "ko"
        }
    }
    make_page(query)