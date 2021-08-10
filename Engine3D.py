#Codigo ayuda: https://github.com/churly92/Engine3D/blob/main/gl.py
#Repositorio perteneciente a Prof. Carlos Alonso

#Mirka Monzon 18139
#SR4: Flat Shading & Textures

from textura import Texture
from gl import Bitmap

bmp = Bitmap(1000, 1000)

def glInit():
    return bmp


if __name__ == '__main__':

    #Inicializa obj
    bmp = glInit()

    #Cambia todos los pixeles de un color
    bmp.glClear()

    #Colores de pixeles
    bmp.glColor(1, 1, 1)

    fur = Texture("Textura1.bmp")

    bmp.glLoadObjModel('cat.obj', texture = fur)
    
    #Output BMP
    bmp.glWrite("out.bmp")