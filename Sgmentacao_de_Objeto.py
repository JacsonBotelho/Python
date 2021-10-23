import cv2
import numpy as np

imagemOriginal = cv2.imread("D:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja.jpg",0)
metodo = cv2.THRESH_BINARY_INV
ret,imgBinarizada = cv2.threshold(imagemOriginal, 135, 255, metodo)

cv2.imshow("Imagem Original", imagemOriginal)
cv2.imshow("Imagem Tratada", imgBinarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()