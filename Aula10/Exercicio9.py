import cv2
import numpy as np

img = cv2.imread('Image/Dragon.jpg')
blue, green, red = cv2.split(img)
zeros = np.zeros(blue.shape, np.uint8)
redBGR = cv2.merge( (blue, zeros, red) )

blueBGR= cv2.merge((blue,green,zeros))
greenBGR = cv2.merge((zeros,red,green))
zeros = np.zeros(blue.shape, np.uint8)
resp = np.concatenate( ( img, redBGR), axis = 1 )
#cv2.imshow("Orig x Equalidaza", resp)
# cv2.imshow("yellow",greenBGR)
#cv2.imshow("ciano",blueBGR)
comp = np.concatenate((blueBGR,greenBGR),axis=1)

compare= np.concatenate((resp,comp),axis=1)#Estou deixando no 1 pois o numero 0 fica ruim de ver!
cv2.imshow("Resultado",compare)
cv2.waitKey(0)
cv2.destroyAllWindows()