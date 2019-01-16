import requests
from lxml import html
from bs4  import BeautifulSoup

url_msi  = 'https://tw.msi.com/Motherboards' #test_on_msi
html     = requests.get(url_msi).text.encode('UTF-8', 'ignore')
soup     = BeautifulSoup(html, 'lxml')
cname    = 'productcard card' #class_name

soup.prettify()

#do_nothing_try_later
def grab_name():
    for mbn in soup.find_all('div', cname):
        print(mbn.get('title'))

#print out resaults
def output():
    file=open('D:\\test\\output.json', 'wb')
    file.write(html)

#okay.
output()
