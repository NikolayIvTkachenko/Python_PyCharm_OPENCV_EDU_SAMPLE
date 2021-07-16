import cv2
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
    kernel = np.ones((5, 5))
    imgDial = cv.dilate(imgCanny, kernel, iterations=2)
    imgThres = cv.erode(imgDial, kernel, iterations=1)

    return imgThres

def getCounters(img):
    biggest = np.array([])
    maxArea = 0
    counters, hierarchy = cv.findContours(img,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in counters:
        area = cv.contourArea(cnt)
        #print(area)
        if area > 5000:
            cv.drawContours(imgCounters, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            print(approx)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area

            #obj = len(approx)
            #x, y, w, h = cv.boundingRect(approx)
    cv.drawContours(imgCounters, biggest, -1, (255, 0, 0), 20)
    return biggest

def getWarp(img, biggest):
    biggest = reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0,0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv.warpPerspective(img, matrix, (widthImg, heightImg))

    return imgOutput

def reorder(points):
    points = points.reshape((4,2))
    pointsNew = np.zeros((4,1,2), np.int32)
    add = points.sum(1)
    print("add", add)

    pointsNew[0] = points[np.argmin(add)]
    pointsNew[3] = points[np.argmax(add)]

    diff = np.diff(points, axis=1)
    pointsNew[1] = points[np.argmin(diff)]
    pointsNew[2] = points[np.argmax(diff)]

    return pointsNew

while True:
    success, img = cap.read()
    cv.resize(img, (widthImg, heightImg))
    imgCounters = img.copy()

    imgThres = preProcessing(img)
    biggest = getCounters(imgThres)

    print(biggest)

    if len(biggest)>0:
        imgWraped = getWarp(img, biggest)
        imageArray = ([img, imgThres], [imgCounters, imgWraped])
        #stackedImages = stackedImages(0.6, imageArray)

    #cv.imshow("Stacked", stackedImages)
    cv.imshow("Result", imgCounters)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break