import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
#cv.imshow('Blank', blank)

#img = cv.imread('PhotoEdu/ElonMusk.jpg')
#cv.imshow('Elon Musk', img)

#1 Paint the image
#blank[:] = 0,255,0
#cv.imshow('Green', blank)

#blank[200:300, 300:400] = 0,0,255
#cv.imshow('Green', blank)

#2 Draw rectangle
#cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), thickness=cv.FILLED)
#cv.imshow('Rectangle', blank)

#3 Draw circle
cv.circle(blank, (150, 150), 40, (255, 255,0), thickness=3)
#cv.imshow('Circle', blank)


#4 Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=1)
cv.imshow('Line', blank)
cv.waitKey(0)