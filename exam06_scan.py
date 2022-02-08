import cv2
import numpy as np

img = cv2.imread('./resources/cards.jpg')

pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 444]])
width, height = 250, 350
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])  # 좌상 우상 좌하 우하

matrix = cv2.getPerspectiveTransform(pts1, pts2)  # 이미지 변환
imgOutput = cv2.warpPerspective(img, matrix, (width, height))  # 이미지 출력

cv2.imshow('Image', img)
cv2.imshow('Output', imgOutput)
cv2.waitKey(0)