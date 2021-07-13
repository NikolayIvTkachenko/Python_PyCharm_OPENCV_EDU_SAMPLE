import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#Read Photo
#img = cv.imread('PhotoEdu/ElonMusk.jpg')
#cv.imshow('Elon Musk', img)
#cv.waitKey(0)


#Read video
#capture = cv.VideoCapture(0) #web camera from computere
capture = cv.VideoCapture('VideoEdu/DoctorWho.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resize = rescaleFrame(frame)
    cv.imshow('Video', frame_resize)

    if cv.waitKey(20) & 0xFF == ord('d'):# press d -destroy
        break
capture.release()
cv.destroyAllWindows()

