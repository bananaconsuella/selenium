from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    lastname = (By.NAME, "email")
    gender = (By.ID,  "exampleFormControlSelect1")
    check = (By.ID, "exampleCheck1")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    successMessage = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getLastName(self):
        return self.driver.find_element(*HomePage.lastname)

    def getCheckBox(self):
       return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)