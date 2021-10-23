import cv2
import statistics

imagemBinaria = cv2.imread("D:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja.jpg",0)
imgTonsdeCinza = cv2.imread("D:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja.jpg",0)

rolBinaria = imagemBinaria.ravel()
rolTonsdeCinza = imgTonsdeCinza.ravel()

print(statistics.mode(rolBinaria))
print(statistics.mode(rolTonsdeCinza))

