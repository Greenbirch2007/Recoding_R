#! -*- coding:utf-8 -*-
import pymysql
import requests
from lxml import etree
from selenium import webdriver

driver = webdriver.Chrome()

def get_one_page(url):

    driver.get(url)
    html = driver.page_source
    driver.quit()
    return html


def parse_page(html):
    selector = etree.HTML(html)
    title = selector.xpath("/html/body/ul[1]/li/a/text()")
    links = selector.xpath("/html/body/ul[1]/li/a/@href")
    #
    for i1,i2,in zip(title,links):
        big_list.append((i1,"https://cloud.r-project.org/web"+i2[2:]))
    return big_list





def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='R',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # 这里是判断big_list的长度，不是content字符的长度
    try:
        cursor.executemany('insert into R_Finance (title,links) values (%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except :
        print('出列啦')



if __name__ == "__main__":
    big_list = []

    url = "https://cloud.r-project.org/web/views/Finance.html"
    html = get_one_page(url)
    cont = parse_page(html)
    insertDB(cont)

#
# create table R_Finance(
# id int not null primary key auto_increment,
# title text,
# links text
# ) engine=InnoDB  charset=utf8;


# drop  table R_links;