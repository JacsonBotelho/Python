import cv2
import numpy as np

imgRGB = cv2.imread("D:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja_queimada.webp")
imgHSV = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2HSV)

# Limite inferior
tomClaro = np.array([160,100,100])

# Limite Superior
tomEscuro = np.array([200,255,255])

imgSegmentada = cv2.inRange(imgHSV,tomClaro,tomEscuro)

cv2.imshow("Imagem Original", imgRGB)
cv2.imshow("Segmentada", imgSegmentada)

cv2.waitKey(0)
cv2.destroyAllWindows()