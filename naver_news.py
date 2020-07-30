import requests
from bs4 import BeautifulSoup

base_url = "https://search.naver.com/search.naver?&where=news&query=%EA%B4%91%EC%A3%BC%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=60&start="
start_num = 11
end_url = "&refresh_start=0"

URL = base_url + str(start_num) + end_url

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup)

container = soup.select("a._sp_each_title")

for con in container:
    print("제목: ", con.text.strip(), "\t링크: ", con["href"])
# a._sp_each_title

# a 태그의 href와 값 꺼내오기