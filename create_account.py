import pytest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("http://seleniumdemo.com/?page_id=7")
    yield
    driver.quit()

def test_create_account_failed(test_setup):
    driver.find_element(By.ID, "reg_email").send_keys("blabla@wp.pl")
    driver.find_element(By.ID, "reg_password").send_keys("blachara123")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)
    msg = "An account is already registered with your email address. Please log in."
    assert msg in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text

def test_create_account_passed(test_setup):
    email = str(random.randint(0,100)) + "blabla@wp.pl"
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys("blachara123")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)
    msg = "An account is already registered with your email address. Please log in."
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()