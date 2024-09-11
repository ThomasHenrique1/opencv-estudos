
import cv2
import numpy as np
img = cv2.imread('Image/Draco.jpg')
median = cv2.medianBlur(img, 5)
compare = np.concatenate((img, median), axis=1)

cv2.imshow("Original e Blur",compare)
cv2.waitKey(0)