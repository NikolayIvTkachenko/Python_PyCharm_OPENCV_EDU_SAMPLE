import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('PhotoEdu/ElonMusk.jpg')
cv.imshow('Elon Musk', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

haar_cascade = cv.CascadeClassifier('haar/haarcascade_profileface.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces = {len(faces_rect)}')

cv.waitKey(0)