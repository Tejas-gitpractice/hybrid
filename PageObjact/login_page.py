class loginpage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[normalize-space()='Log in']"
    link_logout_linktext = "//*[@id='navbarText']/ul/li[3]/a"

    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,username):
        self.driver.find_element("id",self.textbox_username_id).clear()
        self.driver.find_element("id",self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element("id",self.textbox_password_id).clear()
        self.driver.find_element("id",self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element("xpath",self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element("xpath",self.link_logout_linktext).click()






