import pytest
from selenium import webdriver
from PageObjact.login_page import loginpage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_001_login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):

        self.logger.info("******************* Test_001_login *****************")
        self.logger.info("****************** verifying home page Title *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****************** home page Title Passed *****************")
        else:
            self.driver.save_screenshot(".\\ScreenShot\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.info("****************** home page Title Failed *****************")
            assert False

    def test_login(self,setup):
        self.logger.info("****************** Verifying login test *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title =="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("****************** Login page Title Passed *****************")
        else:
            self.driver.save_screenshot(".\\ScreenShot\\" + "test_login.png")
            self.driver.close()
            self.logger.info("****************** login page Title failed *****************")
            assert False



