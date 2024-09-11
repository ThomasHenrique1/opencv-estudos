import cv2 as cv
import numpy as np

img = cv.imread('Image/j.png',0)
#img = cv.resize(img,(256,256))
kernel = np.ones((9,9),np.uint8) # estrutura
dilate = cv.dilate(img, kernel, iterations = 2)
erosion = cv.erode(img,kernel,iterations = 1)
#close  = cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
close  = cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)
img2 = img - close
imgs = np.concatenate((img , blackhat,img2),axis=1)
cv.imshow("Imagens com BlackHat",imgs)
cv.waitKey(0)





