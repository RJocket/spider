'''
使用selenium加载网页爬取数据，往往比通过浏览器"检查"的方式，速度慢。
不复杂的话，则推荐使用"检查"方式，获取真实地址，进行数据抓取。
否则，也可以使用#控制CSS加载；#控制图片文件显示；#控制JavaScript的执行 等方式，提高selenium抓取数据速度
'''

'''
1.控制CSS。因为抓取过程中我们仅仅抓取页面的内容，CSS样式文件是用来控制页面的外观和元素放置位置的，对内容并没有影响。
因此我们可以限制网页加载CSS，从而减少抓取时间。代码如下所示：
'''
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

firefox_path = R"D:\软件\火狐\firefox.exe"
binary = FirefoxBinary(firefox_path)

caps = webdriver.DesiredCapabilities().FIREFOX#期望的能力，可以配置脚本运行的平台
caps["marionette"] = True

fp = webdriver.FirefoxProfile()
fp.set_preference("permissions.default.stylesheet",2)#配置优先权；禁用CSS 
fp.set_preference("permissions.default.image",2)#禁止加载图片
fp.set_preference("javascript.enabled",False)#禁止执行javascript
'''
#获取Firefox配置文件对象
 firefoxProfile = FirefoxProfile ##禁用CSS 
 firefoxProfile.set_preference（'permissions.default.stylesheet'，2）
 ##禁用图像
 firefoxProfile.set_preference（'permissions.default.image'，2 ）
 ##禁用Flash 
 firefoxProfile.set_preference（'dom.ipc.plugins.enabled.libflashplayer.so'，
'false'）
 ##设置修改后的配置文件创建浏览器对象
 self.browserHandle = webdriver.Firefox（firefoxProfile）
  
'''
driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp, capabilities=caps)

driver.get("http://www.santostang.com/2018/07/04/hello-world/")