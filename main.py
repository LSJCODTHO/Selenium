import time

from selenium.webdriver.chrome.service import service
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="driver/chromedriver")

driver.get("https://portalerp.thomasgreg.com/web/login")
driver.implicitly_wait(0.5)
title = driver.title
print(title)

assert title == "Login | THOMAS GREG & SONS LIMITED (GUERNSEY) S.A."


text_box_user = driver.find_element(By.ID, value="login")
text_box_user.send_keys("asistente.virtual3")

text_box_pass = driver.find_element(By.ID, value="hidPassword")
text_box_pass.send_keys("Thomas-2021+")

button_login = driver.find_element(By.CLASS_NAME, value="btn")
button_login.click()

time.sleep(10)

text_box_name_user = driver.find_element(By.CLASS_NAME, value="o_main_navbar")
text_box_name_user = text_box_name_user.text
print(text_box_name_user)

driver.close()

time.sleep(10)