
import cv2

cinza = True


image = cv2.imread('Image/bolas_cores.jpg')

#Função que converte img color em cinza
if(cinza == True):
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#BGR2GRAY deixa a imagem cinza sem precisar colocar calcula
  thresh , bw = cv2.threshold(gray,127, 255, cv2.THRESH_BINARY)#Deixa a imagem preta e branca sem necessidade de calculo
  cv2.imshow("Imagem em tons de cinza", gray)  # Deixa a imagem cinza sem precisar de calcular!
  cv2.imshow("Imagem preto e branco", bw)  # Mostra a imagem preto a branco
else:
  cv2.imshow("Imagem colorida", image)
  cv2.imwrite("resultado.jpg",image) #Salva a imagem com um novo nome

cv2.waitKey(0)


# import cv2
#
# import numpy as np
#
#
# Frame = cv2.imread("bolas_cores.jpg")
# hsv = cv2.cvtColor(Frame,cv2.COLOR_BGR2HSV)
# #Procurar somente a cor azul na imagem
# lower_blue = np.array([110,127,127])
# upper_blue =  np.array([130,255,255])
#
# mask = cv2.inRange(hsv,lower_blue,upper_blue)
# res = cv2.bitwise_and(Frame, Frame, mask=mask)
#
# cv2.imshow("Frame", Frame)
# cv2.imshow("Mask", mask)
# cv2.imshow("Azul", res)
# cv2.waitKey(0)

# import cv2
#
# img = cv2.imread("face_a.jpg")
# #crop =  img[y:y+a , x:x+b]
# crop = img[96:137:,49:155]#Arruma os numeros para o OPENCV fazer o corte na imagem
# cv2.imshow("Original",img)
# cv2.imshow("Crop", crop)
#
# cv2.waitKey(0)



