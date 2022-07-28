import requests
from .api_settings import DrainPipeMonitoringAPISetting


class ListRainfallServiceAPI:
    KEY = DrainPipeMonitoringAPISetting.KEY

    def get_rainfall_data(GU_NAME=None):
        try:
            url = f"http://openapi.seoul.go.kr:8088/{ListRainfallServiceAPI.KEY}/json/ListRainfallService/1/20/{GU_NAME}"
            data = requests.get(url).json()
            return list(data['ListRainfallService']['row'])
        except KeyError:
            raise  Exception()