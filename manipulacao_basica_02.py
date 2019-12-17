# -*- coding: utf-8 -*-
import cv2

#Pega a camera de video do sistema
camera = cv2.VideoCapture(0)

#Mantem o programa rodando
while True:
    #Pega um frame com a informação de retorno se ele deu certo
    ret, frame = camera.read()
    #Exibe a imagem em uma tela dedicada
    cv2.imshow("Titulo da img", frame)
    #Se o usuário apertar 'q' termina a aplicação
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
#Devolve a camera para o sistema
camera.release()
#Fecha qualquer tela que estiver aberta
cv2.destroyAllWindows()

