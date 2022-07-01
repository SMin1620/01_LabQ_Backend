from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from .sewer_pipe import *
from .rainfall_pipe import *
from rest_framework.views import APIView


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