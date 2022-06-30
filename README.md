# Detecting-danger-at-the-construction-sites-using-YOLO-network
Detecting danger at the construction sites using YOLO network 
<br>
-목차- <br> 
 1. 아이디어 선정 <br>
 2. 프로젝트 주제 선정 배경 <br>
 3. 프로젝트 목표 <br>
 4. 차별화 전략 <br>
 5. 채택 알고리즘 (yolo v3) <br>
 6. 과정 및 수행 <br>
 7. 상세 설계 <br>
 8. 전체 시스템 구성 <br>
 9. 시연 영상 <br>
 10. 문제점 및 어려웠던 점 <br>
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


