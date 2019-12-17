# -*- coding: utf-8 -*-

import cv2

#img = cv2.imread("lena.jpg")
#
#img_com_filtro = cv2.blur(img, (5,5))
#
#cv2.imshow("Img normal", img)
#cv2.imshow("Img media", img_com_filtro)
#
#img_com_filtro = cv2.GaussianBlur(img,(5,5), 0)
#cv2.imshow("Filtro Gaussiano", img_com_filtro)
#
#nova_img = img
#for i in range(len(img)):
#    for j in range(len(img[i])//2):
#        nova_img[i,j] = img_com_filtro[i,j]
#
#cv2.imshow("Fusao", nova_img)
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()

##############################################################################

img = cv2.imread("lena.jpg")

img_com_filtro = cv2.blur(img, (5,5))

cv2.imshow("Img normal", img)
cv2.imshow("Img media", img_com_filtro)

img_com_filtro = cv2.GaussianBlur(img,(5,5), 0)
cv2.imshow("Filtro Gaussiano", img_com_filtro)

img_com_filtro = cv2.medianBlur(img,5)
cv2.imshow("Filtro mediana", img_com_filtro)
                                     #tam,matriz,influ de cor, influ pixel vizinho
img_com_filtro = cv2.bilateralFilter(img,5,70,70)
cv2.imshow("Filtro bilateral", img_com_filtro)

img2 = cv2.imread("estacionamento.jpg")
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2_g = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(img_g, 100,100)
cv2.imshow("Canny Lenna", canny)
canny = cv2.Canny(img2_g, 400,400)
cv2.imshow("eSTACIONAMENTO", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
