import requests
from resources.varaibles import BASE_URL, params
from resources.errorMessages import ErrorMessages


def test_get_forecast_weather():
    response = requests.get(BASE_URL + "forecast", params=params)
    #print(response.json())
    assert response.status_code == 200, ErrorMessages.statusCodeError.value
    assert response.json()['city']['name'] == "Almaty", ErrorMessages.cityNameError.value
    #do i need check the date?
    #endppoint for free apikey provides 5 days forecsa each 3 hours thus response cnt = 40 (5 days * 8 times a day)
    assert len(response.json()['list']) == 40, ErrorMessages.forecastDaysWrongNumberError.value


