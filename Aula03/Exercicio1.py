# Este código carrega uma imagem, separa seus canais de cor, 
# cria uma imagem com apenas o canal vermelho e exibe ambas lado a lado.

import cv2
import numpy as np

# Carrega a imagem
img = cv2.imread('Image/Python.jpg')

# Separa a imagem em canais de cor (azul, verde, vermelho)
blue, green, red = cv2.split(img)

# Cria uma imagem com apenas o canal vermelho
zeros = np.zeros(blue.shape, np.uint8)  # Matriz de zeros para canais azul e verde
redBGR = cv2.merge((zeros, zeros, red)) # Imagem com apenas o canal vermelho

# Concatena a imagem original e a imagem vermelha horizontalmente
resp = np.concatenate((img, redBGR), axis=1)

# Exibe a imagem resultante
cv2.imshow("Orig x Equalidaza", resp)
cv2.waitKey(0)       # Aguarda uma tecla ser pressionada
cv2.destroyAllWindows()  # Fecha todas as janelas
