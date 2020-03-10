from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys("Yaroslav")

    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("Kuznietsov")

    email = browser.find_element_by_name("email")
    email.send_keys("yaroslav.kuznetsov1994@gmail.com")

    file = browser.find_element_by_name("file")
    current_dir = os.path.abspath('/Users/ykuzniet/PycharmProjects/stepik_auto/')
    file_path = os.path.join(current_dir, 'true.txt')
    file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
