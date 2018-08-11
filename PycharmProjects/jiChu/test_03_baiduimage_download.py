# coding=utf-8
import time
import os
import urllib
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1533044452523_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=python"
driver = webdriver.Chrome()
driver.get(url)
page = driver.page_source
time.sleep(5)
soup = BeautifulSoup(page, "html.parser")
a = soup.find_all(class_="main_img img-hover")
for i in range(len(a)):
    pic_url = a[i]["data-imgurl"].replace("amp;", "")
    print("第%d张图片地址已找到" % (i + 1))
    print(pic_url)
    # ------ 这里最好使用异常处理及多线程编程方式 ------
    img_path = 'D:\\Temp\\'  # 下载图片存放文件夹
    # 如果不存在这个下载图片文件夹，就自动创建一个
    if not os.path.exists(img_path): os.mkdir(img_path)

    try:
        pic = requests.get(pic_url, timeout=5)  # 超时异常判断 5秒超时
        f = open(img_path + str(i) + ".jpg", 'wb')
        f.write((urllib.request.urlopen(pic_url)).read())
        print("第%d张图片已完成下载" % i)
        f.close()
    except Exception as e:
        print(str(i) + " error")

print("all download")
driver.quit()
