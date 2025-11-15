from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles_in_en = driver.find_elements(By.CSS_SELECTOR, "#articlecount ul li")[1].find_element(By.CSS_SELECTOR, "a").text

print()
