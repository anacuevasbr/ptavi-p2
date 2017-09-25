#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo

class CalculadoraHija(calcoo.Calculadora):

    def multiplica(self):
        return self.valor1 * self.valor2

    def divide(self):
        try:
            return self.valor1 / self.valor2
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")

if __name__== "__main__":

    if len(sys.argv) != 4:
        sys.exit("Input: python3 calc.py operando1 operador operando2")

    operador = sys.argv[2]
    try:
        Operar = CalculadoraHija(float(sys.argv[1]), float(sys.argv[3]))

    except ValueError:
        sys.exit("Los operandos tienen que ser números")

    if operador=="suma":
        print(Operar.suma())

    elif operador=="resta":
        print(Operar.resta())

    elif operador=="multiplica":
        print(Operar.multiplica())

    elif operador=="divide":
        print(Operar.divide())
    else:
        print("Las operaciones disponibles son suma, resta, multiplica y divide")

