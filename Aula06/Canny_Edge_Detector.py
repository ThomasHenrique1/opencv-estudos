import cv2
import numpy as np

# Carrega a imagem original
img = cv2.imread("Image/bola_pink_blue.jpg")

# Aplica o detector de bordas Canny na imagem
canny = cv2.Canny(img, 10, 400)

# Converte a imagem em escala de cinza (canny) para uma imagem com 3 canais
canny_3c = cv2.merge([canny, canny, canny])

# Concatena a imagem original e a imagem de bordas com 3 canais
imgs_concat = np.concatenate((img, canny_3c), axis=1)

cv2.imshow("Original x Bordas", imgs_concat)  # Exibe a concatenação das imagens

# Aguarda até que uma tecla seja pressionada
cv2.waitKey(0)

# Fecha todas as janelas abertas pelo OpenCV
cv2.destroyAllWindows()
