import sys
import os
import urllib.request
import requests
from lxml import html
from bs4 import BeautifulSoup

url_msi  = 'https://tw.msi.com/Motherboards'
html     = requests.get(url_msi).text.encode('UTF-8', 'ignore')
cname    = 'productcard card'

#def grab_name():

#print out resaults
try:
    def output():
        file=open('D:\\test\\output.txt', 'wb')
        file.write(html)
        file.close()
except Exception as e:
    file.write('error')
    file.close()


output()
