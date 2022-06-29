import requests
from bs4 import BeautifulSoup as bs
import os


"""config.settings -> config == project name"""
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LabQ.settings")

import django
django.setup()



"""
이승민
서울시 강우량 정보
pip install requests
pip install bs4

param : KEY, TYPE, SERVICE, START_INDEX, END_INDEX
"""

""" param """
########### xml type ############
KEY = '5557686370736b653738776e4b564f'
TYPE = 'xml'
SERVICE = 'ListRainfallService'
START_INDEX = 1
END_INDEX = 100


"""parsing"""
for _ in range(2):
    url = f"http://openapi.seoul.go.kr:8088/{KEY}/{TYPE}/{SERVICE}/{START_INDEX}/{END_INDEX}"
    res = requests.get(url)
    soup = bs(res.content, 'html.parser')

    for i in soup.find_all('row'):
        ## database create
        # RainFall.objects.create(
        #     raingauge_code=i.raingauge_code.string,
        #     raingauge_name=i.raingauge_name.string,
        #     gu_code=i.gu_code.string,
        #     gu_name=i.gu_name.string,
        #     rainfall10=i.rainfall10.string,
        #     receive_time=i.receive_time.string
        # )
        res = {
            ''
            'gu_name': i.gu_name.string,
            'receive_time': i.receive_time.string
        }

        print(res)
        # START_INDEX = END_INDEX + 1
        # END_INDEX += 100

