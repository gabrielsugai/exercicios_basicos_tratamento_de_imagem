# -*- coding: utf-8 -*-
import cv2

#Carrega a imagem para tratamento
img = cv2.imread("estacionamento.jpg")

#Imagem em cinza
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Aplica o filtro Canny
img_com_filtro = cv2.Canny(img_gray, 300, 300)

#exibe as imagens
cv2.imshow("Original", img_gray)
cv2.imshow("Com Filtro", img_com_filtro)

cv2.waitKey(0)
cv2.destroyAllWindows()
