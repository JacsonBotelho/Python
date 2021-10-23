import cv2
import numpy as np

imagemOriginal = cv2.imread("D:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja.jpg",0)
metodo = cv2.THRESH_BINARY_INV
ret,imgBinarizada = cv2.threshold(imagemOriginal, 135, 255, metodo)

e = np.ones((3,3), np.uint8)
imgTratada = cv2.morphologyEx(imgBinarizada,cv2.MORPH_CLOSE, e)

imgSegmentada = cv2.Canny(imgTratada, 100, 200)


cv2.imshow("Binarizada", imgBinarizada)
cv2.imshow("Imagem Tratada", imgTratada)
cv2.imshow("Segmentada", imgSegmentada)

cv2.waitKey(0)
cv2.destroyAllWindows()