class Televisor:
    def __init__(self,marca=None,resolucion=None,tipo=None):
        self.__marca=marca
        self.__resolucion=resolucion
        self.__tipo=tipo

    def __str__(self):
        return f"Marca: {self.__marca}, Resolución: {self.__resolucion}p, Tipo: {self.__tipo}"

print("----------")
tv1 = Televisor("LG", 3840, "LG NanoCell")
print("Televisor", tv1)

print("----------")
tv2=Televisor()
print("Televisor ",tv2)

