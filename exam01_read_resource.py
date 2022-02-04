import cv2

# img = cv2.imread('./resources/lena.png')
#
# cv2.imshow('Lena Soderberg', img)  # 문자열은 창 제목
# cv2.waitKey(0)  # 0을 주면 무한대기

# cap = cv2.VideoCapture('./resources/test_video.mp4')
# while cv2.waitKey(1) != ord('q'):
#     sucess, img = cap.read()
#     img = cv2.resize(img, (640, 480))
#     cv2.imshow('test video', img)
#     # if cv2.waitKey(1) & 0xFF == ord('q'):
#     #     break

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
while cv2.waitKey(1) != ord('q'):
    sucess, img = cap.read()
    cv2.imshow('test video', img)