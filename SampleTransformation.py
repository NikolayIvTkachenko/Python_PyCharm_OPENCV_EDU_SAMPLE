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

#Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated01 = rotate(img, 45)
cv.imshow('rotated01', rotated01)

cv.waitKey(0)