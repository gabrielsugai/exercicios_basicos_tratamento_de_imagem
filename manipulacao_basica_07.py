# -*- coding: utf-8 -*-
import cv2

#Abre uma imagem que está salva no mesmo diretório que o arquivo python
imagem = cv2.imread("vegeta_goku.jpg")

#Converte a imagem para escala de cinza
hsv_imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

#Divide os canais
matiz, saturacao, valor = cv2.split(hsv_imagem)

#Manipulando a imagem
for i in range(len(valor)):
    for j in range(len(valor[i])):
        valor[i,j] *= 2

#Junta os canais
imagem_final_hsv = cv2.merge((matiz, saturacao, valor))

#Volta imagem para o espaço RGB
imagem_final = cv2.cvtColor(imagem_final_hsv, cv2.COLOR_HSV2BGR)

#Exibe o resultado final
cv2.imshow("Imagem processada", imagem_final)

#Aguarda que o x da tela possa ser clicado
cv2.waitKey(0)
cv2.destroyAllWindows()

