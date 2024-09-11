# Importa a biblioteca OpenCV
import cv2

# Carrega a imagem 'tempo620x465.jpg'
img = cv2.imread("Image/tempo620x465.jpg")

# Exibe a imagem em uma janela
cv2.imshow("Imagem", img)

# Aguarda até que uma tecla seja pressionada antes de fechar a janela
cv2.waitKey(0)

# Fecha todas as janelas abertas pelo OpenCV
cv2.destroyAllWindows()

# Obtém as dimensões da imagem: altura (a), largura (l) e número de canais (c)
a, l, c = img.shape

# Calcula o tamanho da imagem em bytes
# A fórmula considera a profundidade de cor (8 bits por canal) e calcula o total de bytes
tIMGByte = a * l * c * 255 / 8

# Exibe o tamanho da imagem em bytes
print(f"Dimensões da imagem (Altura x Largura x Canais): {a} x {l} x {c}")
print(f"Tamanho da imagem em bytes: {tIMGByte:.2f}")
