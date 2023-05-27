import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select


class AddCustomer():
    link_Customers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    link_Customers_menuitem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p "
    btnAddnew_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    CB_MaleGender_id = "Gender_Male"
    CB_FemaleGender_id = "Gender_Female"
    txtDOB_xpath = "//input[@id='DateOfBirth']"
    txt_CompanyName_xpath = "//input[@id='Company']"
    txt_NewsLetter_xpath = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"
    txt_NewsLetterTS_Xpath = "//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[2]]"
    txtCustomerroles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[1]"
    lstitemGuest_xpath = "//li[contains(text(),'Guests')]"
    lstitemRegister_xpath = "//li[contains(text(),'Registered')]"
    lstitemVendors_xpath = "//select[@id='VendorId']"
    drpmgrVendor_id = "//select[@id='VendorId']"
    CB_Active_xpath = "//input[@id='Active']"
    txt_Comment_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/button[1]"



    def __init__(self, driver):
        self.driver = driver

    def clickonCustomerMenu(self):
        self.driver.find_element("xpath",self.link_Customers_menu_xpath).click()

    def clickonCustomerMenuItem(self):
        self.driver.find_element("xpath",self.link_Customers_menuitem_xpath).click()

    def ClickonADDnew(self):
        self.driver.find_element("xpath",self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element("xpath",self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element("xpath",self.txtPassword_xpath).send_keys(password)

    def setFirstName(self,fname):
        self.driver.find_element("xpath",self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element("xpath",self.txtLastName_xpath).send_keys(lname)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element("id",self.CB_MaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element("id", self.CB_FemaleGender_id).click()
        else:
            self.driver.find_element("id", self.CB_MaleGender_id).click()

    def setDOB(self,dob):
        self.driver.find_element("xpath",self.txtDOB_xpath).send_keys(dob)

    def setCompanyName(self,companyname):
        self.driver.find_element("xpath",self.txt_CompanyName_xpath).send_keys(companyname)

    def setNewsletter(self):
        news = self.driver.find_element("xpath",self.txt_NewsLetter_xpath).click()
        news1 = Select(news)
        news1.select_by_index(1)
        # self.driver.find_element("xpath",self.txt_NewsLetterTS_Xpath).click()

    def setCustomerRoles(self,role):
        self.driver.find_element("xpath",self.txtCustomerroles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element("xpath",self.lstitemRegister_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element("xpath",self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            #here user can be Registered or Guest, only one
            time.sleep(2)
            self.driver.find_element("xpath","//span[@title='delete']").click()
            self.listitem = self.driver.find_element("xpath",self.lstitemGuest_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element("xpath", self.lstitemRegister_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element("xpath", self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element("xpath", self.lstitemGuest_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setManagerofVender(self,value):
        drp =self.driver.find_element("xpath",self.drpmgrVendor_id).click()
        drpp = Select(drp)
        drpp.select_by_visible_text(value)

    def AdminComment(self,comment):
        self.driver.find_element("xpath",self.txt_Comment_xpath).send_keys(comment)

    def ClickonSave(self):
        self.driver.find_element("xpath",self.btnSave_xpath).click()





