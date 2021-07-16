import cv2 as cv
import numpy as np

widthImg = 640
heightImg = 480


cap = cv.VideoCapture(0)
cap.set(3, widthImg)
cap.set(4, heightImg)
cap.set(10, 150)


def preProcessing(img):
    imgGray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    imgBlur = cv.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv.Canny(imgBlur, 200, 200)
    kernel = np.ones(5, 5)
    imgDial = cv.dilate(imgCanny, kernel, iterations=2)
    imgThres = cv.erode(imgDial, kernel, iterations=1)

    return imgThres




while True:
    success, img = cap.read()
    cv.resize(img, (widthImg, heightImg))
    
    imgThres = preProcessing(img)

    cv.imshow("Result", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break