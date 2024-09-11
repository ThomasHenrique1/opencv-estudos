import cv2
import numpy as np

# Carrega a imagem 'out.jpg' da pasta 'Image' em modo de escala de cinza
img = cv2.imread('Image/out.jpg', 0)

# Equaliza o histograma da imagem para melhorar o contraste
eq = cv2.equalizeHist(img)

# Concatena a imagem original e a imagem equalizada lado a lado
resp = np.concatenate((img, eq), axis=1)

# Exibe a imagem concatenada em uma janela chamada "Orig x Equalidaza"
cv2.imshow("Orig x Equalidaza", resp)

# Aguarda até que uma tecla seja pressionada
cv2.waitKey(0)

# Fecha todas as janelas abertas pelo OpenCV
cv2.destroyAllWindows()
