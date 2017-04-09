# -*- encoding:utf8 -*-
# BeatutifulSoap 사용 예제
import os,sys,time
os.chdir(os.path.dirname(__file__))
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://newstapa.org/category/every_news/news/page/1'
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

'<div id="content" class="col-md-8 mgto0" role="main">'
soup2 = soup.find('div',attrs={'id':'content','class':'col-md-8 mgto0','role':'main'})
for article in soup2.findAll('div',attrs={'class':'col-md-12 col-sm-4 gettouch'}):
    print(article.find('small',attrs={'class':'panel_small_inf'}).text) #기사 날짜
    print(article.find('h2', attrs={'class': 'rt-article-title'}).a['href']) #기사 url
    print(article.find('h2', attrs={'class': 'rt-article-title'}).a['title']) #기사 제목
    print(article.find('div',attrs={'class':'item-thumbnail'}).a.img['src']) #섬네일 url
