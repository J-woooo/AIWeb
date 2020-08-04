import requests
import json
from collections import OrderedDict
from bs4 import BeautifulSoup
file_data = OrderedDict()
raw = requests.get("https://movie.naver.com/movie/running/current.nhn#")

html = BeautifulSoup(raw.text, 'html.parser')

movie_list = []

movies = html.select('ul.lst_detail_t1 dl.lst_dsc')

for movie in movies:
    title = movie.select_one('dt.tit a').text
    code = movie.select_one('dt.tit a')['href'].split("code=="[-1])
    # print(title)
    # print(code[-1])
    movie_dic = {}
    movie_dic['title'] = title
    movie_dic['code'] = code[-1]
    movie_list.append(movie_dic)
# print(movie_list)

with open('movie.json', 'w', encoding='utf-8') as f:
    json.dump(movie_list, f, ensure_ascii=False, indent=4)
