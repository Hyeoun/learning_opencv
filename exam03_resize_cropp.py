import cv2

img = cv2.imread('./resources/shapes.png')
print(img.shape)

imgResize = cv2.resize(img, (200, 500))  # 이미지 크기 재정의
imgCropped = img[200:300, 100:300]  # 이미지 자르기

cv2.imshow('Image', img)
cv2.imshow('Image resize', imgResize)
cv2.imshow('Image Cropped', imgCropped)


cv2.waitKey(0)