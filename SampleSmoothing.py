import cv2 as cv
import numpy as np

img = cv.imread('PhotoEdu/ElonMusk.jpg')
cv.imshow('Elon Musk', img)

#Average
average = cv.blur(img, (7, 7))
cv.imshow('Average Blur', average)

#Gaussion Blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('gauss Blur', gauss)

#Median Blur
medianBlur = cv.medianBlur(img, 3)
cv.imshow('medianBlur', medianBlur)

#Bilateral
bilateral= cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)