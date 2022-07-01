

<div align="center">

  # 과제 01 - LabQ




## 목차
- [F팀 멤버 소개](#-team-f-member)  
- [개발 기간](#--개발-기간--)  
- [프로젝트 설명 분석](#-프로젝트-설명--분석)
- [프로젝트 개발 조건](#-개발-조건)  
- [프로젝트 요구 조건](#-요구-조건)    
- [구현 기능](#구현-기능)  
- [실행방법](#-실행방법)
- [배포](#-배포)
- [API 명세서](#api-명세서)  
- [Test cases code](#테스트-케이스)  
- [기술 스택](#사용된-기술-스택)  

<div align="left">  


## 👨‍👨‍👦‍👦 Team "F" member  

|이승민|임혁|전재완|정용수|
|:------:|:------:|:------:|:------:|
|[Github](https://github.com/SMin1620) | [Github](https://github.com/Cat-Nile) | [Github](https://github.com/iamjaewhan) | [Github](https://github.com/blueknarr) |

  <br>



| <img height="200" width="380" src="https://retaintechnologies.com/wp-content/uploads/2020/04/Project-Management-Mantenimiento-1.jpg"> | <img height="200" width="330" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGElLjafMUhHglmqwh9lRh_sVzOCQyBiPNfQ&usqp=CAU"> |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| 💻 [**Team work**](https://www.notion.so/c7edd2a8004a4fc894f04b939db39861) | 📒 [**Project page**](https://www.notion.so/Team-F-3f553f413ee14b389da0641d8bb4d99e) |
|        공지사항, 컨벤션 공유 등<br> 우리 팀을 위한 룰        | 요구사항 분석, 정보 공유 및<br> 원할한 프로젝트를 위해 사용  |

  </div> 

  <h2> ⌛ 개발 기간  </h2> 
  2022/06/29  ~ 2022/07/01 

  </div> 


# 💻 Project
  ### 💭 프로젝트 설명 & 분석
  - Open API 방식의 공공데이터를 수집, 가공하여 전달하는 REST API와 이를 요청하는 클라이언트 개발

<details>
  <summary>어떤 정보를 조회 할 수 있는가?</summary>
<div markdown="1">


- 서울시 하수관로 수위 현황
  
  - 요청 인자
    
    - TYPE : 요청하는 데이터의 타입으로, JSON 타입 데이터를 요청한다.
    - START_INDEX / END_INDEX : 데이터 행의 시작과 끝 번호이다.
    - GUBN : 조회하고자 하는 지역명 코드이다.
- 서울시 강우량 정보
  
  - 요청인자
  
    - TYPE : 요청하는 데이터의 타입으로, JSON 타입 데이터를 요청한다.
    - START_INDEX / END_INDEX : 데이터 행의 시작과 끝 번호이다.
    - GU_NAME : 조회하고자 하는 지역명이다.

</div>
</details>


  ### 🚥 개발 조건 

  #### 🙆‍♂️ 필수사항  
    - Python, Django  
    - REST API 구현
    - Docstring
    - 데이터는 JSON으로 전달
  #### 🔥 선택사항
    - Docker  
    - Unit test codes  
    - REST API Documentation (Swagger UI)  



### 💫 구현 기능

<details>
  <summary>REST API V1</summary>
<div markdown="1">

  - 필수  

    - 구분 코드(GUBN)로 하수관로 함께 서울시 하수관로 수위 현황과 강우량 정보를 결합하여 데이터를 JSON으로 보낸다.

- 서버


    - 구분 코드(GUBN)에 맞는 서울시 하수관로 수위 현황 및 강우량 정보를 결합하여 client에게 필터링한 데이터를 JSON 형식으로 반환한다.
    
    - ```text
        #request URI : /api/rainfall-drain/?gubn=1
        #response 
        { 
        'REQUEST_TIME': '2022-06-30 11:53:02.0',  (datetime.datetime.now())
        'GUBN':1
        'GU_NAME': '종로구',
        'RAINFALL_DATA': {
            'DATA_NUM' : 2,
        	'ROW' :[
        			{'GU_CODE': 110.0,
        			 'RAINFALL10': '0',
        			 'RAINGAUGE_CODE': 1002.0,
        			 'RAINGAUGE_NAME': '부암동',
        			 'RECEIVE_TIME': '2022-06-30 11:49'},
                      ...
        			]
             },
         'DRAINPIPE_DATA': {
                'DATA_NUM' :4,
        		'ROW' :[
        				{'GUBN': '01',
        				'IDN': '01-0001',
        				'MEA_WAL': 0.63,
        				'MEA_YMD': '2022-06-30 11:53:02.0',
        				'SIG_STA': '통신양호'},
        				...
        				]
        		}
        }
        ```


​        

- 클라이언트


    - 구분 코드(GUBN)와 함께 API를 호출한다.
    - request method : GET
    - URL : domain/api/rainfall-drain
    - Query String(key = value)
        - gubn=int : 조회할 구의 구분 코드를 입력한다. 입력 값은 정수로 유효 값은 1부터 25이다.


​    

## 실행 방법

```
📌 Dependency

# 로컬에서 바로 서버 구동
pip install -r requirements.txt
python manage.py runserver

# 도커 실행
pip install docker
pip install docker-compose
docker-compose up -d
```



## 🔥 배포

docker를 이용해 프로젝트 api를 컨테이너화 하여 GCP에 배포했습니다  

[API Link](http://34.64.83.224:8000/api/rainfall-drop/?gubn=1)



## API 명세서  

[API 명세서 (Swagger)](http://34.64.83.224:8000/swagger/)



## 테스트 케이스

Pytest-Django로 구현 된 28개의 테스트 구현

- 성공 케이스: 25개 (통과)
- 실패 케이스: 3개 (통과)



## 사용된 기술 스택

> - Back-End :  <img src="https://img.shields.io/badge/Python 3.10-3776AB?style=flat&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 4.0.4-092E20?style=flat&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django-DRF 3.13.1-009287?style=flat&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Docker 20.10.14-2496ED?style=flat&logo=docker&logoColor=white"/>
>
> - ETC　　　:  <img src="https://img.shields.io/badge/Git-F05032?style=flat-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=flat-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Swagger-FF6C37?style=flat-badge&logo=Swagger&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white"/>
