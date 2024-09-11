import cv2 as cv
import numpy as np
img = cv.imread('Image/brain_noisy.png')
#media
kernel = np.ones((7,7),np.float32)/49
dst = cv.filter2D(img,-1,kernel)
imgs_concat = np.concatenate((img, dst), axis=1)

#mediana
median = cv.medianBlur(img, 7)
cv.imshow('Mediana', median)

cv.imshow('taj_noise',imgs_concat)
cv.waitKey(0)
cv.destroyAllWindows()