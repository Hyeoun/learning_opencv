import cv2

faceCascade = cv2.CascadeClassifier('./resources/haarcascade_frontalface_default.xml')
img = cv2.imread('./resources/02.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)  # 얼굴의 좌표 찾기

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x + w, y + h), (200, 50, 50), 2)  # 얼굴의 좌표를 이용해 사각형 그리기

cv2.imshow('Result', img)
cv2.waitKey(0)
