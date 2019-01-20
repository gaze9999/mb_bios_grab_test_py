import os
import requests
from bs4  import BeautifulSoup

#absolute dir the script is in
script_dir = os.path.dirname(__file__)
msi_path = "msi/"
opt_path = "opt/"
msi_file_path = os.path.join(script_dir, msi_path)
opt_file_path = os.path.join(script_dir, opt_path)

Msi_H310 = file=open(msi_file_path + "H310.html", "r", encoding = "utf8")
Msi_H370 = file=open(msi_file_path + "H370.html", "r", encoding = "utf8")
Msi_B360 = file=open(msi_file_path + "B360.html", "r", encoding = "utf8")
Msi_Z370 = file=open(msi_file_path + "Z370.html", "r", encoding = "utf8")
Msi_Z390 = file=open(msi_file_path + "Z390.html", "r", encoding = "utf8")
cname    = "productcard-link" #class_name
mbl1     = []
Msi_List = [Msi_H310, Msi_H370, Msi_B360, Msi_Z370, Msi_Z390]
Msi_len  = len(Msi_List)

for br in Msi_List:
    ord = 0
    if ord != len(Msi_List):
        Msi_List.pop(ord)
        soup = BeautifulSoup(br, "html.parser")
        ord += 1
        for link in soup.find_all("a", href=True):
            link = link.get('href')
            mbl1.append(link)

#sorting and remove duplicated
mbl2     = sorted(set(mbl1),key=mbl1.index)

#print out resaults
def output():
    with open(opt_file_path + "output.json", "w") as f:
        for item in mbl2:
            f.write("%s\n" % item)

#okay.
output()
