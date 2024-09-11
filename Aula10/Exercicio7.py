import cv2
import numpy as np

img = cv2.imread('Image/Dragon.jpg')
blue, green, red = cv2.split(img)

zeros = np.zeros(blue.shape, np.uint8)
redBGR = cv2.merge( (zeros, zeros, red) )
zeros = np.zeros(blue.shape, np.uint8)

resp = np.concatenate( ( img, redBGR), axis = 1 )

cv2.imshow("Orig x Equalidaza", resp)
cv2.waitKey(0)
