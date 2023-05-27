import pytest
from selenium import webdriver
from PageObjact.login_page import loginpage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from PageObjact.AddcustomerPage import AddCustomer
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    def test_addcustomer(self,setup):
        self.logger.info("****************** Test_003_AddCustomer  *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****************login successful***********")

        self.logger.info("***********Starting Add Customer Test ******************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonCustomerMenu()
        self.addcust.clickonCustomerMenuItem()

        self.addcust.ClickonADDnew()

        self.logger.info("**********Providing Customer Info*************")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("Tejas12345")
        self.addcust.setFirstName("tejas")
        self.addcust.setLastName("Bhawsar")
        self.addcust.setGender("Male")
        self.addcust.setDOB("15-11-1995")
        self.addcust.setCompanyName("MS Global")
        self.addcust.setNewsletter()
        self.addcust.setCustomerRoles("Guest")
        self.addcust.setManagerofVender("Vendor 2")
        self.addcust.AdminComment("*****This is for Testing.........")
        self.addcust.ClickonSave()

        self.logger.info("**********Saving customer Info**************")

        self.msg = self.driver.find_element("xpath","//body/div[3]/div[1]/div[1]").text
        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("*******Add customer Test Passed***********")
        else:
            self.driver.save_screenshot(".\\ScreenShot\\" + "test_addCustomer_scr.png")
            self.logger.info("****************** Add customer Title failed *****************")
            assert True == False

        self.driver.close()
        self.logger.info("************ Ending Test_003_AddCustomer Test ")

def random_generator(size = 8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

