import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

#absolute dir the script is in
script_dir = os.path.dirname(__file__)
opt_path   = "./"
file_path  = os.path.join(script_dir, opt_path)

BdList     = ["Z390", "Z370", "H370", "B360", "H310"]
PriList    = []
for Bd in BdList:
    order = 0
    if order != 3:
        BdList.pop(order)
        Xpth = '//input[@id="Intel-' + Bd + '"]' + str(order) + "\n"
        PriList.append(Xpth)
        order += 1

def output():
    with open(file_path + "./opt/output4.json", "w") as f:
        for item in PriList:
            f.write("%s" % item)

output()
