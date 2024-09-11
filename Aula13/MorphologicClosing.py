import cv2 as cv
import numpy as np

img = cv.imread('Image/closing.png',0)
#img = cv.resize(img,(256,256))
kernel = np.ones((5,5),np.uint8) # estrutura
# dilate = cv.dilate(img, kernel, iterations = 2)
# close = cv.erode(dilate,kernel,iterations = 2)
close  = cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)
imgs = np.concatenate((img ,close),axis=1)
cv.imshow("Imagens com closing",imgs)
cv.waitKey(0)
