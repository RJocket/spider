#coding =UTF-8
import MySQLdb
# 创建连接
conn = MySQLdb.connect(host='localhost',user='root',passwd='136951',db='scraping')
# 获取游标
cur = conn.cursor()
#执行SQL语句
cur.execute("INSERT INTO urls(url,content) VALUES ('www.aiqiyi.com','aiqiyi')")
# 关闭游标
cur.close()
# 提交
conn.commit()
# 关闭连接
conn.close()