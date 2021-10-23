import cv2

imagemOriginal = cv2.imread("D:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja.jpg")
imagemTratada = cv2.bilateralFilter(imagemOriginal, 9,75,75)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Tratada", imagemTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()



