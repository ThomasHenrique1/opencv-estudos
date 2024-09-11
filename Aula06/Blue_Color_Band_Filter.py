import cv2
import numpy as np

# Carrega a imagem original
frame = cv2.imread("Image/bolas_cores.jpg")

# Converte a imagem para o espaço de cor HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Define os limites para a cor azul
lower_blue = np.array([110, 127, 127])
upper_blue = np.array([130, 255, 255])

# Cria uma máscara para a cor azul
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Aplica a máscara na imagem original
res = cv2.bitwise_and(frame, frame, mask=mask)

# Converte a máscara para uma imagem com 3 canais (para concatenação)
mask_3d = cv2.merge([mask, mask, mask])

# Concatena as imagens (frame, mask_3d, res) horizontalmente
resp = np.concatenate((frame, mask_3d, res), axis=1)

# Exibe a imagem concatenada
cv2.imshow('Original x Mascara x Final', resp)

# Aguarda até que uma tecla seja pressionada
cv2.waitKey(0)

# Fecha todas as janelas abertas pelo OpenCV
cv2.destroyAllWindows()
