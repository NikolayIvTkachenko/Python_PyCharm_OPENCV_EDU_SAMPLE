import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('PhotoEdu/ElonMusk.jpg')
cv.imshow('Elon Musk', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))



cv.waitKey(0)








cv.waitKey(0)