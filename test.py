import os
import requests
import urllib.request
from bs4  import BeautifulSoup

#absolute dir the script is in
script_dir = os.path.dirname(__file__)
opt_path   = "./"
file_path  = os.path.join(script_dir, opt_path)

url = "https://tw.msi.com/Motherboard/support/H310M-GAMING-PLUS"
# trying to get the html
r = urllib.request.urlopen(url)
results = requests.get(url).text
# x = BeautifulSoup(url, "html.parser")

# for link in results.find_all("a", href=True): #getting links
#     link = link.get('href')
#     MBList1.append(link)

def output():
    with open(file_path + "./opt/output3.json", "w") as f:
        for item in r: #remember to change
            f.write("%s" % item)

output()
