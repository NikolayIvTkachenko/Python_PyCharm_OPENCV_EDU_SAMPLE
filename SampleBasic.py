import cv2 as cv

img = cv.imread('PhotoEdu/ElonMusk.jpg')
cv.imshow('Musk ', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
cv.waitKey(0)