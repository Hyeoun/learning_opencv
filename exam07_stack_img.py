import cv2
import numpy as np

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    rowAvailable = isinstance(imgArray[0], list)
    if rowAvailable:
        for x in range(rows):
            for y in range(cols):
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_BGR2RGB)
                imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
    hor = []
    for x in range(rows):
        hor.append(np.hstack(imgArray[x]))
    ver = np.vstack(hor)
    return ver

img = cv2.imread('./resources/lena.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgColor = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR)

imgStack = stackImages(0.5, [[img, imgGray, img], [imgGray, img, imgGray]])  # 흑백 컬러 번갈아가면서 이미지를 출력하는 함수를 생성한다.

cv2.imshow('Image STack', imgStack)
cv2.waitKey(0)