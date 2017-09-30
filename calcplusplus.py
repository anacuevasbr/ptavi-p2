#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

if __name__== "__main__":

    if len(sys.argv) != 2:
        sys.exit("Input: python3 calcplus.py fichero")


    with open(sys.argv[1], newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
