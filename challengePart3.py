
from time import sleep
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



driver= webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)

url ="https://www.saucedemo.com/"
driver.get(url)
driver.maximize_window()
driver.find_element(By.ID,'user-name').clear()
driver.find_element(By.ID,'user-name').send_keys('standard_user')

driver.find_element(By.ID,'password').clear()
driver.find_element(By.ID,'password').send_keys('secret_sauce')

driver.find_element(By.ID,'login-button').click()

priceTags=driver.find_elements(By.XPATH,"//div[@class='inventory_item_price']")
max=0
i=0
iMax=0

for e in priceTags:
    i=i+1
    price=float(e.text.replace('$',''))
    if price>max:
        max=price
        iMax=i

xpath="(//div[@class='pricebar']/button)["+str(iMax)+"]"
productName = driver.find_element(By.XPATH,"(//a[contains(@id,'item') and contains(@id,'title_link')])["+str(iMax)+"]").text

driver.find_element(By.XPATH,xpath).click()
time.sleep(3)
driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[text()='"+productName+"']").click()
time.sleep(3)

driver.quit()


        




