import cv2

#Tras os dados do classificador de faces
classificador = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Traz os dados do classificador de olhos
#classificador_olhos = cv2.CascadeClassifier("haarcascade_eye.xml")

#Abre a imagem
#imagem = cv2.imread('pessoas/beatles.jpg')
#imagem = cv2.imread('pessoas/faceolho.jpg')
imagem = cv2.imread('../vegeta_goku.jpg')
#Converte a imagem para escala de cinza
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

#Usa o classificador para encontrar as faces nas imagens
facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.2, minNeighbors = 3, minSize = (30,30))

#Imprime o tamanho da lista com os dados encontrados
#print(len(facesDetectadas))

#Varre os dados da matriz de detecção: [x_de_onde_encontrou y_de_onde_encontrou largura altura]
for (x,y,largura, altura) in facesDetectadas:
    #Desenha um retangulo vermelho na imagem
    cv2.rectangle(imagem, (x,y), (x+largura, y+altura), (0,0,255), 2)
    #Pega a região em que a face foi detectada
#    regiao_detectada = imagem[ y:y+altura, x:x+largura]
#    #Converte a região para escala de cinza
#    regiao_detectada_cinza = cv2.cvtColor(regiao_detectada, cv2.COLOR_BGR2GRAY)
#    #Chama o classificador para detectar os olhos
#    olhos_detectados = classificador_olhos.detectMultiScale(regiao_detectada_cinza, scaleFactor = 1.035, minSize = (15,15), minNeighbors = 10)
#    #Varre os dados da matriz de detecção: [x_de_onde_encontrou y_de_onde_encontrou largura altura]
#    for (x_olhos,y_olhos,largura_olhos, altura_olhos) in olhos_detectados:
#        #Desenha um retangulo vermelho na imagem
#        cv2.rectangle(regiao_detectada, (x_olhos,y_olhos), (x_olhos+largura_olhos, y_olhos+altura_olhos), (255,0,0), 2)

#Mostra a imagem
cv2.imshow("Faces encontradas", imagem)
#Espera uma tecla para fechar a imagem
cv2.waitKey()