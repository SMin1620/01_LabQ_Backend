from django.shortcuts import render
from django.http import JsonResponse

from .sewer_pipe import *



# Create your views here.


def test(request, gubn):
    drain_pipe_data = DrainPipeMonitoringAPI.getJsonData(gubn)
    GU_NAME = drain_pipe_data[0]['GUBN_NAM'] + '구'
    return JsonResponse({"하수구" : drain_pipe_data})