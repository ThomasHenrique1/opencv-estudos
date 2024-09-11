import cv2
import numpy as np

# Carrega a imagem
Frame = cv2.imread("Image/bolas_cores.jpg")
hsv = cv2.cvtColor(Frame, cv2.COLOR_BGR2HSV)

# Define os limites para a cor vermelha
lower_red = np.array([150, 127, 127])
upper_red = np.array([250, 255, 255])

# Cria uma máscara para a cor vermelha
mask = cv2.inRange(hsv, lower_red, upper_red)

# Aplica a máscara na imagem
res = cv2.bitwise_and(Frame, Frame, mask=mask)

# Converte a máscara para uma imagem RGB para concatenação
mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

# Concatena as imagens horizontalmente
resp = np.concatenate((Frame, mask_rgb, res), axis=1)

# Mostra as imagens
cv2.imshow('Frame x Mask x Verde', resp)

# Espera até que uma tecla seja pressionada e fecha as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
