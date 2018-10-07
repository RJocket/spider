import requests

url ="Http://www.santostang.com/"

# r = requests.get(url)
# print("响应体的字符串形式",r.text)
# print("响应状态码",r.status_code)
# print("文本编码",r.encoding)
# print(r.content)
# print(r.json)		

'''
有些网页需要对Reuqests的参数进行设置才能获取网页数据，
包括设置URL参数，定制请求头，发送post请求，	设置超时etc.
'''

#1. 传递URL参数
# 键值对形式，跟在？后面 传递参数params
key_dict={'key1':'value1','key2':'value2'}
r=requests.get("Http://httpbin.org/get",params=key_dict)
print(r.url)#http://httpbin.org/get?key1=value1&key2=value2
# print(r.text)

#2. 定制请求头
# 某些网页需要定制请求头，否则可能无法获取正确的数据

headers ={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Fixfox/62.0',
	'Host':'www.santostang.com'
}
r = requests.get('Http://www.santostang.com/',headers =headers)
print(r.status_code)

# 3.发送Post请求
# 除了get请求，有时需要发送的数据如果为表单格式的数据，就需要使用post请求。
# 因为get请求，会将请求数据显示在URL中，非常不安全。
# 使用post请求，也是用字典方式传递参数data ,自动编写为表单格式
key_dict={'key1':'value1','key2':'value2'}
r = requests.post('Http://httpbin.org/post',data = key_dict)
print(r.text)

# 4.设置超时
# 服务器没响应时，爬虫程序会一直等待。这时候需要设置超时
# 可以在requests的 timeout中设置秒数，时间到则返回异常
link = 'Http://www.santostang.com/'
r = requests.get(link,timeout = 0.01)
