# -*- coding: utf-8 -*-
import cv2

#Abre uma imagem que está salva no mesmo diretório que o arquivo python
imagem = cv2.imread("vegeta_goku.jpg")

#Divide a imagem em seus três canais de cores
azul, verde, vermelho = cv2.split(imagem)

#Exibe a imagem em uma tela dedicada
cv2.imshow("Titulo da img", imagem)
#cv2.imshow("CanalVermelho", vermelho)
#cv2.imshow("CanalAzulAntes", azul)
#cv2.imshow("CanalVerde", verde)
#print("Antes:")
#print(azul)
for i in range(len(azul)):
    for j in range(len(azul[i])):
        if azul[i,j]+50 > 255:
            azul[i,j] = 255
        else:
            azul[i,j] = azul[i,j] + 50
#print("Depois:")
#print(azul)
#cv2.imshow("CanalAzulDepois", azul)
imagem_nova = cv2.merge((azul, verde, vermelho))
cv2.imshow("Nova Imagem", imagem_nova)
#Salva as imagens em seus respectivos canais
#cv2.imwrite("CanalVermelho.jpeg", vermelho)
#cv2.imwrite("CanalAzul.jpeg", azul)
#cv2.imwrite("CanalVerde.jpeg", verde)

#Aguarda que o x da tela possa ser clicado
cv2.waitKey(0)
cv2.destroyAllWindows()

