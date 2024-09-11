import cv2
import numpy as np

# Carrega a imagem 'Python.jpg' usando OpenCV
img = cv2.imread('Image/Python.jpg')

# Separa os canais de cor da imagem (B, G, R)
blue, green, red = cv2.split(img)

# Cria uma imagem de zeros com o mesmo tamanho dos canais (representando o canal azul)
zeros = np.zeros(blue.shape, np.uint8)

# Cria uma nova imagem onde apenas o canal azul é visível (BGR)
blueBGR = cv2.merge((blue, zeros, zeros))

# Cria uma nova imagem onde apenas o canal verde é visível (BGR)
greenBGR = cv2.merge((zeros, green, zeros))

# Exibe a imagem com apenas o canal azul visível na janela chamada 'Janela2'
cv2.imshow('Janela2', blueBGR)

# Exibe a imagem com apenas o canal verde visível na janela chamada 'Janela'
cv2.imshow('Janela', greenBGR)

# Aguarda até que uma tecla seja pressionada
cv2.waitKey(0)

# Fecha todas as janelas abertas pelo OpenCV
cv2.destroyAllWindows()
