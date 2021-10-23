# Operação de Adição

import cv2
import numpy as np
from matplotlib import pyplot as grafico

imagemOriginal = cv2.imread("D:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja.jpg")
imagem =cv2.add(imagemOriginal,0)
imagemClara = cv2.add(imagemOriginal,40)
imagemEscura = cv2.add(imagemOriginal,-40)

cv2.imshow("Imagem Original", imagemOriginal)
cv2.imshow("Imagem Clara", imagemClara)
cv2.imshow("Imagem Escura", imagemEscura)

grafico.hist(imagemOriginal.ravel(), 256, [0,256])

grafico.figure();
grafico.hist(imagemClara.ravel(), 256, [0,256])

grafico.figure();
grafico.hist(imagemEscura.ravel(), 256, [0,256])

grafico.show()

cv2.waitKey(0)
cv2.destroyAllWindows()