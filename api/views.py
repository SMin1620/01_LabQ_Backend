from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .sewer_pipe import *
from .rainfall_pipe import *
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from api.serializers import GubnSerializer


# Create your views here.
class Test(APIView):
    def get(self, request, gubn):
        drain_pipe_data = DrainPipeMonitoringAPI.get_drainpipe_data(gubn)
        GU_NAME = drain_pipe_data[0]['GUBN_NAM'] + '구'
        rainfall_data = ListRainfallServiceAPI.get_rainfall_data(GU_NAME)

        latest_drain_pipe_data = []
        for row_num in range(len(drain_pipe_data)-1):
            if latest_drain_pipe_data:
                if latest_drain_pipe_data[0]['MEA_YMD'] < drain_pipe_data[row_num]['MEA_YMD']:
                    latest_drain_pipe_data = [drain_pipe_data[row_num]]
                elif latest_drain_pipe_data[0]['MEA_YMD'] == drain_pipe_data[row_num]['MEA_YMD']:
                    latest_drain_pipe_data.append(drain_pipe_data[row_num])
            else:
                latest_drain_pipe_data.append(drain_pipe_data[row_num])
                
        latest_rainfall_data = []
        for data in rainfall_data:
            if rainfall_data[0]['RECEIVE_TIME'] == data['RECEIVE_TIME']:
                latest_rainfall_data.append(data)
    
        return JsonResponse({"drain_info": latest_drain_pipe_data, "rainfall_info" : latest_rainfall_data})


class RainfallDrainAPI(APIView):
    @swagger_auto_schema(query_serializer=GubnSerializer)
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
            return JsonResponse({'status_code' : 400, 'detail' : '잘못된 요청입니다,'}, status=400)
        except IndexError:
            return JsonResponse({'status_code' : 500, 'detail' : '서버에 에러 발생'}, status=500)
        except Exception:
            return JsonResponse({'status_code' : 400, 'detail' : '잘못된 요청입니다,'}, status=400)

