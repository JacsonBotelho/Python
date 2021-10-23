import cv2
import numpy as np

def points_template_matching(imagemOriginal, template):
    points = []
    threshold = 0.9

    resp = cv2.matchTemplate(imagemOriginal, template, cv2.TM_CCOEFF_NORMED)
    candidatos = np.where(resp >= threshold)
    candidatos = np.column_stack([candidatos[1], candidatos[0]])
    print(candidatos)
    print("len(candidatos) = ",len(candidatos))

    i=0
    while len(candidatos) > 0:
        if i ==0: points.append(candidatos[0])
        else:
            to_delete = []
            for j in range (0, len(candidatos)):
                diff = points[i-1] - candidatos[j]
                if abs(diff[0]) < 10 and abs(diff[1]) < 10:
                    to_delete.append(j)
                print ("diff = ", diff)
            print(to_delete)
            candidatos = np.delete(candidatos, to_delete, axis=0)
            print(candidatos)
            print("len(candidatos) = ",len(candidatos))
            if len(candidatos) ==0: break
            points.append(candidatos[0])
        i += 1
    return points

imagemOriginal = cv2.imread("D:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja.jpg")

imagem_gray = cv2.cvtColor(imagemOriginal, cv2.COLOR_BGR2GRAY)

imgBinarizada = cv2.adaptiveThreshold(
    imagem_gray, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV, 11,5
)

template1 = cv2.imread("D:/Users/campo/Documents/ALURA\ANALISE_E_CLASSIFICACAO_FACIAL/alura-analise-facial-aula_3/alura-analise-facial-aula_3/imagens/soja5.jpg",0)

points1 = points_template_matching(imagem_gray, template1)
print("points1",points1)

template2 = cv2.flip(template1, -1)
points2 = points_template_matching(imagem_gray, template2)
print("points2",points2)

if len(points1) > 0 and len(points2) > 0:
    points = np.concatenate((points1, points2))
elif len(points1) == 0 and len(points2) == 0:
    points = []
elif len(points1) == 0 and len(points2) > 0:
    points = points2
elif len(points1) > 0 and len(points2) == 0:
    points = points1

for point in points:
    x1, y1 = point[0], point[1]
    x2, y2 = point[0] + template1.shape[1], point[1] + template1.shape[0]
    cv2.rectangle(imagemOriginal, (x1,y1), (x2,y2), (0,255,0),2)

cv2.putText(imagemOriginal,str(len(points)), (95,35), 1, 3, (0,255,0),2)
cv2.imshow("Imagem Original", imagemOriginal)
cv2.imshow("template1", template1)
cv2.imshow("template2", template2)
cv2.imshow("Binaria", imgBinarizada)

cv2.waitKey(0)
cv2.destroyAllWindows()