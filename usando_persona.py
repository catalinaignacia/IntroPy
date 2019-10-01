#!/usr/bin/python3

from persona import Persona


perrin = Persona("Kang Daniel", "18077087-7")
perrin.imprimir()

perrin.rut = "19100102-6"
perrin.imprimir()

# perrin._nombre = "juan lopez" -> esto no se hace!

nombre = input("ingrese su nombre:")
rut = input("ingrese su rut:")
persona_nueva = Persona(nombre, rut)
persona_nueva.imprimir()