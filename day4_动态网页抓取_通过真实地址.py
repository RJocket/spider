# 和静态网页不同的是，动态网页使用JavaScript，很多内容不会显示在源Html中
# 动态网页数据获取的两种方式：1.通过浏览器审查元素解析真实网页地址（网络->所有）；2.使用selenium模拟浏览器
# 
# Ajax，异步JavaScript和XML ,异步更新技术。使得后台与服务器通过少量的数据交换就能使网页实现异步更新。
# 使得网页不需要重新加载整个网页，只需要加载部分数据即可；

# 方式一：找到真实地址
import requests
headers ={
	'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

link = 'https://api-zero.livere.com/v1/comments/list?callback=jQuery112403473268296510956_1531502963311&limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1531502963313'
r = requests.get(link,headers =headers,timeout=10)
# print (r.text)#这里取出来是json 格式

# 解析JSON数据
import json
# 获取JSON的String
json_string = r.text
json_string =json_string[json_string.find('{'):-2]#提取字符串中符合json格式的部分
# print(json_string)

# 使用 json.loads 可以把字符串格式的响应体数据转化为 json 数据
json_data = json.loads(json_string)
# print(json_data)

# 利用json结构体数据，提取需要的数据 
comment_list = json_data['results']['parents']#得到一个字典

for each in comment_list:
	message = each['content']
	print(message)#打印出所有评论

# 如果需要打印多页评论，则需要for循环更新URL

