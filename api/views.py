from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from .sewer_pipe import *
from .rainfall_pipe import *


# Create your views here.
class RainfallDrainAPI(View):
    def get(self, request):
        try:
            GUBN = request.GET['gubn']
            drain_pipe_data = DrainPipeMonitoringAPI.get_drain_pipe_data(GUBN)
            GU_NAME = drain_pipe_data[0]['GUBN_NAM'] + '구'
            rainfall_data = ListRainfallServiceAPI.get_rainfall_data(GU_NAME)

            latest_drain_pipe_data = list(filter(lambda x: x['MEA_YMD'] == drain_pipe_data[0]['MEA_YMD'], drain_pipe_data))
            latest_rainfall_data = list(filter(lambda x: x['RECEIVE_TIME'] == rainfall_data[0]['RECEIVE_TIME'], rainfall_data))

            res = {
                'REQUEST_TIME': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'GUBN': GUBN,
                'GU_NAME': GU_NAME,
                'RAINFALL_DATA': {
                    'DATA_NUM': len(latest_rainfall_data),
                    'ROW': latest_rainfall_data
                },
                'DRAINPIPE_DATA': {
                    'DATA_NUM': len(latest_drain_pipe_data),
                    'ROW': latest_drain_pipe_data
                }
            }
            return JsonResponse(res)
        
        except KeyError:
            return JsonResponse({'status_code' : 404, 'detail' : '잘못된 요청입니다,'}, status=404)
        except Exception:
            return JsonResponse({'status_code' : 404, 'detail' : '잘못된 요청입니다,'}, status=404)
