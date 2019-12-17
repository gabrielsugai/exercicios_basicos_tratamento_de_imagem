from PIL import Image
import numpy as np
from PIL import ImageFilter
img = Image.open("vegeta_goku.jpg")
#img_cinza = img.convert("RGB")
#img_cinza.show()
#x,y = img.size
#print("Tamanho da imagem %i por %i"%(x,y))
#r,g,b = img.split()
#r.show()
#g.show()
#b.show()
#img = np.array(Image.open("vegeta_goku.jpg").convert('L'))
#for linha in img:
#    print(linha)
#saida = 255 - img
#saida = Image.fromarray(saida)
#saida.show()
#saida = img.transpose(Image.ROTATE_90)
saida = img.filter(ImageFilter.EMBOSS)
#saida = img.filter(ImageFilter.Find_EDGES)
#saida = img.filter(ImageFilter.DETAIL)
saida.show()