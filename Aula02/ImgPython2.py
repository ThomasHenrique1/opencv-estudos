import cv2
import numpy as np

# Carrega a imagem 'Python.jpg' da pasta 'Image' usando OpenCV
img = cv2.imread('Image/Python.jpg')

# Separa os canais de cor da imagem (B, G, R)
blue, green, red = cv2.split(img)

# Cria uma imagem de zeros com o mesmo tamanho dos canais (representando os canais azul e verde)
zeros = np.zeros(blue.shape, np.uint8)

# Cria uma nova imagem onde apenas o canal vermelho é visível (BGR)
redBGR = cv2.merge((zeros, zeros, red))

# Concatena a imagem original e a imagem com apenas o canal vermelho lado a lado
resp = np.concatenate((img, redBGR), axis=1)

# Exibe a imagem concatenada em uma janela chamada "Orig x Equalidaza"
cv2.imshow("Orig x Equalidaza", resp)

# Aguarda até que uma tecla seja pressionada
cv2.waitKey(0)

# Fecha todas as janelas abertas pelo OpenCV
cv2.destroyAllWindows()
