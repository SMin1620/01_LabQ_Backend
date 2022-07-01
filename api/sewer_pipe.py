from .api_settings import DrainPipeMonitoringAPISetting

import requests, json
import datetime



class  DrainPipeMonitoringAPI:
    KEY = DrainPipeMonitoringAPISetting.KEY
    SERVICE = DrainPipeMonitoringAPISetting.SERVICE
    TYPE = DrainPipeMonitoringAPISetting.TYPE
    URL = DrainPipeMonitoringAPISetting.URL
    START_INDEX = DrainPipeMonitoringAPISetting.START_INDEX
    END_INDEX = DrainPipeMonitoringAPISetting.END_INDEX

    def get_drainpipe_data(GUBN=None):
        now_datetime = datetime.datetime.now()
        before_datetime = (now_datetime - datetime.timedelta(minutes=10)).strftime('%Y%m%d%H')
        now_datetime = now_datetime.strftime('%Y%m%d%H')
        
        url = DrainPipeMonitoringAPI.URL.format(
            DrainPipeMonitoringAPI.KEY,
            DrainPipeMonitoringAPI.TYPE,
            DrainPipeMonitoringAPI.SERVICE,
            DrainPipeMonitoringAPI.START_INDEX,
            DrainPipeMonitoringAPI.END_INDEX,
            str(GUBN).zfill(2),
            before_datetime,
            now_datetime
            )
        
        res = requests.get(url)
        data = json.loads(res.text)
        return list(data['DrainpipeMonitoringInfo']['row'][::-1])
    def get_drain_pipe_data(GUBN=None):
        try:
            now_datetime = datetime.datetime.now()
            before_datetime = (now_datetime - datetime.timedelta(minutes=20)).strftime('%Y%m%d%H')
            now_datetime = now_datetime.strftime('%Y%m%d%H')

            url = DrainPipeMonitoringAPI.URL.format(
                DrainPipeMonitoringAPI.KEY,
                DrainPipeMonitoringAPI.TYPE,
                DrainPipeMonitoringAPI.SERVICE,
                DrainPipeMonitoringAPI.START_INDEX,
                DrainPipeMonitoringAPI.END_INDEX,
                str(GUBN).zfill(2),
                before_datetime,
                now_datetime
                )

            res = requests.get(url)
            data = json.loads(res.text)
            return list(data['DrainpipeMonitoringInfo']['row'][::-1])
        except KeyError:
            raise Exception()
