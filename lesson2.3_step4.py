from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"

    browser = webdriver.Chrome()
    browser.get(link)

    button_a = browser.find_element_by_css_selector(".btn-primary")
    button_a.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(1)

    x_elem = browser.find_element_by_id("input_value")
    x = x_elem.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    button = browser.find_element_by_css_selector(".btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


