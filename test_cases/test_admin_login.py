import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_AdminPage import Login_Admin_Page
from utilities.read_properties import ReadProperties
from utilities.custom_logger import Log_Maker


class TestAdminLogin:
    username = ReadProperties.get_user()
    password = ReadProperties.get_password()
    baseurl = ReadProperties.get_url()
    logger = Log_Maker.log_gen()

    def test_page_title_verification(self, setup):
        page_title = "Dashboard"
        self.logger.info("Testing page title verification")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title

        if page_title == act_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_page_title_verification.png")
            self.driver.close()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.login_lp = Login_Admin_Page(self.driver)
        self.login_lp.enter_text_box_email(self.username)
        self.login_lp.enter_text_box_password(self.password)
        self.login_lp.click_on_login_button()
        act_page_title = self.driver.find_element(By.XPATH, "//h6").text
        if act_page_title == "Dashboard":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_login.png")
            self.driver.close()
            assert False
