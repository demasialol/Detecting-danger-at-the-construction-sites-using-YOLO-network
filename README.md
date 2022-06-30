# Detecting-danger-at-the-construction-sites-using-YOLO-network
Detecting danger at the construction sites using YOLO network 
<br>
-목차- <br> 
 1. 아이디어 선정 <br>
 2. 프로젝트 주제 선정 배경 <br>
 3. 프로젝트 목표 <br>
 4. 차별화 전략 <br>
 5. 과정 및 수행 <br>
 6. 상세 설계 <br>
 7. 전체 시스템 구성 <br>
 8. 시연 영상 <br>
 <hr>
 
아이디어 선정 <br><br>
<img src="https://github.com/demasialol/Detecting-danger-at-the-construction-sites-using-YOLO-network/blob/main/slide3.JPG?raw=true" align="center"><br><br>
지난 3월 3일, 광주에 건설중인 신축 아파트 사고 붕괴 사고, 해운대 호텔 공사장 적재물 추락, 서울 서초구 공사 현장서 50대 노동자 추락,부산 오피스텔 공사 현장서 끼임 사망 사고 등등
공사현장에서는 위 같이 다양한 사고가 자주 발생하고 있다. <br><br>
<hr>
프로젝트 주제 선정 배경 <br><br>
<img src="https://github.com/demasialol/Detecting-danger-at-the-construction-sites-using-YOLO-network/blob/main/slide4.JPG?raw=true" align="center"><br><br>
이러한 사고 발생을 사전에 방지 하기위해 상황을 가정하여 
CCTV 나 드론같이 공간에 제약없이 어떠한 방식이던 유동적으로 실시간 현장 영상을 촬영 가능한 기기를 사용하여 현장 영상을 받고 
전달받은 영상을 사물인식을 통해 미착용 안전장비를 판별하고, 적재물을 판별하여 위험이 발생할 수 있는 상황을 사전에 탐지 할 수 있는 알고리즘을 구상하였다
<br><br>
<hr>
프로젝트 목표 <br><br>
<img src="https://github.com/demasialol/Detecting-danger-at-the-construction-sites-using-YOLO-network/blob/main/slide6.JPG?raw=true" align="center"><br><br>
공사현장에서 빈번하게 발생하는 안전사고를 미연에 방지할 수 있도록 안전사고 관제 시스템의 핵심인 위험요소를 판별하는 것을 목표로 하였다. 
정리하자면, CCTV 나 드론을 통해 받은 실시간 영상을 사물인식 알고리즘을 사용하여 저희가 구상한 2가지 위험 케이스들을 기반으로, 현장 노동자들의 위험 상황을 사전 감지해, 사고가 발생하기전에 현장에 위치한 노동자들이나 매니저에게 알려주는 방식이다.
<br><br>
<hr>
차별화 전략 <br><br>
<img src="https://github.com/demasialol/Detecting-danger-at-the-construction-sites-using-YOLO-network/blob/main/slide7.JPG?raw=true" align="center"><br><br>
구상한 프로젝트의 핵심인 판별 요소중 하나인 헬멧, 마스크등의 안전장비 착용 감지 시스템은 
코로나를 겪은 우리들에게 매우 친숙한 시스템중 하나이다
최근 아파트 붕괴 사고로 인해 공사현장을 기반으로한 스마트 안전기술 개발에 한창 관심이 쏠렸는데,
그에 맞물려 발전한 기능들은 주로 ‘원격 점검시스템’, ‘중장비 접근 경고 알람 시스템’, ‘근로자 위치 관제 시스템, ‘환경센서 시스템’ 과 같이 특수한 센서와 장비가 있어야 구현이 가능한 방식의 사고 예방 방식을 채택하고 있다

해당 프로젝트는 비용적인 측면에서 문제가 발생하지 않기 때문에 현장 대입이 훨씬 용의한 방식이다. 

사전에 가정한 상황에 원하는 사물들만 실시간 이미지를 통하여 높은 확률로 판별 할 수 있도록 사물 인식 알고리즘을 구현하는것을 목표로 제작한 프로그램이고 이는 기존에 이미 완성되어 있는 타 사고 예방 시스템과 해당 프로젝트의 가장 큰 차별점이라고 볼 수 있다. 
<br><br>
<hr>
과정 및 수행 <br><br>
<img src="https://github.com/demasialol/Detecting-danger-at-the-construction-sites-using-YOLO-network/blob/main/slide9.JPG?raw=true" align="center"><br><br>
프로젝트의 핵심 목표인 위험 요소 다중 판별을 위해서는 오픈 이미지 데이터는 활용하기 어렵기 때문에
학습용 이미지는 데이터 셋 사이트인 AIhub와 Kaggle라는 데이터셋 클라우드 사이트 에서 제공하는 이미지를 약 2,000장 가량 수집하여 라벨링을 진행하였다.
라벨링 데이터는 라벨링 툴인 YOLO-mark와 LabelImg를 이용하여 직접 라벨링을 한 후 데이터셋을 구축했다.
<br><br>
<hr>
과정 및 수행 <br><br>
<img src="https://github.com/demasialol/Detecting-danger-at-the-construction-sites-using-YOLO-network/blob/main/slide10.JPG?raw=true" align="center"><br><br>
다음으로 darknet 모델을 이용해서 라벨링한 이미지를 학습시키는 방법을 진행했다.
학습 과정에서 학습 데이터 설정에 따른 값 정확도에 큰 차이가 있었다. 
학습과정에서 변경한 설정 값들은 subdivision, angle, maxbatches, steps, 이미지 데이터 양으로 위 값을 조정하여 최적의 학습 모델 (weight)를 도출했다.
<br><br>
<hr>
상세 설계 <br><br>
<img src="https://github.com/demasialol/Detecting-danger-at-the-construction-sites-using-YOLO-network/blob/main/slide11.JPG?raw=true" align="center"><br><br>
위 사진에 차트가 다크넷을 통한 학습을 실시간으로 보여주는 차트다.
학습 횟수 -> 차트에서는 batches 라고 표현하고, 로스->  예측 실패 비율 두가지를 축으로 표현한다. 
학습량이 많아질수록 loss 가 적어지는 것을 확인할 수 있다.
이렇게 다크넷을 통해 수집한 데이터셋 (이미지 데이터) 들을 학습시키면 최종적으로 오른쪽과 같은 yolo v3 weight 를 생성한다. 
<br><br>
<hr>
상세 설계 <br><br>
<img src="https://github.com/demasialol/Detecting-danger-at-the-construction-sites-using-YOLO-network/blob/main/slide12.JPG?raw=true" align="center"><br><br>
추가적으로 영상에서 라인을 찾을 때 주로 사용되는 허프변환 알고리즘을 사용하여 외곽선을 검출한다. 
파이썬에서 지원하는 OpenCv 라이브러리에서 함수로 제공하고 있어 허프변환 함수를 이용하여 적재물의 외곽선을 검출하는데 사용하였다. 
허프변환을 이용하여 검출한 외곽선에서 기울기를 추출하여 표준편차가 크면 적재물이 제대로 적재되어 있지 않다고 판단하면 
경고 로그를 띄우는 형식으로 설계했다.
<br><br>
<hr>
전체 시스템 구성 <br><br>
<img src="https://github.com/demasialol/Detecting-danger-at-the-construction-sites-using-YOLO-network/blob/main/slide13.JPG?raw=true" align="center"><br><br>
해당 프로젝트의 전체 시스템 구성표이다. 

우선 공사현장의 영상을 입력 받는다. 
다음으로 사람을 인식하고 사람을 인식해 존재하는지 확인하면 
두가지 방식을 추가로 판별 한다. 

1. 먼저 헬멧, 베스트 판별. 여기서 헬멧과 조끼가 없는걸로 인식되면 로그 형태로 주의 알림을 띄우기 

2. 사람과 적재물이 같이 판별된 상태라면 일단 로그 형태로 주의 알림을 띄우고 
추가적으로 edge detection을 통해 적재물의 적재 상태(적재 퀄리티)를 좀더 직관적으로 알 수 있게 하는 이미지를 출력한다. 
<br><br>
<hr>
시연 영상 <br><br>
https://youtu.be/rRSA1cg0DXg
