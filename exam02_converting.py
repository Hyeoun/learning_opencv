import cv2
import numpy as np

img = cv2.imread('./resources/lena.png')

kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 이미지를 흑백으로 보여준다.
imgBlur = cv2.GaussianBlur(img, (1, 1), 0)  # 이미지를 블러처리한다.
imgCanny = cv2.Canny(img, 150, 200)  # 외곽선을 찾는 알고리즘
imgDialtion = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialtion, kernel, iterations=1)

cv2.imshow('Origin image', img)
cv2.imshow('Gray image', imgGray)
cv2.imshow('Blur image', imgBlur)
cv2.imshow('Canny image', imgCanny)
cv2.imshow('Dialation image', imgDialtion)
cv2.imshow('Eroded image', imgEroded)

cv2.waitKey(0)