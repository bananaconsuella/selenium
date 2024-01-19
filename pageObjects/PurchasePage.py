from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class PurchasePage:
    def __init__(self, driver):
        self.driver = driver

    continueShopping = (By.CSS_SELECTOR, "button[class='btn btn-default']")
    finalCheckOut = (By.CSS_SELECTOR, "button[class='btn btn-success']")


    def getContinueShopping(self):
        return self.driver.find_element(*PurchasePage.continueShopping)

    def getFinalCheckOut(self):
        return self.driver.find_element(*PurchasePage.finalCheckOut)

    def hitFinalCheckOut(self):
        self.driver.find_element(*PurchasePage.finalCheckOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

    #assert self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-default']").text == "Continue Shopping"
   # assert self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").text == "Checkout"