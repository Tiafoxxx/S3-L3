import Formule
import math
import sys

def menu():
    print ("""Scegli la figura:
           1. QUADRATO
           2. RETTANGOLO
           3. CERCHIO""")
    scelta1 = int (input(">"))
    if (scelta1 == 1):
        Formule.perimetro_quadrato()
    elif (scelta1 == 2):
        Formule.perimetro_rettangolo()
    elif (scelta1 == 3):
        Formule.circonferenza()
    else:
        print("VATTENE STUPIDO UMANO!!!")
        sys.exit()



print ("""\t\t\t\tCiao sono IL CALCOLATORE, 
       Sono in grado solo di calcolare il perimetro di alcune figure ma sono comunque potentissimo.""")
print ("Hai bisogno?\n1. SI'\n2.NO")
scelta0 = int (input(">"))
if (scelta0 == 1):
    print("INIZIAMO!")
    menu()

elif (scelta0 == 2):
    print ("ALLA PROSSIMA!")
    sys.exit()
    
else:
    print("VATTENE STUPIDO UMANO!!!")
    sys.exit()

