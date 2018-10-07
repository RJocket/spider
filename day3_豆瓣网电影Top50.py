import requests
from bs4 import BeautifulSoup

def getMovies():
	link ="Https://movie.douban.com/top250"
	# 模拟浏览器
	headers ={
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Fixfox/62.0',
		'Host':'movie.douban.com'
	}
	movies =[]
	# 使用 for 循环翻页
	for i in range(0,10):
		link = "Https://movie.douban.com/top250"+"?start={}&filter=".format(25*i)

		r = requests.get(link,headers =headers,timeout =10)
		# print (str(i+1))
		# print(r.text)
		# print(link)
		# print(r.status_code)
		soup = BeautifulSoup(r.text,'lxml')
		div_list = soup.find_all("div",class_ ="hd")
		for each in div_list:
			movie =each.a.span.text.strip()
			movies.append(movie)
	return movies

movies =getMovies()
print(movies)