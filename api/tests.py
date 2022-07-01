from rest_framework.test import APIClient, APITestCase


# Create your tests here.
class SewerLineTest(APITestCase):

    """
    author : 이승민
    co_author : 임혁
    param :
        - IDN : String
        - GUBN : Int
        - GUBN_NAM : String
        - MEA_YMD : YYYYMMDDHH24
        - MEA_WAL : Float
        - SIG_STA : String

    return :
        - GUBN
        - status_code(200 or 400)

    explanation :
        테스트 케이스 명세서

        1. 케이스 설정 방법
            1) success test case
                - 성공 응답 코드
            2) error test case
                - 에러 응답 코드

        2. 케이스 종류
            1) 필수 요소 1개 (구분 코드 GUBN)
                - 구분 코드(GUBN)
                - Success Test Case 25개
                - Error Test Case 3개

        3. 테스트 케이스
            - 성공 테스트 케이스
                필수 요소 : GUBN
                Success Test Case : 25개
                method : GET
                param : gubn

            - 실패 테스트 케이스
                필수 요소 : GUBN
                Fail Test Case : 3개
                method : GET
                param : gubn
                content : (1) gubn이 포함되어 있지 않은 경우. (/api/rainfall-drain/)
                          (2) gubn 범위를 벗어난 경우 (gubn == 0)
                          (2) gubn 범위가 벗어난 경우 (gubn == 26 ~ )
    """

    client = APIClient
    headers = {}

    def setUp(self):
        sewer1 = {
            'gubn': 1,
            'gubn_nam': '종로구',
        }
        self.sewer1 = sewer1

        sewer2 = {
            'gubn': 2,
            'gubn_nam': '중구',
        }
        self.sewer2 = sewer2

        sewer3 = {
            'gubn': 3,
            'gubn_nam': '용산구',
        }
        self.sewer3 = sewer3

        sewer4 = {
            'gubn': 4,
            'gubn_nam': '성동구',
        }
        self.sewer4 = sewer4

        sewer5 = {
            'gubn': 5,
            'gubn_nam': '광진구',
        }
        self.sewer5 = sewer5

        sewer6 = {
            'gubn': 6,
            'gubn_nam': '동대문구',
        }
        self.sewer6 = sewer6

        sewer7 = {
            'gubn': 7,
            'gubn_nam': '중랑구',
        }
        self.sewer7 = sewer7

        sewer8 = {
            'gubn': 8,
            'gubn_nam': '성북구',
        }
        self.sewer8 = sewer8

        sewer9 = {
            'gubn': 9,
            'gubn_nam': '강북구',
        }
        self.sewer9 = sewer9

        sewer10 = {
            'gubn': 10,
            'gubn_nam': '도봉구',
        }
        self.sewer10 = sewer10

        sewer11 = {
            'gubn': 11,
            'gubn_nam': '노원구',
        }
        self.sewer11 = sewer11

        sewer12 = {
            'gubn': 12,
            'gubn_nam': '은평구',
        }
        self.sewer12 = sewer12

        sewer13 = {
            'gubn': 13,
            'gubn_nam': '서대문구',
        }
        self.sewer13 = sewer13

        sewer14 = {
            'gubn': 14,
            'gubn_nam': '마포구',
        }
        self.sewer14 = sewer14

        sewer15 = {
            'gubn': 15,
            'gubn_nam': '양천구',
        }
        self.sewer15 = sewer15

        sewer16 = {
            'gubn': 16,
            'gubn_nam': '강서구',
        }
        self.sewer16 = sewer16

        sewer17 = {
            'gubn': 17,
            'gubn_nam': '구로구',
        }
        self.sewer17 = sewer17

        sewer18 = {
            'gubn': 18,
            'gubn_nam': '금천구',
        }
        self.sewer18 = sewer18

        sewer19 = {
            'gubn': 19,
            'gubn_nam': '영등포구',
        }
        self.sewer19 = sewer19

        sewer20 = {
            'gubn': 20,
            'gubn_nam': '동작구',
        }
        self.sewer20 = sewer20

        sewer21 = {
            'gubn': 21,
            'gubn_nam': '관악구',
        }
        self.sewer21 = sewer21

        sewer22 = {
            'gubn': 22,
            'gubn_nam': '서초구',
        }
        self.sewer22 = sewer22

        sewer23 = {
            'gubn': 23,
            'gubn_nam': '강남구',
        }
        self.sewer23 = sewer23

        sewer24 = {
            'gubn': 24,
            'gubn_nam': '송파구',
        }
        self.sewer24 = sewer24

        sewer25 = {
            'gubn': 25,
            'gubn_nam': '강동구',
        }
        self.sewer25 = sewer25

    """
    필수 요소 : GUBN
    Success Test Case : 25개
    method : GET
    param : gubn
    """

    def test_necessary_success01(self):
        response = self.client.get('/api/rainfall-drain/?gubn=01', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer1['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer1['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success02(self):
        response = self.client.get('/api/rainfall-drain/?gubn=02', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer2['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer2['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success03(self):
        response = self.client.get('/api/rainfall-drain/?gubn=03', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer3['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer3['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success04(self):
        response = self.client.get('/api/rainfall-drain/?gubn=04', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer4['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer4['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success05(self):
        response = self.client.get('/api/rainfall-drain/?gubn=05', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer5['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer5['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success06(self):
        response = self.client.get('/api/rainfall-drain/?gubn=06', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer6['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer6['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success07(self):
        response = self.client.get('/api/rainfall-drain/?gubn=07', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer7['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer7['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success08(self):
        response = self.client.get('/api/rainfall-drain/?gubn=08', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer8['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer8['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success09(self):
        response = self.client.get('/api/rainfall-drain/?gubn=09', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer9['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer9['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success010(self):
        response = self.client.get('/api/rainfall-drain/?gubn=10', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer10['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer10['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success011(self):
        response = self.client.get('/api/rainfall-drain/?gubn=11', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer11['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer11['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success012(self):
        response = self.client.get('/api/rainfall-drain/?gubn=12', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer12['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer12['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success013(self):
        response = self.client.get('/api/rainfall-drain/?gubn=13', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer13['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer13['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success014(self):
        response = self.client.get('/api/rainfall-drain/?gubn=14', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer14['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer14['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success015(self):
        response = self.client.get('/api/rainfall-drain/?gubn=15', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer15['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer15['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success016(self):
        response = self.client.get('/api/rainfall-drain/?gubn=16', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer16['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer16['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success017(self):
        response = self.client.get('/api/rainfall-drain/?gubn=17', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer17['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer17['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success018(self):
        response = self.client.get('/api/rainfall-drain/?gubn=18', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer18['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer18['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success019(self):
        response = self.client.get('/api/rainfall-drain/?gubn=19', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer19['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer19['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success020(self):
        response = self.client.get('/api/rainfall-drain/?gubn=20', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer20['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer20['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success021(self):
        response = self.client.get('/api/rainfall-drain/?gubn=21', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer21['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer21['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success022(self):
        response = self.client.get('/api/rainfall-drain/?gubn=22', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer22['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer22['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success023(self):
        response = self.client.get('/api/rainfall-drain/?gubn=23', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer23['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer23['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success024(self):
        response = self.client.get('/api/rainfall-drain/?gubn=24', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer24['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer24['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    def test_necessary_success025(self):
        response = self.client.get('/api/rainfall-drain/?gubn=25', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        """ GUBN 일치 테스트 """
        self.assertEqual(int(data['GUBN']), self.sewer25['gubn'])
        """ GU_NAME 일치 테스트"""
        self.assertEqual(data['GU_NAME'], self.sewer25['gubn_nam'])
        """ 응답 코드 일치 테스트 """
        self.assertEqual(response.status_code, 200)

    """
    필수 요소 : GUBN
    Fail Test Case : 3개
    method : GET
    param : gubn
    content : (1) gubn이 포함되어 있지 않은 경우. (/api/rainfall-drain/)
              (2) gubn 범위를 벗어난 경우 (gubn == 0)
              (2) gubn 범위가 벗어난 경우 (gubn == 26 ~ )
    """

    def test_necessary_fail01(self):
        response = self.client.get('/api/rainfall-drain/?gubn=26', content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_necessary_fail02(self):
        response = self.client.get('/api/rainfall-drain/?gubn=00', content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_necessary_fail03(self):
        response = self.client.get('/api/rainfall-drain/', content_type='application/json')
        self.assertEqual(response.status_code, 400)














