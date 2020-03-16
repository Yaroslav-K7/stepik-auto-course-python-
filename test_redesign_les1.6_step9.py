from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


def r_browser(self, link):
    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys(
        "Name")
    input_last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys(
        "LastName")
    input_email = browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys(
        "test1@test.com")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # welcome_text = WebDriverWait(browser, 3).until(
    #     EC.presence_of_element_located(By.TAG_NAME, "h1")).text
    self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    browser.quit()


class TestRedesign(unittest.TestCase):
    def test_valid_check(self):
        r_browser(self, link1)

    def test_invalid_check(self):
        r_browser(self, link2)


if __name__ == "__main__":
    unittest.main()
