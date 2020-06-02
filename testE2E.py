from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common import keys
from selenium.webdriver.support.select import Select
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utility.baseclass import BaseClass

class Testone(BaseClass):

    def test_e2e(self,getdata):

        self.driver.find_element_by_xpath("//a[@class='nav-link' and text()='Shop']").click()
        products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        for product in products:
            productname = product.find_element_by_xpath("div/h4/a").text
            if productname == "Blackberry":
                product.find_element_by_xpath("div/button").click()
        self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys(getdata[0])
        time.sleep(10)
        self.driver.find_element_by_xpath("//a[text()=getdata]").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_xpath("//input[@class='btn btn-success btn-lg']").click()
        print(self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text)
        self.driver.get_screenshot_as_file("endtoendtest.png")


@pytest.fixture(params=[("india"),("usa")])
def getdata(request):
    return request.param