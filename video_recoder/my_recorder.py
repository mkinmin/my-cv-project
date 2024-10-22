import cv2 as cv
import os

# VideoCapture 객체 생성 (기본 카메라)
cap = cv.VideoCapture(0)

# 녹화 모드 여부를 확인하는 변수
is_recording = False

# VideoWriter 객체를 초기화할 변수
out = None

# 저장할 동영상 파일의 이름과 설정
save_path = './videos/'  # 저장할 경로
if not os.path.exists(save_path):
    os.makedirs(save_path)  # 폴더가 없으면 생성

filename = os.path.join(save_path, 'output.avi')  # 파일 이름
fourcc = cv.VideoWriter_fourcc(*'XVID')  # 코덱 설정
fps = 20.0  # 초당 프레임 수
frame_size = (int(cap.get(3)), int(cap.get(4)))  # 프레임 크기 (카메라 해상도)

# 무한 루프 (카메라 피드 처리)
while True:
    ret, frame = cap.read()  # 카메라로부터 프레임을 읽기
    if not ret:
        print("카메라로부터 영상을 가져올 수 없습니다.")
        break

    # 녹화를 위한 원본 프레임을 복사하여 저장용으로 사용
    frame_to_save = frame.copy()

    # 현재 모드에 따라 표시할 UI 결정
    if is_recording:
        # Recording 모드인 경우 빨간 원을 화면에 표시
        cv.circle(frame, (50, 50), 8, (0, 0, 255), -1)  # 1/5 크기로 조정된 빨간 원

        # VideoWriter 객체가 초기화되지 않았다면 초기화
        if out is None:
            out = cv.VideoWriter(filename, fourcc, fps, frame_size)

        # 복사한 프레임을 저장 (빨간 원이 없는 상태로 저장)
        out.write(frame_to_save)

    # 화면에 현재 프레임을 보여줌 (빨간 원 포함)
    cv.imshow('Camera', frame)

    # 키 입력 대기 (1ms 동안)
    key = cv.waitKey(1) & 0xFF

    if key == 27:  # ESC 키를 누르면 종료
        break
    elif key == 32:  # 스페이스바를 누르면 모드 전환
        is_recording = not is_recording
        if is_recording:
            print("녹화 시작")
        else:
            print("녹화 중지")

# 자원 해제 및 창 닫기
cap.release()
if out is not None:
    out.release()
cv.destroyAllWindows()

print(f"녹화된 영상은 {filename}에 저장되었습니다.")
