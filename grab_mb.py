import os
import requests
from bs4  import BeautifulSoup

#absolute dir the script is in
script_dir = os.path.dirname(__file__)
opt_path   = "./"
file_path  = os.path.join(script_dir, opt_path)

#create folders
if not os.path.exists(file_path + "opt"):
    os.makedirs(file_path       + "opt")
if not os.path.exists(file_path + "msi"):
    os.makedirs(file_path       + "msi")
if not os.path.exists(file_path + "html"):
    os.makedirs(file_path       + "html")

Msi_H310 = file=open(file_path + "./msi/H310.html", "r", encoding = "utf8")
Msi_H370 = file=open(file_path + "./msi/H370.html", "r", encoding = "utf8")
Msi_B360 = file=open(file_path + "./msi/B360.html", "r", encoding = "utf8")
Msi_Z370 = file=open(file_path + "./msi/Z370.html", "r", encoding = "utf8")
Msi_Z390 = file=open(file_path + "./msi/Z390.html", "r", encoding = "utf8")
cname    = "productcard-link" #class_name
MBList1  = []

#for print all
Msi_List = [Msi_H310, Msi_H370, Msi_B360, Msi_Z370, Msi_Z390]
Msi_len  = len(Msi_List)

for board in Msi_List:
    order = 0 #set list
    if order != len(Msi_List):
        Msi_List.pop(order) #picking
        soup = BeautifulSoup(board, "html.parser")
        order += 1
        for link in soup.find_all("a", href=True): #getting links
            link = link.get('href')
            MBList1.append(link)

#sorting and remove duplicated
MBList2  = sorted(set(MBList1),key=MBList1.index)

#print out resaults
def output():
    with open(file_path + "./opt/output.json", "w") as f:
        for item in MBList2:
            d = "https://tw.msi.com/Motherboard/"
            item = item.split(d)[1] #get only name
            f.write("https://tw.msi.com/Motherboard/support/" + "%s\n" % item)

#okay.
output()
