from logica.instrumento import Instrumento

class Piano(Instrumento):
    def tocar(self):
        print("Tocando piano")
    def afinar(self):
        print("Afinando piano")