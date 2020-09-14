from selenium.webdriver.common.keys import Keys

from locators import locators

class MyAccountPage:

    def __init__(self,driver):
        self.driver = driver
        # my account page elements
        self.username_input = locators.MyAccountPage.username_input
        self.password_input = locators.MyAccountPage.password_input
        self.reg_email_input = locators.MyAccountPage.reg_email_input
        self.reg_password_input = locators.MyAccountPage.reg_password_input
        self.logout_link = locators.MyAccountPage.logout_link
        self.error_msg = locators.MyAccountPage.error_msg

    def open_page(self):
        self.driver..get("http://seleniumdemo.com/?page_id=7")

    def log_in(self, username, password):
        # przechodzimy do logowania
        self.driver.find_element(self.username_input).send_keys(username)
        self.driver.find_element(self.password_input).send_keys(password)
        self.driver.find_element(self.password_input).send_keys(Keys.ENTER)

    def create_account(self, email, password):
        self.driver.find_element(self.reg_email_input).send_keys(email)
        self.driver.find_element(self.reg_password_input).send_keys(password)
        self.driver.find_element(self.reg_password_input).send_keys(Keys.ENTER)

    def is_logout_link_displayed(self):
        return self.driver.find.element(self.logout_link).is_displayed()

    def get_error_message(self):
        return self.driver.find_element(self.error_msg).text
