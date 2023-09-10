from enum import Enum


class ErrorMessages(Enum):
    statusCodeError = "Wrong Status Code"
    cityNameError = "Wrong City Name"
    forecastDaysWrongNumberError = "Wrong number of days"
