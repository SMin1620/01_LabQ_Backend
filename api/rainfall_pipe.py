import requests
from . import api_settings


class RainfallMonitoringAPI:
    SERVICE = 'ListRainfallService'
    START_INDEX = 1
    END_INDEX = 20

    def get_rainfall_data(GU_NAME=None):
        '''
        author: 정용수
        co-author: 전재완
        param: String
        return: List
        설명: 구청명을 입력받아 서울시 공공데이터 api를 이용해 강우량 데이터를 받음
        '''
        try:
            url = api_settings.URL + '/{}/{}/{}/{}/{}/{}'.format(
                api_settings.KEY,
                api_settings.TYPE,
                RainfallMonitoringAPI.SERVICE,
                RainfallMonitoringAPI.START_INDEX,
                RainfallMonitoringAPI.END_INDEX,
                GU_NAME,
            )
            data = requests.get(url).json()
            return list(data['ListRainfallService']['row'])
        except KeyError:
            raise  Exception()