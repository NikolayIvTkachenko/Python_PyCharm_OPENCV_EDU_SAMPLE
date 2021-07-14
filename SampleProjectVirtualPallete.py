import cv2 as cv
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

def empty(a):
    pass

appColor = [[5, 107, 0, 19, 255, 255],
            [133, 56, 0, 159, 156, 255],
            [57, 76, 0, 100, 255, 255],
            [90, 48, 0, 118, 255, 255]]

appColorValues = [[51, 153, 255],
                  [255, 0, 255],
                  [0, 255, 0],
                  [255, 0, 0]]

appPoint = [] ##[x, y, colorId]

#cv.namedWindow("TrackBars")
#cv.resizeWindow("TrackBars", 640, 240)
#cv.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
#cv.createTrackbar("Hue Max", "TrackBars", 19, 179, empty)
#cv.createTrackbar("Sat Min", "TrackBars", 110, 255, empty)
##cv.createTrackbar("Sat Max", "TrackBars", 240, 255, empty)
#cv.createTrackbar("Val Min", "TrackBars", 153, 255, empty)
#cv.createTrackbar("Val Max", "TrackBars", 255, 255, empty)


def findColor(img, appColors, appColorsValues):
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    #h_min = cv.getTrackbarPos("Hue Min", "TrackBars")
    #h_max = cv.getTrackbarPos("Hue Max", "TrackBars")
    #s_min = cv.getTrackbarPos("Sat Min", "TrackBars")
    #s_max = cv.getTrackbarPos("Sat Max", "TrackBars")
    #v_min = cv.getTrackbarPos("Val Min", "TrackBars")
    #v_max = cv.getTrackbarPos("Val Max", "TrackBars")

    for color in appColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        #cv.circle(imgResult, (x, y), 10, (255, 0, 0), cv.FILLED)
        cv.circle(imgResult, (x, y), 10, appColorsValues[count], cv.FILLED)

        if x != 0 and y != 0:
            newPoints.append([x, y, count])

        count += 1
        #cv.imshow(f'img = {str(color[0])}', mask)
    return newPoints



def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv.contourArea(cnt)
        #print(area)
        if area > 500:
            #cv.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            #print(peri)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            #print(len(approx))
            #objCor = len(approx)
            x, y, w, h = cv.boundingRect(approx)
    return x+w//2, y

def drawOnCanvas(appPoints, appColorValues):
    for point in appPoints:
        cv.circle(imgResult, (point[0], point[1]), 10, appColorValues[point[2]], cv.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()

    #findColor(img)
    newPoints = findColor(img, appColor, appColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            appPoint.append(newP)

    if len(appPoint) != 0:
        drawOnCanvas(appPoint, appColorValues)

    #cv.imshow("Result", img)
    cv.imshow("Result", imgResult)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break