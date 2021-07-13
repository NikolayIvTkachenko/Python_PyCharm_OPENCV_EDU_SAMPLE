import cv2 as cv
import numpy as np

img = cv.imread('PhotoEdu/ElonMusk.jpg')
cv.imshow('Elon', img)

def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -x => Left
# -y => Up
# x => Right
# y => Dawn

translate = translate(img, 100, 100)
cv.imshow('translate', translate)

cv.waitKey(0)