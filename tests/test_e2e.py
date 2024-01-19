from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.PurchasePage import PurchasePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()
        expectedProducts = ['iphone X', 'Samsung Note 8', 'Nokia Edge', 'Blackberry']
        actualProducts = []

        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("Getting items by hitting Shop")
        self.driver.implicitly_wait(5)

        cards = checkOutPage.getCardTitles()
        for card in cards:
            actualProductText = card.text
            log.info(actualProductText)
            actualProducts.append(actualProductText)
            if card.text == "Blackberry":
                checkOutPage.getCardButton().click()

        assert actualProducts == expectedProducts
        assert checkOutPage.getCheckOutButton().text == "Checkout ( 1 )\n(current)"

        purchasePage = checkOutPage.hitCheckOutButton()

        assert purchasePage.getContinueShopping().text == "Continue Shopping"
        assert purchasePage.getFinalCheckOut().text == "Checkout"

        confirmPage = purchasePage.hitFinalCheckOut()

        log.info("Entering country name as ukr")
        self.driver.find_element(By.ID, "country").send_keys("ukr")
        self.verifyLinkPresence("Ukraine")
        self. driver.find_element(By.LINK_TEXT, "Ukraine").click()

        log.info("Purchasing items by hitting Purchase button")
        confirmPage.checkAgreeToTerms().click()
        confirmPage.hitPurchaseButton().click()

        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("Response from application is " + successText)
        assert "Success!" in successText

