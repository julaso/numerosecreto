#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def main ():
    secret = random.randint(1,30)


    while True:
        adivina = int(raw_input("Adivina el numero secreto entre 1 y 30): "))

        if adivina == secret:
            print "enhorabuena acertaste el numero secreto %s" % secret
            break

        elif adivina > secret:
            print "Prueba un numero mas bajo"
        elif adivina < secret:
            print "Prueba un numero mas alto"

if __name__ == "__main__": #Python solo ejecuta la funcion de abajo
    main()