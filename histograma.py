import cv2
import numpy as np
from matplotlib import pyplot as grafico

imagemOriginal = cv2.imread("C:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja.jpg",0)
imagemEqualizada = cv2.equalizeHist(imagemOriginal)
cv2.imshow("Imagem Original", imagemOriginal)
cv2.imshow("Imagem Equalizada",imagemEqualizada)
grafico.hist(imagemOriginal.ravel(),256,[0,256])
grafico.figure();
grafico.hist(imagemEqualizada.ravel(),256,[0,256])

grafico.show()