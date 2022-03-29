from logica.instrumento import Instrumento
from logica.guitarra import Guitarra
from logica.piano import Piano
from logica.tiple import Tiple

class Afinador():
    def __init__(self, musico):
        self.musico = musico
        self.instrumento = musico.instrumento

    def tocar(self):
        self.instrumento.afinar()