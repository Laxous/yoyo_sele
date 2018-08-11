# coding:utf -8
from bs4 import BeautifulSoup
import logging
logging.captureWarnings(True) #设置忽略警告
import requests
r = requests.get("https://www.qiushibaike.com/",verify=False)
soup = BeautifulSoup(r.content, "html.parser")
duanzi = soup.find_all(class_="content")
for i in duanzi:
    print (i.span.get_text().replace("\n",""))


