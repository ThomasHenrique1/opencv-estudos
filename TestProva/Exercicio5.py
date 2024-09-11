import cv2
import numpy as np

cinza = True

image = cv2.imread('Image/Draco.jpg')
# função ue converte img color em cinza
if(cinza == True):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    #cv2.imshow("Imagem em Tons de Cinza", gray)
    #cv2.imshow("Imagem Preto e Branco", bw)

else:
    cv2.imshow("Imagem Colorida", image)
    #cv2.imwrite("resultado.jpg", image)

resp = np.concatenate((gray, bw), axis=1)
cv2.imshow("Orig x Preta e Branco", resp)
cv2.waitKey(0)





