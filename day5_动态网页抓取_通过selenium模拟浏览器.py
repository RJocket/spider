'''
使用Chrome“检查”功能找到源地址还十分容易。但是有一些网站非常复杂，例如前面的天猫产品评论，使用“检查”功能很难找到调用的网页地址。
除此之外，有一些数据真实地址的URL也十分冗长和复杂，有些网站为了规避这些抓取会对地址进行加密，造成其中的一些变量让人摸不着头脑。
'''
'''
动态网页抓取——方法二：使用浏览器渲染引擎。直接用浏览器在显示网页时解析HTML，应用CSS样式并执行JavaScript的语句
'''

from selenium import webdriver

profile_directory =R"C:\Users\R\AppData\Roaming\Mozilla\Firefox\Profiles\yjdic0n5.default"
profile = webdriver.FirefoxProfile(profile_directory)
driver = webdriver.Firefox(profile)

driver.get('http://www.santostang.com/2018/07/04/hello-world/')
# 原来代码中的 JavaScript 解析成了一个 iframe，<iframe title="livere" scrolling="no"…>也就是说，
# 所有的评论都装在这个框架之中，里面的评论并没有解析出来，所以才找不到div.reply-content元素。这时，我们需要加上对 iframe 的解析。
# driver.switch_to.frame(0)  # 1.用frame的index来定位，第一个是0
# driver.switch_to.frame("frame1")  # 2.用id来定位
# driver.switch_to.frame("myframe")  # 3.用name来定位
# driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))  # 4.用WebElement对象来定位

driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))

comments = driver.find_elements_by_css_selector('div.reply-content')
# 循环读取列表元素
for each in comments:
	content = each.find_element_by_tag_name('p')
	print(content.text)

'''

    find_element_by_id：通过元素的id选择，例如:driver.find_element_by_id(‘loginForm’)
    find_element_by_name：通过元素的name选择，driver.find_element_by_name(‘password’)
    find_element_by_xpath：通过xpath选择，driver.find_element_by_xpath(“//form[1]”)
    find_element_by_link_text：通过链接地址选择
    find_element_by_partial_link_text：通过链接的部分地址选择
    find_element_by_tag_name：通过元素的名称选择
    find_element_by_class_name：通过元素的id选择
    find_element_by_css_selector：通过css选择器选择

'''