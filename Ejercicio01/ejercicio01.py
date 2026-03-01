#ejercicio1
class Anime:
    def __init__(self,nombre,genero,nroEpisodios,):
        self.nombre=nombre
        self.genero=genero
        self.__nroEpisodios=nroEpisodios
        self.__episodios=[]

    def __str__(self):
        return f"anime: {self.nombre} , genero: {self.genero} , episodios: {self.__nroEpisodios}"
class Main:
        
        A = Anime("Gachiakuta", "Accion", 24)
        print(A)
        #recomendado buen anime y ya se confirmo 2 temporada (づ｡◕‿‿◕｡)づ

        B = Anime("Overlord", "Isekai", 52)
        print(B)
