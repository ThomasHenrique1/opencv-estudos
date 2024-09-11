import cv2 as cv
import numpy as np

img = cv.imread('Image/j.png',0)
img = cv.resize(img,(256,256))
kernel = np.ones((5,5),np.uint8) # estrutura
dilate = cv.dilate(img, kernel, iterations = 2)
erosion = cv.erode(img,kernel,iterations = 1)
#close  = cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)
img2 =  dilate - erosion
imgs = np.concatenate((img ,dilate,erosion,img2),axis=1)
cv.imshow("Imagens com closing",imgs)
cv.waitKey(0)