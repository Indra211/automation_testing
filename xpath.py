'''
/html/body/form/div[3]/table[2]/tbody/tr[2]/td[1]/table/tbody/tr/td/div/ul/li/a   

//*[@id="lnkLogins"] # partial x path

/html/body/form/div[3]/table[2]/tbody/tr[1]/td/table/tbody/tr/td/img

//*[@id="Image2"]

//a[@id="lnkLogins"]
//a[@id='lnkLogins']

/html[1]/body[1]/form[1]/div[3]/table[2]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/ul[1]/li[1]/a[1]

or
and
contains
starts-with
text

'''

from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

d = wb.Firefox()
d.maximize_window()
d.get("https://www.facebook.com/")
d.find_element(By.XPATH,"//*[contains(@id,em)]").send_keys("9177468511")
d.find_element(By.XPATH,"//*[starts-with(@id,pa)]").send_keys("Indra")
d.find_element(By.XPATH,"//h2[text()='Facebook']")
print(d.title)
