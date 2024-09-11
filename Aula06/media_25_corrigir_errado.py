import cv2 as cv
import numpy as np
img = cv.imread('Image/brain_noisy.png')
kernel = np.array([
    [1/25, 1/25, 1/25, 1/25, 1/25],
    [1/25, 1/25, 1/25, 1/25, 1/25],
    [1/25, 1/25, 1/25, 1/25, 1/25],
    [1/25, 1/25, 1/25, 1/25, 1/25],
    [1/25, 1/25, 1/25, 1/25, 1/25]
    ])
dst = cv.filter2D(img,-1,kernel)
imgs_concat = np.concatenate((img, dst), axis=1)
cv.imshow('brain_noisy',imgs_concat)
cv.waitKey(0)
cv.destroyAllWindows()