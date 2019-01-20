import requests
from bs4  import BeautifulSoup

Msi_H310 = file=open("D:\\GitHub\\mb_bios_grab_test_py\\msi\\H310.html", "r", encoding = "utf8")
Msi_H370 = file=open("D:\\GitHub\\mb_bios_grab_test_py\\msi\\H370.html", "r", encoding = "utf8")
Msi_B360 = file=open("D:\\GitHub\\mb_bios_grab_test_py\\msi\\B360.html", "r", encoding = "utf8")
Msi_Z370 = file=open("D:\\GitHub\\mb_bios_grab_test_py\\msi\\Z370.html", "r", encoding = "utf8")
Msi_Z390 = file=open("D:\\GitHub\\mb_bios_grab_test_py\\msi\\Z390.html", "r", encoding = "utf8")
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
    with open("D:\\test\\output.json", "w") as f:
        for item in mbl2:
            f.write("%s\n" % item)

#okay.
output()
