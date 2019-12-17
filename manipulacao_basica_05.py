# -*- coding: utf-8 -*-
import cv2

#Abre uma imagem que está salva no mesmo diretório que o arquivo python
imagem = cv2.imread("vegeta_goku.jpg")

#Converte a imagem para escala de cinza
gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

#Exibe as duas imagens
cv2.imshow("Imagem colorida", imagem)
cv2.imshow("Escala de cinza", gray)

#Aguarda que o x da tela possa ser clicado
cv2.waitKey(0)
cv2.destroyAllWindows()

