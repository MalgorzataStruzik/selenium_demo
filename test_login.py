import pytest
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
    driver.get("http://seleniumdemo.com/")
    yield
    driver.quit()

def test_log_in_passed(test_setup):
    # przechodzimy do logowania
    driver.find_element(By.XPATH, "//li[@id='menu-item-22']//a").click()
    driver.find_element(By.ID, "username").send_keys("bleble@wp.pl")
    driver.find_element(By.ID, "password").send_keys("blachara123")
    driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()

def test_log_in_failed(test_setup):
    # przechodzimy do logowania
    driver.find_element(By.XPATH, "//li[@id='menu-item-22']//a").click()
    driver.find_element(By.ID, "username").send_keys("bleble@wp.pl")
    driver.find_element(By.ID, "password").send_keys("blachara123123")
    driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

    assert "ERROR: Incorrect username or password." in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text
