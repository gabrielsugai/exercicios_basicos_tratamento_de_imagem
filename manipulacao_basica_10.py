# -*- coding: utf-8 -*-
import cv2
import numpy as np

#Abre uma imagem que está salva no mesmo diretório que o arquivo python
imagem = cv2.imread("poker.jpg")

#Troca o tamanho da image utilizando interpolação cubica
imagemModificada = cv2.resize(
        imagem, None, fx = 0.5, fy = 0.5,
        interpolation= cv2.INTER_CUBIC)

cv2.imshow("Imagem com novo tamanho", imagemModificada)

#Aguarda que o x da tela possa ser clicado
cv2.waitKey(0)
cv2.destroyAllWindows()

