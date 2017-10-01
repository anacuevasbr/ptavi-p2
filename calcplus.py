#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Input: python3 calcplus.py fichero")

    fich = open(sys.argv[1], "r")
    lineas = fich.readlines()

    for linea in lineas:
        operador = linea[:linea.find(',')]
        linea = linea[linea.find(',')+1:-1]
        Operandos = []

        while (',' in linea) == 1:
            Operandos.append(linea[:linea.find(',')])
            linea = linea[linea.find(',')+1:]
        Operandos.append(linea)

        Total = Operandos[0]
        Operandos = Operandos[1:]

        for Operando in Operandos:

            try:
                Operar = calcoohija.CalculadoraHija(float(Total),
                                                    float(Operando))
            except ValueError:
                sys.exit("Los operandos tienen que ser números")

            if operador == "suma":
                Total = Operar.suma()

            elif operador == "resta":
                Total = Operar.resta()

            elif operador == "multiplica":
                Total = Operar.multiplica()

            elif operador == "divide":
                Total = Operar.divide()
            else:
                print("operaciones: suma, resta, multiplica y divide")

        print(Total)
