import cv2
import numpy as np

img = np.ones((512, 512, 3), np.uint8) * 255  # 하얀바탕으로 하고 싶으면 *255

cv2.line(img, (0, 0), (512, 512), (0, 255, 0), 3)  # 선
cv2.rectangle(img, (10, 10), (250, 350), (50, 50, 255), 2)  # 사각형
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)  # 원
cv2.ellipse(img, ((150, 150), (200, 100), 0), (200, 50, 50), 2)  # 타원
cv2.putText(img, 'OPENCV', (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 200, 200), 3)  # 텍스트




cv2.imshow('Image', img)
cv2.waitKey(0)