#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

if __name__== "__main__":

    if len(sys.argv) != 2:
        sys.exit("Input: python3 calcplus.py fichero")


    with open(sys.argv[1], newline='') as f:
        Fich = csv.reader(f)
        for Linea in Fich:
            Operador=Linea[0]
            Total=Linea[1]
            Operandos=Linea[2:]

            for Operando in Operandos:

                try:
                    Operar = calcoohija.CalculadoraHija(float(Total), float(Operando))
                except ValueError:
                    sys.exit("Los operandos tienen que ser números")
                
                if Operador=="suma":
                    Total=Operar.suma()

                elif Operador=="resta":
                    Total=Operar.resta()

                elif Operador=="multiplica":
                    Total=Operar.multiplica()

                elif Operador=="divide":
                    Total=Operar.divide()
                else:
                    print("Las operaciones disponibles son suma, resta, multiplica y divide")

            print(Total)

                
