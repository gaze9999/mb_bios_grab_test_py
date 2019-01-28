import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#absolute dir the script is in
script_dir = os.path.dirname(__file__)
opt_path   = "./"
file_path  = os.path.join(script_dir, opt_path)

url    = "https://tw.msi.com/Motherboard/"
driver = webdriver.Chrome()
driver.get(url)

#defined sth
BdList   = ["Z390", "Z370", "H370", "B360", "H310"]
MainList = []
PriList  = []

# class GetPages():
driver.find_element_by_xpath('//input[@value="2243"]').send_keys(Keys.SPACE)
sleep(1)
MainList = driver.find_elements_by_xpath('//a[@class="productcard-link"]')

for link in MainList:
    order = 0 #set list
    if order != len(MainList):
        MainList.pop(order) #picking
        link = link.get_attribute("href") + "\n"
        PriList.append(link)
        order += 1

def output():
    with open(file_path + "./opt/output4.json", "w") as f:
        for item in PriList:
            f.write("%s" % item)

# old things
# ChkBox = driver.find_element_by_class_name("checkbox")
# ChkBoxChkd = driver.find_element_by_class_name("checkbox checked")
# Z390 = driver.find_element_by_id("Intel-Z390")

output()
driver.close()
