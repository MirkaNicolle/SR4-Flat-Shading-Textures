#Codigo ayuda: https://github.com/churly92/Engine3D/blob/main/gl.py
#Repositorio perteneciente a Prof. Carlos Alonso

#Mirka Monzon 18139
#SR4: Flat Shading & Textures

#Lector de archivos .obj
class ObjReader(object):

    def __init__(self, filename):
        #Abre y lee archivos .obj
        with open(filename) as obj_file:
            self.lines = obj_file.read().splitlines()
        
        self.vertices = []
        self.normals = []
        self.tex_coords = []
        self.faces = []

        #Lee lineas individuales del archivo .obj 
        self.readLines()
    

    def removeSpaces(self, face):
        #Remueve espacios en blanco si los hay
        store_data = face.split('/')

        if ("") in store_data:
            store_data.remove("")
        
        return map(int, store_data)

    def readLines(self):
        #Lee lineas individuales del archivo .obj
        for line in self.lines:
            if line:
                prefix, value = line.split(' ', 1)
                if prefix == 'v':
                    self.vertices.append(list(map(float,value.split(' '))))
                elif prefix == 'vn':
                    self.normals.append(list(map(float,value.split(' '))))
                elif prefix == 'vt':
                    self.tex_coords.append(list(map(float,value.split(' '))))
                elif prefix == 'f':
                    self.faces.append([list(self.removeSpaces(face)) for face in value.split(' ')])