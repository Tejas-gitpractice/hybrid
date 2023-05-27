import time

import pytest
from selenium import webdriver
from PageObjact.login_page import loginpage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils


class Test_002_DDT_login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("******************Test_002_DDT_login*********************")
        self.logger.info("****************** Verifying login DDT test *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in an Excel:", self.rows)

        lst_status = []

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("******Passed*****")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("******Failed*******")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("******Failed*****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("******Passed*****")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("********login DDT test passed*********")
            self.driver.close()
            assert True
        else:
            self.logger.info("******Login DDT test failed********")
            self.driver.close()
            assert False

        self.logger.info("*********end of login DDt test*************")
        self.logger.info("*********Completed TC_LoginDDT_002*************")
