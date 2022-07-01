from . import api_settings
import requests, json
import datetime


class  DrainPipeMonitoringAPI:
    SERVICE = 'DrainpipeMonitoringInfo'
    START_INDEX = 1
    END_INDEX = 1000

    def get_drain_pipe_data(GUBN=None):
        '''
        author: 전재완
        co-author: 정용수
        param: String
        return: List
        설명: 구분코드를 입력받아 서울시 공공데이터 api를 이용해 하수도관 수위 현황 데이터를 받음
        '''
        try:
            now_datetime = datetime.datetime.now()
            before_datetime = (now_datetime - datetime.timedelta(minutes=20)).strftime('%Y%m%d%H')
            now_datetime = now_datetime.strftime('%Y%m%d%H')

            url = api_settings.URL + '/{}/{}/{}/{}/{}/{}/{}/{}'.format(
                api_settings.KEY,
                api_settings.TYPE,
                DrainPipeMonitoringAPI.SERVICE,
                DrainPipeMonitoringAPI.START_INDEX,
                DrainPipeMonitoringAPI.END_INDEX,
                GUBN.zfill(2),
                before_datetime,
                now_datetime
                )

            res = requests.get(url)
            data = json.loads(res.text)
            return list(data['DrainpipeMonitoringInfo']['row'][::-1])
        except KeyError:
            raise Exception()