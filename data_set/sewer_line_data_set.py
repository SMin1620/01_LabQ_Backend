import requests
from bs4 import BeautifulSoup as bs
import os, json, datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()



"""
이승민
서울시 하수관로 수위 현황

pip install requests
pip install bs4

param : KEY, TYPE, SERVICE, START_INDEX, END_INDEX, GUBN, MEA_YMD, MEA_YMD2
"""


""" param """
######### json type ##########
KEY = '5557686370736b653738776e4b564f'
TYPE = 'json'
SERVICE = 'DrainpipeMonitoringInfo'
START_INDEX = 1
END_INDEX = 100
GUBN = 1
MEA_YMD = 2022062820
MEA_YMD2 = 2022062920


"""parsing"""
for _ in range(2):
    url = f'http://openapi.seoul.go.kr:8088/{KEY}/{TYPE}/{SERVICE}/{START_INDEX}/{END_INDEX}/0{GUBN}/{MEA_YMD}/{MEA_YMD2}'
    res = requests.get(url).json()
    sewer_list = res['DrainpipeMonitoringInfo']['row']

    for data in sewer_list:
        ## database create
        # SewerLine.objects.create(
        #     idn=data['IDN'],
        #     gubn=data['GUBN'],
        #     gubn_nam=data['GUBN_NAM'],
        #     mea_ymd=data['MEA_YMD'],
        #     mea_wal=data['MEA_WAL'],
        #     sig_sta=data['SIG_STA']
        # )
        res = {
            'gubn_nam': data['GUBN_NAM'],
            'mea_ymd': data['MEA_YMD']
        }
        print(res)

    # START_INDEX = END_INDEX + 1
    # END_INDEX += 100



