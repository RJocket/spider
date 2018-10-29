#推荐使用BeautifulSoup "lxml"
import requests
from bs4 import BeautifulSoup

link = "http://www.santostang.com"
headers = {
	'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
r = requests.get(link,headers =headers)
soup= BeautifulSoup(r.text,"lxml")#使用“lxml”速度较快 makeup=r.text

print(soup.prettify())#美化soup
#通过find查找第一个数据
fisrt_title =soup.find("h1",class_="post-title").a.text.strip()
print("第一个标题是",fisrt_title)

# 通过find_all查找所有数据
title_list = soup.find_all("h1",class_="post-title")
for each in title_list:
	print(each.a.text.strip())

'''
BeautifulSoup提取对象的方法：1.遍历文档树；2.搜索文档树；3.CSS选择器
1.遍历文档树 慢
 eg:	soup.header.h3
 		soup.header.div.contents
 		for child in soup.header.div.contents:
 			print(child)
 		也可以获取父节点 soup.parent	
2. 搜索文档树
	soup.find ()
	soup.find_all()
	这里也能和正则表达式一起使用，eg： for tag in soup.find(re.compile("^h"))：
3.CSS选择器
	soup.select("header> h3")
	soup.select("div>a")

'''