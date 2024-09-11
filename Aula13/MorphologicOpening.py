import cv2 as cv
import numpy as np

img = cv.imread('Image/opening.png',0)
#img = cv.resize(img,(256,256))
kernel = np.ones((5,5),np.uint8) # estrutura

# erosion = cv.erode(img,kernel,iterations = 2)
# dilate = cv.dilate(ero, kernel, iterations = 2)

opening = cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
imgs = np.concatenate((img ,opening),axis=1)
cv.imshow("Imagens com Opening",imgs)
cv.waitKey(0)
