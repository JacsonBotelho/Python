import cv2
import numpy as np

imagemOriginal = cv2.imread("D:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja.jpg",0)
elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
imagemProcessada = cv2.morphologyEx(imagemOriginal,cv2.MORPH_CLOSE ,elementoEstruturante)

imagemSubtraida = cv2.subtract(imagemOriginal,imagemProcessada)

imagemTratada = cv2.add(imagemSubtraida,imagemSubtraida)

cv2.imshow("Imagem Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)
cv2.imshow("Subtraida",imagemSubtraida)
cv2.imshow("Tratada", imagemTratada)


cv2.waitKey(0)
cv2.destroyAllWindows()