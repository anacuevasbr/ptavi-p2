#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__== "__main__":

    if len(sys.argv) != 2:
        sys.exit("Input: python3 calcplus.py fichero")

    
    fich=open(sys.argv[1],"r")
    lineas=fich.readlines()
    
    for linea in lineas:
        Operacion=linea[:linea.find(',')]
        linea=linea[linea.find(',')+1:-1]
        Operandos=[]
        
        while (',' in linea)==1:
            Operandos.append(linea[:linea.find(',')])
            linea=linea[linea.find(',')+1:]
        Operandos.append(linea)
        print(Operandos)   

