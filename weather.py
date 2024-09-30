from bs4 import BeautifulSoup as bs
import bs4  # BeautifulSoup 내부의 모듈인 SoupStrainer 사용을 위해 추가
import requests
import sys
import io
import os
from langchain_community.document_loaders import WebBaseLoader

os.environ['USER_AGENT'] = 'myagent'

# 한글 출력 인코딩 설정 (환경에 따라 필요할 수 있음)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 환경 변수에서 User-Agent 가져오기
# user_agent = os.getenv('USER_AGENT', 'Mozilla/5.0')

# # 요청 헤더에 User-Agent 설정 (여기서는 Chrome을 사용하는 것처럼 설정)
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
# }
# 여러 개의 URL 지정 (리스트로 설정)
urls = ["https://blog.langchain.dev/customers-podium/", "https://blog.langchain.dev/langgraph-v0-2/"]

# WebBaseLoader로 HTML 문서를 로드하면서 특정 부분만 파싱
# header_template=headers,
loader = WebBaseLoader(
    web_paths=urls,
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("article-header", "article-content")  # 가져오려는 특정 클래스 선택
        )
    ),
)

# 문서 로드
docs = loader.load()

# 문서 내용을 출력
for idx, doc in enumerate(docs):
    print(f"Document {idx+1}:\n", doc.page_content[:500])  # 각 문서에서 첫 500자만 출력
