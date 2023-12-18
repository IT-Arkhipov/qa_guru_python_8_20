import allure
import pytest
import requests
import utils

from selene import browser, query
from allure_commons._allure import step
from allure_commons.types import AttachmentType


@pytest.fixture(scope='session', autouse=True)
def cookie():
    with step("Получение авторизационной куки"):
        response = requests.post(url=utils.API_URL + "/login",
                                 data={"Email": utils.LOGIN, "Password": utils.PASSWORD, "RememberMe": False},
                                 allow_redirects=False)
        allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
        utils.cookie = response.cookies.get("NOPCOMMERCE.AUTH")


@pytest.fixture(scope='session', autouse=True)
def clear_cart(cookie):
    utils.open_cart()
    with step("Очистка корзины"):
        products_number = browser.element('.cart tbody').all('tr').get(query.size)
        for i in range(products_number):
            browser.element('.cart tbody').all('tr')[i].element('.remove-from-cart').click()
        browser.element('[name="updatecart"]').click()


@pytest.fixture(scope='function', autouse=True)
def init_browser():
    with step("Инициализация браузера"):
        browser.config.window_width = 1280
        browser.config.window_height = 1024

        yield browser

        browser.quit()
