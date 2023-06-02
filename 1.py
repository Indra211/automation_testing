from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

db = wb.Chrome()
db.get("https://www.facebook.com/")
db.find_element(By.ID,"email").send_keys("9177*****" + Keys.ENTER)
db.find_element(by=By.ID,value="pass").send_keys("********" + Keys.ENTER)
db.find_element(by=By.ID,value="u_0_5_bv").click()
tt = db.title()
print(tt)
