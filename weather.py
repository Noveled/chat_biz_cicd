from bs4 import BeautifulSoup as bs
import requests
import sys # 한글 출력 인코딩에 사용
import io # 한글 출력 인코딩에 사용 
from langchain_community.document_loaders import WebBaseLoader

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


# 여러 개의 url 지정 가능
url1 = "https://blog.langchain.dev/customers-podium/"
url2 = "https://blog.langchain.dev/langgraph-v0-2/"

loader = WebBaseLoader(
    web_paths=(url1, url2),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("article-header", "article-content")
        )
    ),
)
docs = loader.load()

print(docs[0], docs[1])

