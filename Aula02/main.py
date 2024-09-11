# import cv2
#
# img = cv2.imread("Python.jpg")#Mostrar a imagem!
#
# #=========================================================
#
#
# # img2 = cv2.imread("Python.jpg", 0)
# # cv2.imshow("PythonColorido", img)#Nome do titulo da pagina, sempre diferenciar para rodar as imagens!
# # cv2.imshow("PythonCinza", img2)
#
# #============================================================
#
# # print(img)#Mostra uma parte da matriz
# # print(img.dtype)
# print(img.ndim)#mostra os canais
# print(img.shape)#mostra a largura,altura e os canais
# cv2.waitKey(0)#Colocar delay na imagem!
#
# #tamanho da imagem
# #largura x altura
# #tammanho em bytes
# #Largyra x altura x qTC X 255/8
#
# a , l , c = img.shape
# tIMG = a * l
# tIMGByte=  a * l * c * 255 / 8
# print(tIMGByte)
# print(img.shape)
# print(tIMG)

import cv2
import numpy as np

img = cv2.imread('Image/tempo620x465.jpg', 0)
eq = cv2.equalizeHist(img)#tem problema
resp = np.concatenate( ( img, eq), axis = 1 )
cv2.imshow("Orig x Equalidaza", resp)
cv2.waitKey(0)
cv2.destroyAllWindows()






# # #Exercicio 3
# import cv2
# import numpy as np
# img = cv2.imread('Python.jpg')
# blue, green, red = cv2.split(img)
# zeros = np.zeros(blue.shape, np.uint8)
# redBGR = cv2.merge( (zeros, zeros, red) )
# greenBGR = cv2.merge((zeros,green,zeros))
# #zeros = zeros * 0;
# cv2.imshow('Janela', redBGR)
# cv2.imshow('Janela2', greenBGR)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#
#
# #Exercicio 4
# import cv2
# img = cv2.imread("tempo620x465.jpg")#Mostrar a imagem!
# cv2.waitKey(0)#Colocar delay na imagem!
# print(img.shape)#mostra a largura,altura e os canais
# #Largyra x altura x qTC X 255/8
# a , l , c = img.shape
# tIMGByte=  a * l * c * 255 / 8
# print(tIMGByte)


