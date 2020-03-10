from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    first_elem = browser.find_element_by_id("num1")
    second_elem = browser.find_element_by_id("num2")
    sum_first_second = int(first_elem.text) + int(second_elem.text)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(sum_first_second))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
