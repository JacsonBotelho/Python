import cv2
import numpy as np


imagemRGB = cv2.imread("D:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja_1.jpg",0)

imagemTonsDeCinza = cv2.imread("D:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja_1.jpg",0)

tipo = cv2.THRESH_BINARY_INV
ret, imgBinarizada = cv2.threshold(imagemTonsDeCinza, 70, 75, tipo)

#obtendo os contornos dos objetos na imagem
modo = cv2.RETR_TREE;
metodo = cv2.CHAIN_APPROX_SIMPLE;
contornos, hierarquia = cv2.findContours(imgBinarizada, modo, metodo)

#obtendo os contornos dp primeiro objeto segmentado
objeto = contornos[0]

# obtendo o ponto contral e o raio da circunferência
(x,y), raio = cv2.minEnclosingCircle(objeto)
centro= (int(x), int(y))
raio = int(raio)

#Desenhando a circurferência na imagem imagemRGB
cv2.circle(imagemRGB, centro, raio, (0,255,0),2)

cv2.imshow("Circunferencia Envolvente", imagemRGB)

print(x,y,raio)

cv2.waitKey(0)
cv2.destroyAllWindows()