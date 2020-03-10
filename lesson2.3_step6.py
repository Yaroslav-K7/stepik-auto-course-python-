from selenium import webdriver
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"

    browser = webdriver.Chrome()
    browser.get(link)

    button_a = browser.find_element_by_css_selector(".trollface.btn")
    button_a.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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
    # закрываем браузер после всех манипуляций
    browser.quit()

