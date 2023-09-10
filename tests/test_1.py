import requests
from resources.varaibles import BASE_URL, params
from resources.errorMessages import ErrorMessages


def test_get_current_weather():
    response = requests.get(BASE_URL + "weather", params=params)
    # print(response.json())
    assert response.status_code == 200, ErrorMessages.statusCodeError.value
    assert response.json()['name'] == "Almaty", ErrorMessages.cityNameError.value
