'''
爬取安居客上深圳二手房价格 前10页
房屋名，价格，几房几厅，大小，建造年份，联系人，地址，标签
'''
import requests
from bs4 import BeautifulSoup

headers = {
	'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

for i in range(5):
	link = "https://shenzhen.anjuke.com/sale/p{0}}/#filtersort.format(i)"
	r = requests.get(link,headers=headers)
	# print(r.text)
	soup = BeautifulSoup(r.text,"lxml")	
	house_list=soup.find_all('li',class_='list_item')
	for house in house_list:
		name = house.find('div',class_='house-title').a.text.strip()
		price =house.find('span',class_='price-det').text.strip()
		area = house.find('div',class_='details-item').contents[3].text.strip()
		tags_list = house.find_all('span',class_='item-tags')
		tags = [i.text for i in tags_list]
		print(name,price,area,tags)
		time.sleep(5)

