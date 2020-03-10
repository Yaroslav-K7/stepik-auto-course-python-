from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # ожидание цены 12сек
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    button_b = browser.find_element(By.ID, "book").click()

    x_elem = browser.find_element(By.ID, "input_value")

    # скрол к элементу
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_elem)

    x = x_elem.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    input_answer = browser.find_element(By.ID, "answer").send_keys(y)

    button = browser.find_element(By.ID, "solve").click()

finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


