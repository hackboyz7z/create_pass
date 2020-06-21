
import random

print("           $b  Vb.                             ")
print("           ’$b  V$b.                           ")
print("            $$b  V$$b.                         ")
print("            ’$$b. V$$$$oooooooo.        ..     ")
print("             ’$$P*_V$$$$$****$$$b.   .o$$P     ")
print("              ”_.oooZ$$$$b..o$$$$$$$$$$$$C     ")
print("              .$$$$$$$$$$$$$$$$$$$$$$$$$$$b.   ")
print("              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   ")
print("         .o$$$o$$$$$$$$P***$$$$$$$$$P**”*$$$P  ")
print("        .$$$**$$$$P”q$C    ”$$$b       .$$P    ")
print("        .$$$**$$$$P”q$C    ”$$$b       .$$P    ")
print("       $$P   ”$$$b__”$_._.$$$$$b.      *”      ")
print("       $$     $$$._____”***$$$$$$$b._A.        ")
print("       V$b   ._Z$$b.__._______”*$$$$$b$$:      ")
print("       V$$.  ”*$$$b.__b._________”$$$$$             ")
print("       ”$$b     ”*$.__*b._________”$$$b            ")
print("         ”$$b.     ”L__”$$o.________”*”_____.ooo.. ")
print("           ”*$$o.        ”*$$o.__________.o$$$$$   ")
print("              ”*$$b.       ”$$b._______.$$$$$*”    ")
print("                  ”*$$o.     ”$$$o.____$$$$$’      ")
print("                     ”$$o       ”$$$b.__”$$$$__    ")
print("                       ”$b.      ”$$$$b._”$$$$$    ")
print("                       ._”$$      ”$$$$b__”$$$$    ")
print("                        L.”$.      .$$$$$.__       ")


long = input("longuitud de contraseña deseada ")
cadena= int(long)
minusculas = "abcdefghijklmnñopqrstuvwxyz"
mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros = "1234567890"
simbolos = "#{}%&$¡!*"

all = minusculas + mayusculas + numeros + simbolos 
#longitud = long.srt(long)
#long = 10

password = "".join(random.sample(all, cadena))
print(password) 