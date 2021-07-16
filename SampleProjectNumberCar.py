import cv2 as cv

frameWidth = 640
frameHeight = 480

plateCascade = cv.CascadeClassifier("haar/haarcascade_russian_plate_number.xml")
minArea = 500
color = (255, 0, 200)

cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

while True:
    success, img = cap.read()

    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    numberPlate = plateCascade.detectMultiScale(imgGray, 1.1, 5)

    for(x, y, w, h) in numberPlate:
        area = w * h
        if area > minArea:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
            cv.putText(img, "Car Number", (x, y-5), cv.FONT_HERSHEY_COMPLEX, 1, color, 2)
            imgRoi = img[y:y+h, x:x+w]
            cv.imshow("ROI", imgRoi)



    cv.imshow("Result", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        #cv.imwrite("TestPhoto/plate+".jpg, imgRoi)
        break