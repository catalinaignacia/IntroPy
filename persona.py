#!/usr/bin/python3

class Persona:
    """ Clase que representa a una Persona 
    en Chile!
    self -> rol similar al this de Java
    El constructor se llama siempre
    (double underscore) init (doble undercore)
    Todas las operaciones de la clase reciben
    al self como primer parametro!!!
    """

    def __init__(self, nombre, rut):
        self._nombre = nombre
        self.rut = rut
    
    def imprimir(self):
        texto = " ".join(["soy", self._nombre, ", mi rut es", self.rut])
        print(texto)

