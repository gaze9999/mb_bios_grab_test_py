import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#absolute dir the script is in
script_dir = os.path.dirname(__file__)
opt_path   = "./"
file_path  = os.path.join(script_dir, opt_path)

APri    = "https://www.asus.com/tw/Motherboards/ASUS-Prime-Products/"
ARog    = "https://www.asus.com/tw/Motherboards/ROG-Republic-of-Gamers-Products/"
ATuf    = "https://www.asus.com/tw/Motherboards/TUF-The-Ultimate-Force-Products/"
ATfG    = "https://www.asus.com/tw/Motherboards/TUF-Gaming-Products/"
ACom    = "https://www.asus.com/tw/Motherboards/Commercial-Products/"
driver  = webdriver.Chrome()
driver.get(APri) #testing

#defined sth
Xpth    = "//*[@id="af-react"]/div/div/div[1]/section/div/div[2]/div[1]/div[2]/div[2]/ul/li[2]/label"

class GetPages:
    driver.find_element_by_xpath(Xpth).send_keys(Keys.SPACE) #Selecting checkbox
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(3)
    MainList = driver.find_elements_by_xpath('') #Making a list

    #grab each link in list
    for link in MainList:
        order = 0 #set list
        if order != len(MainList):
            MainList.pop(order) #picking
            link = link.get_attribute("href") + "\n" #grab board link
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
