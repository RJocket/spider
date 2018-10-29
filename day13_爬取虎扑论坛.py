from selenium  import webdriver
import re
# driver = webdriver.Firefox()
# link ="https://bbs.hupu.com/bxj"
# driver.get(link)
# html_source = driver.page_source
# # print(html_source)

# with open("hupu.txt","w+",encoding="utf-8") as f:
# 	f.write(html_source)
# 	f.close()
with open("hupu.txt","r+",encoding="utf-8") as f:
	text=f.read()
	# print(text)
	# r = re.findall("<html",text)
	r=re.findall("<div"+"\\s"+"class="+"\"titlelink"+"(.+)</div>",text)
	print(r)


