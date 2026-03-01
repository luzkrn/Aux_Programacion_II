class Instrumento:
    def __init__(self,nombre,material=None,tipo=None):
        self.nombre=nombre
        self.__material=material
        self.__tipo=tipo
    def __str__(self):
        return f"Nombre: {self.nombre}, material: {self.__material}, tipo: {self.__tipo}"
    
    #def
    def getnombre(self):
        return self.nombre
    def getmaterial(self):
        return self.__material
    def gettipo (self):
        return self.__tipo
    #set
    def setnombre(self,nuevo):
        self.nombre=nuevo
    def setmaterial(self,nuevo):
        self.__material=nuevo
    def settipo(self,nuevo):
        self.__tipo=nuevo

violin=Instrumento("violin","madera","cuerda")
print("instrumento",violin)

violin.material="vidrio"
print(violin.material)