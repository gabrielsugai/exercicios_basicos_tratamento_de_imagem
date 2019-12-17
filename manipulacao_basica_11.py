# -*- coding: utf-8 -*-
import cv2
import numpy as np

#Abre uma imagem que está salva no mesmo diretório que o arquivo python
imagem = cv2.imread("sudoku.jpg")

#Cria uma matriz com os pontos iniciais da imagem
pontosIniciais = np.float32([
        [37,46], [183,42], [24,181], [197,180]
        ])

#Determina onde vão ficar os pontos finais
pontosFinais = np.float32([
        [0,0], [200,0], [0,200], [200,200]
        ])

#Cria a matriz de transformação de perspectiva
matriz = cv2.getPerspectiveTransform(
            pontosIniciais, pontosFinais
        )

#muda a perspectiva da imagem
imagemModificada = cv2.warpPerspective(
         imagem, matriz, (200,200)
        )

cv2.imshow("Imagem original", imagem)
cv2.imshow("Imagem com mudança de perspectiva", imagemModificada)

#Aguarda que o x da tela possa ser clicado
cv2.waitKey(0)
cv2.destroyAllWindows()

