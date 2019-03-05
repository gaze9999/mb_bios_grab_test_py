import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#absolute dir the script is in
script_dir = os.path.dirname(__file__)
opt_path   = "./"
file_path  = os.path.join(script_dir, opt_path)

url    = "https://tw.msi.com/Motherboard/"
if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(1600, 900)
    driver.get(url)


#defined sth
BdList   = ["Z390", "Z370", "H370", "B360", "H310"]
ProSec   = ["2243", "2052", "2167", "2166", "2165"] #reference to top
MainList = []
PriList  = []
Xpth     = ""

def SclDwn():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(3)

class GetPages:
    for Bd in BdList:
        order = 0
        if order != 1:
            Xpth = '//input[@id="Intel-' + Bd + '"]' + "\n"
            driver.find_element_by_xpath(Xpth).send_keys(Keys.SPACE) #Selecting checkbox
            SclDwn()
            SclDwn() #scroll down to load page
            MainList = driver.find_elements_by_css_selector("h4.card-title a.productcard-link") #Making a list
            for link in MainList:
                order = 0 #set list
                if order != len(MainList):
                    Link = link.get_attribute("href") + "\n" #innerHTML #grab board link
                    PriList.append(Link)
                    order += 1
            driver.execute_script("window.scrollTo(0, 0)")
            sleep(1)
            driver.refresh()
            order += 1
            sleep(3)

def output():
    with open(file_path + "./opt/output4.json", "w") as f:
        for item in PriList:
            f.write("%s" % item)

output()
driver.close()
