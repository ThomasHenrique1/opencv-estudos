# #Exercicio 4
import cv2
img = cv2.imread("Image/tempo620x465.jpg")#Mostrar a imagem!
cv2.waitKey(0)#Colocar delay na imagem!
print(img.shape)#mostra a largura,altura e os canais
#Largyra x altura x qTC X 255/8
a , l , c = img.shape
tIMGByte=  a * l * c * 255 / 8
print(tIMGByte)
