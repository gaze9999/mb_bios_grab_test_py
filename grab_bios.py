import os
import requests
from bs4  import BeautifulSoup

#absolute dir the script is in
script_dir = os.path.dirname(__file__)
opt_path = "./"
file_path = os.path.join(script_dir, opt_path)

#make folder to download bios
if not os.path.exists(file_path + "bios"):
    os.makedirs(file_path       + "bios")

MsiLink = file=open(file_path + "./opt/output.json", "r", encoding = "utf8")

#fix it to one line later
MsiRead = MsiLink.readlines()

def output():
    with open(file_path + "./opt/output2.json", "w") as f:
        for item in MsiRead:
            f.write("%s\n" % item)

output()
