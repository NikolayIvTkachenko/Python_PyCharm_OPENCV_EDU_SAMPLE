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

#Erofing
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('eroded ', eroded )

#resize
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('resize ', resize)

#cropped
cropped = img[50:200, 200:400]
cv.imshow('Croped',cropped )

cv.waitKey(0)