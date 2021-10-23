import cv2
imagem = cv2.imread("D:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja.jpg")
imagem =cv2.cvtColor(imagem,cv2.COLOR_BGR2HSV)
matriz, saturacao, valor = cv2.split(imagem)

cv2.imshow('Canal H',matriz)
cv2.imshow('Canal S',saturacao)
cv2.imshow('Canal V',valor)

imagem = cv2.merge((matriz, saturacao, valor))
imagem = cv2.cvtColor(imagem, cv2.COLOR_HSV2BGR)

cv2.imshow("imagem",imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()