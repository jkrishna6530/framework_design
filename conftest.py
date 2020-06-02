import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common import keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ChromeOptions
@pytest.fixture()
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    path = "C:/Users/JAI Krishna/PycharmProjects/Framework_Design/Resource/chromedriver.exe"
    driver = webdriver.Chrome(path, options=chrome_options)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(10)

    request.cls.driver=driver
    yield
    driver.close()

