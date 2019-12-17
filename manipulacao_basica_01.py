# -*- coding: utf-8 -*-
import cv2

#Abre uma imagem que está salva no mesmo diretório que o arquivo python
imagem = cv2.imread("vegeta_goku.jpg")

#Exibe a imagem em uma tela dedicada
cv2.imshow("Titulo da img", imagem)

#Aguarda que o x da tela possa ser clicado
cv2.waitKey(0)
cv2.destroyAllWindows()

