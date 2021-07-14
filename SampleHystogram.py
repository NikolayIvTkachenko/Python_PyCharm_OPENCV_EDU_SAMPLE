import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('PhotoEdu/ElonMusk.jpg')
cv.imshow('Elon Musk', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#Grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title('Grascale Histogramm')
plt.xlabel('Bins')
plt.ylabel('# of piexels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()



cv.waitKey(0)