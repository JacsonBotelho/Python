import cv2
imagem = cv2.imread("D:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja.jpg")
'''valorPixel = imagem[150,150]
print(valorPixel)'''

'''imagem =cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
valorPixel = imagem[150,150]
print(valorPixel)'''

'''valorPixel = imagem[150,150,0]
print(valorPixel)'''

print(imagem.shape) # tras informacoes sobre numero de linhas e colunas, canais e
                    # quantidade de pixels.

print(imagem.size) # total de pixel, multiplicando o total de linhas pelo total de
                   # colunas 

