#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def main ():
    secret = random.randrange(0,50)
    print "Acabamos de generar el numero secreto"

    while True:
        adivina = int(raw_input("Adivina el numero secreto entre 1 y 50): "))

        if adivina == secret:
            print "enhorabuena acertaste el numero secreto %s" % secret
            break
        elif adivina > secret:
            print "Prueba un numero mas bajo"
        elif adivina < secret:
            print "Prueba un numero mas alto"


    print "Acertaste, Gracias por jugar"

##        again = raw_input("Quieres jugar otra vez? (yes/no) ")
##          if again == "no":
##              break

if __name__ == "__main__":
    main()