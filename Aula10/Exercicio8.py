import cv2

import numpy as np


Frame = cv2.imread("Image/bola_pink_blue.jpg")
hsv = cv2.cvtColor(Frame,cv2.COLOR_BGR2HSV)
#Procurar somente a cor red na imagem
lower_red = np.array([150,127,127])
upper_red =  np.array([250,255,255])

mask = cv2.inRange(hsv,lower_red,upper_red)
res = cv2.bitwise_and(Frame, Frame, mask=mask)

cv2.imshow("Frame", Frame)
cv2.imshow("Mask", mask)
cv2.imshow("Azul", res)
cv2.waitKey(0)
