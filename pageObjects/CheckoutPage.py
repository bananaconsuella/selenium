from selenium.webdriver.common.by import By

from pageObjects.PurchasePage import PurchasePage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardButton = (By.CSS_SELECTOR, "button[class='btn btn-info']")
    checkOutButton = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardButton(self):
        return self.driver.find_element(*CheckOutPage.cardButton)

    def getCheckOutButton(self):
        return self.driver.find_element(*CheckOutPage.checkOutButton)

    def hitCheckOutButton(self):
        self.driver.find_element(*CheckOutPage.checkOutButton).click()
        purchasePage = PurchasePage(self.driver)
        return purchasePage
#        return self.driver.find_element(*CheckOutPage.checkOutButton)


