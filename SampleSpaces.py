import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('PhotoEdu/ElonMusk.jpg')
cv.imshow('Elon Musk', img)



#bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_RGB2BGR)
cv.imshow('Elon Musk rgb ', rgb )

#hsv to bgr
hsv_bgr = cv.cvtColor(img, cv.COLOR_HSV2BGR)
cv.imshow('Elon Musk hsv_bgr', hsv_bgr)


plt.imshow(img)
plt.show()

#cv.waitKey(0)