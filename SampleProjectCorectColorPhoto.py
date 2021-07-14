import cv2 as cv
import numpy as np

def empty(a):
    pass


path = 'PhotoEdu/ElonMusk.jpg'
cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars", 640, 240)
cv.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv.createTrackbar("Hue Max", "TrackBars", 19, 179, empty)
cv.createTrackbar("Sat Min", "TrackBars", 110, 255, empty)
cv.createTrackbar("Sat Max", "TrackBars", 240, 255, empty)
cv.createTrackbar("Val Min", "TrackBars", 153, 255, empty)
cv.createTrackbar("Val Max", "TrackBars", 255, 255, empty)


while True:

    img = cv.imread(path)
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv.getTrackbarPos("Val Max", "TrackBars")
    #print(h_min)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(imgHSV, lower, upper)

    imgResult = cv.bitwise_and(img, img, mask=mask)


    #cv.imshow('Elon Musk original', img)
    cv.imshow('Elon Musk HSV', imgHSV)
    cv.imshow('Elon Musk mask', mask)
    cv.imshow('Elon Musk imgResult', imgResult)
    cv.waitKey(0)