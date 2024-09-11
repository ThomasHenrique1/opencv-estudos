 #Exercicio 2

import cv2
import numpy as np

img = cv2.imread('Image/out.jpg', 0)
eq = cv2.equalizeHist(img)#tem problema
resp = np.concatenate( ( img, eq), axis = 1 )
cv2.imshow("Orig x Equalidaza", resp)
cv2.waitKey(0)
cv2.destroyAllWindows()