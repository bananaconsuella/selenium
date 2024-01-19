import pytest
from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("Submit form with firstname:" + getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        log.info("Submit form with lastname:" + getData["lastname"])
        homepage.getLastName().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        log.info("Submit form with gender:" + getData["gender"])
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text
        log.info("Alert text:" + alertText)
        assert "Success" in alertText
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param

