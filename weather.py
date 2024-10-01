from bs4 import BeautifulSoup as bs
import bs4  # BeautifulSoup 내부의 모듈인 SoupStrainer 사용을 위해 추가
import requests
import sys
import io
import os
from langchain_community.document_loaders import WebBaseLoader

# os.environ['USER_AGENT'] = 'myagent

# 한글 출력 인코딩 설정 (환경에 따라 필요할 수 있음)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 뉴스기사 내용을 로드합니다.
loader = WebBaseLoader(
    web_paths=("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            "div",
            attrs={"class": ["current-temp"]},
        )
    ),
    header_template={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    },
)

docs = loader.load()
# print(f"문서의 수: {len(docs)}")
print(docs)
