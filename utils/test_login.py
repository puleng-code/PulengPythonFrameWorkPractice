import allure
import pytest

from tests.loginPage import LoginPage
from utils.readProperties import ReadConfig


# call the variables in the readProperties by imprting and using the ReadConfig method
class test_001_LoginToSauceDemo:
    BaseURL = ReadConfig().getBaseURL()
    Username = ReadConfig().getUserName()
    Password = ReadConfig().getPassword()


@pytest.mark.Regression
@allure.severity(allure.severity_level.CRITICAL)
def test_loginTests(self, setup):
    self.driver = setup
    self.driver.get(self.BaseURL)
    self.driver.maximize_window()
    # creating the instance of the Login Page
    self.lp = LoginPage(self.driver)
    self.lp.enterUsername(self.Username)
    self.lp.enterPassword(self.Password)
