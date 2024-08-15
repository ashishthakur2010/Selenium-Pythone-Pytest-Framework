from selenium.webdriver.common.by import By


class Login_Admin_Page:
    textBox_userid_xpath = "//input[@name='username']"
    textBox_password_xpath = "//input[@name='password']"
    button_login_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def enter_into_textbox(self, textbox_id, text):
        self.driver.find_element(By.XPATH, textbox_id).clear()
        self.driver.find_element(By.XPATH, textbox_id).send_keys(text)

    def enter_text_box_email(self, user):
        self.enter_into_textbox(self.textBox_userid_xpath, user)

    def enter_text_box_password(self, password):
        self.enter_into_textbox(self.textBox_password_xpath, password)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()
