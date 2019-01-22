import os
import requests
import urllib.request
from bs4  import BeautifulSoup

#absolute dir the script is in
script_dir = os.path.dirname(__file__)
opt_path   = "./"
file_path  = os.path.join(script_dir, opt_path)

#make folder to download bios
if not os.path.exists(file_path + "bios"):
    os.makedirs(file_path       + "bios")

#open grab_mb.py
Links       = file=open(file_path + "./opt/output.json", "r", encoding = "utf8")
LinkList    = []  #for read
LinkList2   = [] #for output
LinkListLen = len(LinkList)

#add to list
for Link in Links:
    LinkList.append(Link.strip() + ", ")

#fucked up, fix it first
x       = LinkList.pop(0)
results = requests.get(x)
i       = BeautifulSoup(results, "html.parser")
y       = i.find_all("a", href=True)

#later works when done upside code
"""
for bios in LinkList:
    order = 0 #set list
    if order != len(LinkList):
        LinkList.pop(order) #picking
        soup = BeautifulSoup(bios, "html.parser")
        order += 1
        for link in soup.find_all("a", href=True): #getting links
            link = link.get('href')
            LinkList2.append(link)
"""

def output():
    with open(file_path + "./opt/output2.json", "w") as f:
        for item in results: #remember to change
            f.write("%s" % item)

output()
