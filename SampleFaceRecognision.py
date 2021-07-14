import numpy as np
import cv2 as cv

people = ['elonmusk', 'richard', 'mila']
haar_cascade = cv.CascadeClassifier('haar/haarcascade_frontalface_default.xml')
#features = np.load('features.npy')
#labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread('C:\RSH-CODE\PyCharmProject\Project_opencv_edu\PhotoForValidation\mila\\val_mila002.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for(x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (0, 255, 255), thickness=3)
    cv.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), thickness=2)

cv.imshow('Deteting face', img)
cv.waitKey(0)