import cv2

pb = True


image = cv2.imread('Image/bola_pink_blue.jpg')

#Função que converte img color em cinza
if(pb == True):
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#BGR2GRAY deixa a imagem cinza sem precisar colocar calcula
  thresh , bw = cv2.threshold(gray,127, 255, cv2.THRESH_BINARY)#Deixa a imagem preta e branca sem necessidade de calculo
  cv2.imshow("Imagem em tons de cinza", gray)  # Deixa a imagem cinza sem precisar de calcular!
  cv2.imshow("Imagem preto e branco", bw)  # Mostra a imagem preto a branco
  cv2.imwrite("resultado.jpg",bw) #Salva a imagem com um novo nome

cv2.waitKey(0)