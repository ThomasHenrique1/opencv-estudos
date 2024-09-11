#Exercicio 3
import cv2
import numpy as np
img = cv2.imread('Image/Python.jpg')
blue, green, red = cv2.split(img)
zeros = np.zeros(blue.shape, np.uint8)
redBGR = cv2.merge( (zeros, zeros, red) )
greenBGR = cv2.merge((zeros,green,zeros))
zeros = zeros * 0;

resp = np.concatenate((redBGR, greenBGR), axis = 1)
cv2.imshow('Vermelho e Verde',resp)

cv2.waitKey(0)
cv2.destroyAllWindows()