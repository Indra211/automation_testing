'''
in css selectors have muliple items
1.tag_id
2. tag_class
3. tag_attribute
4.tag_class-attribute

 '''

from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



d = wb.Firefox()
d.maximize_window()
# tag and id
d.get("https://www.facebook.com/")
# d.find_element(By.CSS_SELECTOR,"#email").send_keys("9177468511" + Keys.ENTER)
# d.find_element(By.CSS_SELECTOR,"input#pass").send_keys("Indra@211" + Keys.ENTER)

"tag and class"
#d.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc" + Keys.ENTER)

"tag and attribute"

# d.find_element(By.CSS_SELECTOR,"input[name=email]").send_keys("abc")
" tag and class attribute "
d.find_element(By.CSS_SELECTOR,"input.inputtext[name=pass]").send_keys("abc")
print(d.title)
