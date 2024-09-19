# Светлана Чистякова, 21-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

#сохранить номер трека заказа
def get_new_track_number():
    response = sender_stand_request.post_new_order(data.body)
    track = response.json()["track"]
    return track

#проверить, что код ответа равен 200
def test_get_order_by_track():
    track = get_new_track_number()
    response = sender_stand_request.get_order_by_track(track)
    assert response.status_code == 200