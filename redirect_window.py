from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn_magic = browser.find_element(By.CSS_SELECTOR, "button.trollface.btn.btn-primary")
    btn_magic = btn_magic.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    y = str(calc(x))
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(By.ID, "answer").send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()