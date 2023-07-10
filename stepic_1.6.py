import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link ="http://suninjuly.github.io/find_link_text"


browser = webdriver.Chrome()
browser.get(link)

try:
    link = browser.find_element(By.PARTIAL_LINK_TEXT, "224592")
    link.click()

    browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
    browser.find_element(By.NAME, "last_name").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")
    browser.find_element(By.CSS_SELECTOR, "#submit_button").click()
    browser.find_element(By.CSS_SELECTOR, "#submit_button").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

