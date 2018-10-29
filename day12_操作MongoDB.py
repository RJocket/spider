from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import datetime


# 创建MongoClient对象
client =MongoClient('localhost',27017)
# 创建数据库（连接,没有则创建）
db = client.blog_database
# 创建集合collection（连接,没有则创建）
collection = db.blog

link ="http://www.santostang.com"
headers ={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
	'Host':'www.santostang.com'
}

r = requests.get(link,headers =headers)
soup =BeautifulSoup(r.text,"lxml")
soup.prettify()
title_list=soup.find_all('h1',class_='post-title')
for  each  in title_list:
	title = each.a.text.strip()
	url = each.a['href'] #获取a中 'href'属性
	# 组织一个document
	post ={
		'url':url,
		'title':title,
		'date': datetime.datetime.utcnow()
	}
	collection.insert_one(post)#往集合中插入一个document