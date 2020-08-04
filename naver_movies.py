import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn#")

html = BeautifulSoup(raw.text, 'html.parser')

# f = open("movie.csv", 'w')
# f.write('제목', '코드\n')

movie_list = {}

movies = html.select('ul.lst_detail_t1 dl.lst_dsc')

for movie in movies:
    title = movie.select_one('dt.tit a').text
    code = movie.select_one('dt.tit a')['href'].split("code=="[-1])
    print(title)
    print(code[-1])
    movie_list['title'] = title
    movie_list['code'] = code
print(movie_list)