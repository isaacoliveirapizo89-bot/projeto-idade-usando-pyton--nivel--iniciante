import time
import sys

armamento = "peça"
objeto = "cinta"

gang = ["G-Hard", "koda", "Nagalli", "Honaiser", "toledo"]

print("Toc toc na porta, chegou sua visita")
time.sleep(1.5)

for i in gang:
    frase = f"ja pensou se é o {i} com a {armamento} na {objeto}?"

    for char in frase:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

    print()
    time.sleep(0.5)

final = f"\nJá pensou se uma {objeto} com uma {armamento} entoca"

for char in final:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

print ("\n")