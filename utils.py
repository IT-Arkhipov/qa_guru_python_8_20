import allure

from allure_commons._allure import step
from allure_commons.types import AttachmentType
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


def add_screenshot(_browser):
    png = _browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')
