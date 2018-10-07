# -*- coding:utf-8 -*-
'''
<Python 爬虫从入门到实践>——唐松
获取页面数据->解析数据->存储数据
'''
import requests
from bs4 import BeautifulSoup

# 1.获取页面
link ="http://www.santostang.com/"
# 指定headers 请求，伪装成模拟器
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Fixfox/62.0'}
r= requests.get(link,headers=headers).text

# print(r.text,r.staus_code)

# 2.提取需要的数据
soup = BeautifulSoup(r,'lxml')
# #<h1 class="post-title"><a href="http://www.santostang.com/2018/07/15/4-3-%e9%80%9a%e8%bf%87selenium-%e6%a8%a1%e6%8b%9f%e6%b5%8f%e8%a7%88%e5%99%a8%e6%8a%93%e5%8f%96/">4.3 通过selenium 模拟浏览器抓取</a></h1>
title= soup.find('h1',class_="post-title").a.text.strip() # 4.3 通过selenium 模拟浏览器抓取
print(title)

# 3.存储数据
with open("title.text","a+") as f:
	f.write(title)
	f.close()

