import sys
# Adiciona os diretórios 'IMGS' e 'LIBS' ao caminho do sistema para importar módulos ou arquivos de lá, se necessário.
sys.path.insert(0, 'IMGS')
sys.path.insert(0, 'LIBS')

# Importa a biblioteca de matemática padrão, a biblioteca 'tkinter' para interfaces gráficas, e a biblioteca 'graphics' (possivelmente um módulo externo).
import math
from tkinter import *
from graphics import *

# Cria uma janela gráfica chamada "Sonic Cor Preto e Branco" com dimensões de 640x480 usando a biblioteca graphics.
win = GraphWin("Sonic Cor Preto e Branco", 640, 480)

# Carrega a imagem 'sonic.png' da pasta 'Image' usando o 'PhotoImage' do tkinter.
im = PhotoImage(file='Image/sonic.png')

# Também carrega a mesma imagem 'sonic.png' usando a função 'Image' da biblioteca 'graphics'.
im2 = Image(Point(300, 200), 'Image/sonic.png')

# Loop para iterar sobre os primeiros 150x197 pixels da imagem.
for i in range(0, 150):
    for j in range(0, 197):
        # Obtém os valores de vermelho (r), verde (g) e azul (b) do pixel na posição (i, j).
        r, g, b = im.get(i, j)
        
        # Ajusta as coordenadas de onde o pixel será desenhado.
        px = int(i + 50)
        py = int(j + 50)

        # Calcula a média dos valores RGB para converter a cor em escala de cinza.
        media = int((r + g + b) / 3)

        # Se a média for maior ou igual a 127, define o valor da cor como branco (255). Caso contrário, define como preto (0).
        if media >= 127:
            media = 255
        else:
            media = 0
        
        # Converte o valor da cor para o formato hexadecimal necessário para desenhar na tela.
        colorval = "#%02x%02x%02x" % (media, media, media)
        
        # Desenha um único pixel (como um pequeno quadrado) na tela, na cor preta ou branca, dependendo da média calculada.
        win.create_rectangle(
            px, py, px, py, width=0, fill=(colorval))       

# Desenha a imagem original 'sonic.png' no ponto (300, 200) da janela.
im2.draw(win)

# Inicia o loop principal da interface gráfica, mantendo a janela aberta e aguardando interações do usuário.
win.mainloop()

# Fecha a janela quando o loop principal termina.
win.close()
