'''
mysql 增删改查 SQL语句
'''
show databases;
CREATE DATABASE scraping;
USE scraping;
CREATE TABLE urls(
	id INT NOT NULL AUTO_INCREMENT,
    url VARCHAR(1000) NOT NULL,
    content VARCHAR(4000) NOT NULL,
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY(id)
);
DESCRIBE urls;
INSERT INTO urls (url, content) VALUES ("www.baidu.com","content");
SELECT * FROM urls WHERE id=1;
SELECT url,content FROM urls WHERE id =1;
SELECT id,url FROM urls WHERE content LIKE "%content%";
INSERT INTO urls (url,content) VALUES ("www.mysql.com","sql");
SET SQL_SAFE_UPDATES =0;
DELETE FROM urls WHERE content = "content";
SELECT * FROM urls;
INSERT INTO urls(url,content) VALUES ("www.baidu.com","content");
SELECT * FROM urls;
UPDATE urls SET url ="www.google.com",content ="Goole" WHERE  id=2;

'''
MYSQL数据表建立外键 

MySQL创建关联表可以理解为是两个表之间有个外键关系，但这两个表必须满足三个条件
1.两个表必须是InnoDB数据引擎
2.使用在外键关系的域必须为索引型(Index)
3.使用在外键关系的域必须与数据类型相似
 
例如：
1、建立s_user表
create table s_user(
       u_id int auto_increment primary key,
       u_name varchar(15),
       u_pwd varchar(15),
       u_truename varchar(20),
        u_role varchar(6),
       u_email varchar(30)
)
2、
插入几条数据
insert into s_user values
       (1,"wangc","aaaaaa","wangchao","buyer","wang@163.com"),
      (2,"huangfp","bbbbbb","huangfp","seller","huang@126.com"),
      (3,"zhang3","cccccc","zhangsan","buyer","zhang@163.com"),
      (4,"li4","dddddd","lisi","seller","li@1256.com")
3、
建立s_orderform表
create table s_orderform(
          o_id int auto_increment primary key,
         o_buyer_id int,
         o_seller_id int,
         o_totalprices double,
         o_state varchar(50),
         o_information varchar(200),
         foreign key(o_buyer_id) references s_user(u_id),      #外链到s_user表的u_id字段
         foreign key(o_seller_id) references s_user(u_id)      #外链到s_user表的u_id字段
)
'''