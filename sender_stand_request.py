import configuration
import requests

#запрос на создание заказа
def post_new_order(body):
    return requests.post(url=configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                        json=body)

#запрос на получение заказа по треку заказа
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_TRACK_PATH + str(track))