from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

driver.get("https://losangeles.craigslist.org/sfv/cto/d/la-crescenta-2005-toyota-corolla/7742679635.html")

time.sleep(3)

flag_icon = driver.find_element(By.XPATH, "//div[@class='flag']/div[@class='flagIcon']")
flag_icon.click()

time.sleep(30)


driver.quit()
