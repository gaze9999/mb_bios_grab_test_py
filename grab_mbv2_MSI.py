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
ProSec   = ["2243", "2052", "2167", "2166", "2165"] #reference to top
MainList = []
PriList  = []
Xpth     = ""

# for Bd in BdList:
#     order = 0
#     if order != 3:
#         Bd = BdList.pop(order)
#         Xpth = '//input[@id="Intel-' + Bd + '"]'
#         order += 1

def toText():
    #grab each link in list
    for link in MainList:
        order = 0 #set list
        if order != len(MainList):
            link = link.get_attribute("href") + "\n" #innerHTML #grab board link
            PriList.append(link)
            order += 1

def SclDwn():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(3)

class GetPages:
    for Bd in BdList:
        order = 0
        if order != 1:
            BdList.pop()
            Xpth = '//input[@id="Intel-' + Bd + '"]' + "\n"
            driver.find_element_by_xpath(Xpth).send_keys(Keys.SPACE) #Selecting checkbox
            SclDwn()
            SclDwn()
            driver.execute_script("window.scrollTo(0, 0)")
            sleep(1)
            MainList = driver.find_elements_by_xpath("//h4/a[@class='productcard-link']")#Making a list
            toText()
            driver.refresh()
            order += 1
            sleep(3)

def output():
    with open(file_path + "./opt/output4.json", "w") as f:
        for item in PriList:
            f.write("%s" % item)

output()
driver.close()
