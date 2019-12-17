# -*- coding: utf-8 -*-
import cv2

#Carrega a imagem para tratamento
img = cv2.imread("lena.jpg")

#Aplica o filtro de média
img_com_filtro = cv2.blur(img, (10,10))

#exibe as imagens
cv2.imshow("Original", img)
cv2.imshow("Com Filtro", img_com_filtro)

cv2.waitKey(0)
cv2.destroyAllWindows()
