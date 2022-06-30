from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from .sewer_pipe import *
from .rainfall_pipe import *


# Create your views here.
class Test(View):
    def get(self, request, gubn):
        drain_pipe_data = DrainPipeMonitoringAPI.getJsonData(gubn)
        GU_NAME = drain_pipe_data[0]['GUBN_NAM'] + '구'
        rainfall_data = ListRainfallServiceAPI.get_rainfall_data(GU_NAME)
        
        latest_drain_pipie_data = list(filter(lambda x: x['MEA_YMD'] == drain_pipe_data[0]['MEA_YMD'], drain_pipe_data))
        latest_rainfall_data = list(filter(lambda x: x['RECEIVE_TIME'] == rainfall_data[0]['RECEIVE_TIME'], rainfall_data))
        
        if rainfall_data:
            return JsonResponse({"하수구" : latest_drain_pipie_data, "강우량":latest_rainfall_data})
        else:
            return JsonResponse({"하수구": latest_drain_pipie_data})
    