import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

#absolute dir the script is in
script_dir = os.path.dirname(__file__)
opt_path   = "./"
file_path  = os.path.join(script_dir, opt_path)

url = "https://tw.msi.com/Motherboard/"
driver = webdriver.Chrome()
driver.get(url)

#defined sth
ChkBox = driver.find_element_by_class_name("checkbox")
ChkBoxChkd = driver.find_element_by_class_name("checkbox checked")
BdList = [Z390, Z370, H370, B360, H310]

#getting checkbox ID
class BdClass:
    def ClassGet():
        for BId in BdList:
            BdId = "Intel-" + BId

BdList[0] = driver.find_element_by_id()


def FillBoard():
    for name in BdList:

# Z390Chkd = Z390.find_element_by_class_name("checkbox-icon")
