
import numpy as np
import cv2
cinza = True

image = cv2.imread('Image/Draco.jpg')
canny = cv2.Canny(image, 15, 400)
if(cinza == True):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    #cv2.imshow("Imagem em Tons de Cinza", gray)
else:
    cv2.imshow("Imagem Colorida", image)
    #cv2.imwrite("resultado.jpg", image)

Resp = np.concatenate((gray,canny),axis=1)
cv2.imshow("original e com borda", Resp)
cv2.waitKey(0)