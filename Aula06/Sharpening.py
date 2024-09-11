#Sharpening
import cv2
import numpy as np

image = cv2.imread('taj_noise.jpg')
kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])

sharp = cv2.filter2D(image, -1, kernel)
cv2.imshow("Original", image)
cv2.imshow("Sharpening", sharp)
cv2.waitKey(0)