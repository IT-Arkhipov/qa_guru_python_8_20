import json

import requests
import logging
import utils
import allure

from utils import *
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import browser, query
from selene.support.conditions import have


def test_add_books_to_the_cart():
    with step("Добавление книги в корзину"):
        payload = {"addtocart_13.EnteredQuantity: 1": 1}
        response = requests.post(url=API_URL + 'addproducttocart/details/13/1', data=payload,
                                 cookies={"NOPCOMMERCE.AUTH": utils.cookie})
        allure.attach(body=json.dumps(response.json(), indent=2, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.json())

    utils.open_cart()
    with step("Проверка наименования добавленной книги в корзине"):
        browser.element('.order-summary-content').should(have.text('Computing and Internet'))


def test_add_notebook_to_the_cart():
    with step("Добавление ноутбука в корзину"):
        payload = {"addtocart_31.EnteredQuantity: 1": 1}
        response = requests.post(url=API_URL + 'addproducttocart/details/31/1', data=payload,
                                 cookies={"NOPCOMMERCE.AUTH": utils.cookie})
        allure.attach(body=json.dumps(response.json(), indent=2, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.json())

    utils.open_cart()
    with step("Проверка наименования добавленного ноутбука в корзине"):
        browser.element('.order-summary-content').should(have.text('14.1-inch Laptop'))


def test_add_desktop_to_the_cart():
    with step("Добавление десктопного компьютера в корзину"):
        payload = {
          "product_attribute_72_5_18": 53,
          "product_attribute_72_6_19": 54,
          "product_attribute_72_3_20": 57,
          "addtocart_72.EnteredQuantity": 1,
        }
        response = requests.post(url=API_URL + 'addproducttocart/details/72/1', data=payload,
                                 cookies={"NOPCOMMERCE.AUTH": utils.cookie})
        allure.attach(body=json.dumps(response.json(), indent=2, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.json())

    utils.open_cart()
    with step("Проверка наименования десктопного компьютера в корзине"):
        browser.element('.order-summary-content').should(have.text('Build your own cheap computer'))
