from . import api_settings
import requests, json
import datetime



class  DrainPipeMonitoringAPI:
    SERVICE = 'DrainpipeMonitoringInfo'
    START_INDEX = 1
    END_INDEX = 1000
    
    def get_drain_pipe_data(GUBN=None):
        try:
            now_datetime = datetime.datetime.now()
            before_datetime = (now_datetime - datetime.timedelta(minutes=20)).strftime('%Y%m%d%H')
            now_datetime = now_datetime.strftime('%Y%m%d%H')

            url = URL + '/{}/{}/{}/{}/{}/{}/{}/{}'.format(
                KEY,
                TYPE,
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