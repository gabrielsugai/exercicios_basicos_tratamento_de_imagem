# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt

#Abre uma imagem que está salva no mesmo diretório que o arquivo python
imagem = cv2.imread("poker.jpg")
#Converte a imagem para escala de cinza
hsv_imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
#Divide os canais
matiz, saturacao, valor = cv2.split(hsv_imagem)
plt.hist(saturacao.ravel(), 256, [0,256])
plt.show()
nova_saturacao = cv2.equalizeHist(saturacao)
plt.figure()
plt.hist(nova_saturacao.ravel(), 256, [0,256])
plt.show()
nova_imagem = cv2.merge((matiz,nova_saturacao,valor))
nova_imagem = cv2.cvtColor(nova_imagem, cv2.COLOR_HSV2BGR)
cv2.imshow("Imagem Original:", imagem)
cv2.imshow("Nova imagem:", nova_imagem)

#Aguarda que o x da tela possa ser clicado
cv2.waitKey(0)
cv2.destroyAllWindows()

