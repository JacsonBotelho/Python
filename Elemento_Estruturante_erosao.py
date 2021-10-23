import cv2
import numpy as np

imagemOriginal = cv2.imread("D:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja.jpg",0)
elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
imagemProcessada = cv2.erode(imagemOriginal,elementoEstruturante,iterations=2)

cv2.imshow("Imagem Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)
cv2.waitKey(0)
cv2.destroyAllWindows()