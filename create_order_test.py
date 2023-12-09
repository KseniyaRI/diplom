# Ксения Рябухина, 11-я когорта - Финальный проект. Инженер по тестированию плюс

import requests

from configuration import URL_SERVICE, CREATE_ORDER_PATH, \
    GET_ORDER_BY_TRACK_PATH
from data import CREATE_ORDER_BODY


def create_order():
    # функция для создания нового заказа
    response = requests.post(
        url=URL_SERVICE + CREATE_ORDER_PATH,
        json=CREATE_ORDER_BODY
    )
    return response.json()


def test_order_created():
    # функция для проверки создания заказа по треку
    track = create_order()['track']
    new_url = f'{URL_SERVICE}{GET_ORDER_BY_TRACK_PATH}?t={track}'
    response_status = requests.get(
        url=new_url,
    ).status_code

    assert response_status == 200
