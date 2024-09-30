from bs4 import BeautifulSoup as bs
import bs4  # BeautifulSoup 내부의 모듈인 SoupStrainer 사용을 위해 추가
import requests
import sys
import io
import os
from langchain_community.document_loaders import WebBaseLoader

# os.environ['USER_AGENT'] = 'myagent'

# 한글 출력 인코딩 설정 (환경에 따라 필요할 수 있음)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 요청 헤더에 User-Agent 설정 (여기서는 Chrome을 사용하는 것처럼 설정)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

response = requests.get('https://search.naver.com/search.naver?query=%EB%82%A0%EC%94%A8', headers=headers)

print(response.content)
