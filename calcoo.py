#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora:
    
    def __init__(self, valor1, valor2):
        self.valor1=valor1
        self.valor2=valor2

    def suma(self):
        return self.valor1 + self.valor2


if __name__== "__main__":

    if len(sys.argv) != 4:
        sys.exit("Input: python3 calc.py operando1 operador operando2")

    operador = sys.argv[2]
    try:
        Operar = Calculadora(float(sys.argv[1]), float(sys.argv[3]))

    except ValueError:
        sys.exit("Los operandos tienen que ser números")

    resultado=Operar.suma()
    print(resultado)

    
