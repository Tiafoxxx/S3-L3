import math
import sys

def perimetro_quadrato():
    print("Inserisci la misura del lato:")
    lato = float(input(">"))
    risultato = lato * 4
    if (lato <= 0):
        print("Lato uguale a 0? Mi prendi in giro?! Sono IL CALCOLATORE non ho tempo da perdere!")
    else:
        print(f"Il perimetro del quadrato è {risultato}")


def perimetro_rettangolo():
    print("Inserisci la misura della base:")
    base = float(input(">"))
    print("Inserisci la misura dell' altezza:")
    altezza = float(input(">"))
    risultato = (base + altezza) * 2
    if (base <= 0):
        print("Base uguale a 0? Mi prendi in giro?! Sono IL CALCOLATORE non ho tempo da perdere!")
    elif(altezza <= 0):
        print(" Altezza uguale a 0? Mi prendi in giro? Sono IL CALCOLATORE non ho tempo da perdere!")
    else:
        print(f"Il perimetro del quadrato è {risultato}")


def circonferenza():
    print("Inserisci la misura del raggio:")
    raggio = float(input(">"))
    risultato = raggio * math.pi * 2
    if (raggio <= 0):
        print("Raggio uguale a 0? Mi prendi in giro? Sono IL CALCOLATORE non ho tempo da perdere!")
    else:
        print(f"La circonferenza del cerchio è {risultato}")
