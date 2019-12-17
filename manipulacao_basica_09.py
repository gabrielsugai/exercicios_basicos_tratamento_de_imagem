# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Abre uma imagem que está salva no mesmo diretório que o arquivo python
imagem = cv2.imread("poker.jpg")

#Converte a imagem para escala de cinza
gray_imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

#Equaliza o histograma da imagem
gray_equalizada = cv2.equalizeHist(gray_imagem)

#Carrega o histograma da imagem em escala de cinza
plt.hist(gray_imagem.ravel(), 256, [0,256])
plt.show()
plt.figure()
plt.hist(gray_equalizada.ravel(), 256, [0,256])
plt.show()

#Exibe as duas imagens
cv2.imshow("Imagem sem equalizar", gray_imagem)
cv2.imshow("Imagem equalizada", gray_equalizada)

#Aguarda que o x da tela possa ser clicado
cv2.waitKey(0)
cv2.destroyAllWindows()

