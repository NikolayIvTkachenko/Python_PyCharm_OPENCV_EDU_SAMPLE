import cv2 as cv

img = cv.imread('PhotoEdu/ElonMusk.jpg')
cv.imshow('Musk ', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#blur
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#Edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny blur', canny)

#Dilating the image
dilated = cv.dilate(canny, (3, 3), iterations=1)
cv.imshow('dilated', dilated)

cv.waitKey(0)