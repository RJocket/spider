
import requests
import re


# re.match() 从字符串起始位置匹配一个模式 re.match(pattern,string,flags =0)
m =re.match("www","www.baidu.com")
print("匹配的结果",m)
print("匹配的起点和终点",m.span()) 
print("起点",m.start())
print("终点",m.end())

line ="Fat cats are smarter than dogs, is it right?"
m =re.match("(.*) are (.*?) dogs",line)
print("返回匹配结果的整句话",m.group(0))
print("返回匹配结果的第一个",m.group(1)) 
print("返回匹配结果的第二个",m.group(2)) 
print("返回匹配结果列表",m.groups())


# re.search()扫描整个字符串并返回第一个成功的匹配    re.search(pattern,string,flags =0)
m_match = re.match("com","www.baidu.com") #None
m_search =re.search("com","www.baidu.com")#<re.Match object; span=(10, 13), match='com'>
print(m_match)
print(m_search)

patten =re.compile("[a-zA-Z]*")
n =re.match(patten,"qweASD123456")
print(n)#<re.Match object; span=(0, 6), match='qweASD'>

# re.findall() 找到所有匹配
n =re.findall("[0-9]+","123456ABCD654321")
print(n)#['123456', '654321']


r =requests.get("Http://www.baidu.com")
# print (r.text)
n =re.findall("href=http://www.[a-zA-Z]+.com",r.text)
print(n)