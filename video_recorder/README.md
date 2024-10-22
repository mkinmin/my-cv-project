# Opencv를 이용한 Video Capture
OpenCV를 이용하여 컴퓨터의 웹캠이나 카메라 영상을 녹화하는 Video Recorder 제작

## 프로젝트 소개
 'OpenCV의 Captured'와 'Writer'를 활용하여 구현하였습니다.

## 프로젝트 설명
원하는 필터를 적용하여 카메라 영상을 녹화하는 Video Recorder
#### Code 실행 후 녹화할 카메라 선택
1. 로컬 카메라 (로컬PC와 연결된 카메라)
2. IP 카메라 (천안시 교통 CCTV의 'CCTV001'번 카메라 활용)
    - CCTV 설치 위치: 충청남도 천안시 서북구 신당동 482-22

#### 'Space' 키를 눌러 '녹화시작 및 녹화종료
#### 1~6번을 눌러 원하는 필터 적용
1. Original
2. GrayScale filter
3. Gaussian Blur filter
4. Canny Edge detector filter
5. Sepia tone filter
6. Mirror effect filter
    
#### 'ESC'를 누를 경우 녹화 화면 종료

### 프로젝트 기간
> 2024.10.16 ~ 2024.10.22

### 개발환경
> `Python 3.9`

`opencv-python==4.10.0.84`

`numpy==2.0.2`

### Repository 구성
- `opencv_recorder.ipynb` : main code
- `requirements.txt` : 모든 패키지 .txt 파일에 포함
- `videos/output.avi` : 녹화된 영상이 저장

### 필요 패키지 설치
다음 명령을 실행하면 모든 패키지를 한 번에 설치
    
    pip install -r requirements.txt

