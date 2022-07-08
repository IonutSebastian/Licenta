import selenium
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

driver = webdriver.Firefox()  # options=options)


def waitUntilItVisibal(by: str, xpath: str) -> WebElement:
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((by, xpath)))
    return driver.find_element(by, xpath)
