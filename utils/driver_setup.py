from appium import webdriver
from utils.capabilities import get_ios_capabilities

def init_driver():
    options = get_ios_capabilities()
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)
    return driver


