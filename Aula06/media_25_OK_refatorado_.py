import cv2 as cv
import numpy as np
img = cv.imread('Image/taj_noise.jpg')
kernel = np.ones((9,9),np.float32)/81
dst = cv.filter2D(img,-1,kernel)#Adicona um BLUR na imagem
imgs_concat = np.concatenate((img, dst), axis=1)
cv.imshow('taj_noise',imgs_concat)
cv.waitKey(0)
cv.destroyAllWindows()
