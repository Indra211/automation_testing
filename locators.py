from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

d = wb.Firefox()
d.maximize_window()
d.get("https://naasongs.com.co/teluguwap-net-songs-download")
d.find_element(By.PARTIAL_LINK_TEXT,"Skip")
d.find_element(By.NAME,"q").send_keys("indra" + Keys.ENTER)
f=d.find_elements(By.TAG_NAME,"a")
print(len(f))
d.find_element(By.NAME,"site=sen&source=sensongsmp3").click()
print(d.title)

d.get("https://www.naukri.com/registration/createAccount?othersrcp=23531&wExp=N&utm_source=google&utm_medium=cpc&utm_campaign=Brand_Misspellings&gclid=Cj0KCQiAgaGgBhC8ARIsAAAyLfHUZqpNbdBR_eevYV0NYKn3C32jvkIdcApSepU8HFio7lz0khATIskaAtMyEALw_wcB&gclsrc=aw.ds")
e=d.find_elements(By.TAG_NAME,"div")
print(len(e))
print(d.title)

d.quit()



