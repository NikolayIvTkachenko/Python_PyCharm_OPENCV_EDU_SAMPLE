import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('PhotoEdu/ElonMusk.jpg')
cv.imshow('Elon Musk', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')


cv.waitKey(0)