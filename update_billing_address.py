import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
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

def test_create_account_passed(test_setup):
    email = str(random.randint(0,100)) + "blabla@wp.pl"
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys("blachara123")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)
    driver.find_element(By.LINK_TEXT, "Addresses").click()
    driver.find_element(By.LINK_TEXT, "Edit").click()
    driver.find_element(By.ID, "billing_first_name").send_keys("Johny")
    driver.find_element(By.ID, "billing_last_name").send_keys("Dee")
    Select(driver.find_element(By.ID, "billing_country")).select_by_visible_text("Poland")
    driver.find_element(By.ID, "billing_address_1").send_keys("kwiatowa 1")
    driver.find_element(By.ID, "billing_postcode").send_keys("00-111")
    driver.find_element(By.ID, "billing_city").send_keys("Warsaw")
    driver.find_element(By.ID, "billing_phone").send_keys("111111111")
    driver.find_element(By.XPATH, "//button[@value='Save address']").click()

    assert 'Address changed successfully' in driver.find_element(By.XPATH, "//div[@class='woocommerce-message']").text
