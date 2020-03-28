import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', ['236895', "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, url):
    link = f"https://stepik.org/lesson/{url}/step/1/"
    browser.get(link)

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'textarea'))).send_keys(str(math.log(int(time.time()))))

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission '))).click()

    check_status = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))).text

    assert check_status == "Correct!", "Answer isn't correct"
