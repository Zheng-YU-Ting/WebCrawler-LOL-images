# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 10:23:45 2021

@author: CJCU-CC
"""

import urllib.request
import requests
from bs4 import BeautifulSoup

URL = "https://lol.garena.tw/champions"
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
req = requests.get(URL,headers = headers)
req.encoding="utf8"

soup = BeautifulSoup(req.text, "html.parser")

img = soup.find_all("img")


for i in range(0,len(img)):
    img_src = img[i].get("src")

    urllib.request.urlretrieve(img_src, "C:\\Users\\MSI\Desktop\\作業\\三上\\物聯網大數據分析\\python程式\\homework1028_images\\"+  str(i) + ".jpg")

    print("第",str(i),"張圖")

