import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

#absolute dir the script is in
script_dir = os.path.dirname(__file__)
opt_path   = "./"
file_path  = os.path.join(script_dir, opt_path)

#getting driver
url = "https://tw.msi.com/Motherboard/support/H310M-GAMING-PLUS#down-bios"
driver = webdriver.Chrome()
driver.get(url)

#get link
element = driver.find_element_by_class_name("hvr-bob")
x = element.get_attribute("href")

def output():
    with open(file_path + "./opt/output4.json", "w") as f:
        for item in x: #remember to change
            f.write("%s" % item)

output()
driver.close()
