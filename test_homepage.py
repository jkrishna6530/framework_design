from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common import keys
from selenium.webdriver.support.select import Select
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageobject import Homepage
from pageobject.Homepage import homepagedata
from utility.baseclass import BaseClass

class Testtwo(BaseClass):

    def test_login(self,getdata1):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        self.driver.find_element_by_xpath("//div[@class='form-group']//input[@name='name']").send_keys(getdata1[firstname])
        time.sleep(10)



    @pytest.fixture(params=homepagedata.gettestdata("testcase2"))
    def getdata1(self,request):
        return request.param

        
