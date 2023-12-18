from allure_commons._allure import step
from selene import browser


LOGIN = "qa.testing.robot@gmail.com"
PASSWORD = "isWTa5*VdmKi6"
WEB_URL = "https://demowebshop.tricentis.com/"
API_URL = "https://demowebshop.tricentis.com/"
cookie = ''


def open_cart():
    with step("Открытие корзины"):
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open(WEB_URL)
        browser.element('.header-links').element('a[href="/cart"]').click()

