from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

#    selectCountry = (By.ID, "country")
    agreeToTerms = (By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']")
    purchaseButton = (By.CSS_SELECTOR, "input[type='submit']")

#    def getCountry(self):
#        return self.driver.find_elements(*ConfirmPage.selectCountry)

    def checkAgreeToTerms(self):
        return self.driver.find_element(*ConfirmPage.agreeToTerms)

    def hitPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)
