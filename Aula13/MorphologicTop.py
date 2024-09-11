import cv2 as cv
import numpy as np

img = cv.imread('Image/j.png',0)
#img = cv.resize(img,(256,256))
kernel = np.ones((9,9),np.uint8) # estrutura
#dilate = cv.dilate(img, kernel, iterations = 2)
#erosion = cv.erode(img,kernel,iterations = 1)
#close  = cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)
opening = cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
img2 =  img - opening
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
imgs = np.concatenate((img ,img2,tophat),axis=1)
cv.imshow("Imagens com closing",imgs)
cv.waitKey(0)