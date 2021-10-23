import cv2
import numpy as np

imagem = cv2.imread("D:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja.jpg")

tipo = cv2.THRESH_BINARY_INV
ret, imgBinarizada = cv2.threshold(imagem, 127, 255, tipo)

#obtendo os contornos dos objetos na imagem
modo = cv2.RETR_TREE;
metodo = cv2.CHAIN_APPROX_SIMPLE;
contornos, hierarquia = cv2.findContours(imgBinarizada, modo, metodo)

#obtendo os contornos dp primeiro objeto segmentado
objeto = contornos[0]

#obtendo a área do objeto segmentado
area = cv2.contourArea(objeto)
print(area)

cv2.waitKey(0)
cv2.destroyAllWindows()

