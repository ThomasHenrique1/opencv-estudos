import cv2 as cv
import numpy as np

img = cv.imread('Image/j.png',0)
img = cv.resize(img,(256,256))
kernel = np.ones((5,5),np.uint8) # estrutura
dilate = cv.dilate(img, kernel, iterations = 2)
erosion = cv.erode(img,kernel,iterations = 2)

imgs = np.concatenate((img , erosion, dilate),axis=1)
cv.imshow("Imagens com erosão",imgs)
cv.waitKey(0)

