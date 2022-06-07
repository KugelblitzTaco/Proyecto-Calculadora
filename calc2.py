import math
import re

def suma(comandos):
    patron = re.compile("\(\+\s[0-9]+\s[0-9]+\)")
    expresiones = re.findall("\d+", comandos)
    result = 0
    if patron.search(comandos):
        for i in range(0, len(expresiones)):
            result += int(expresiones[i])
    print(expresiones)
    return result

def rest(comandos):
    patron = re.compile("\(\-\s[0-9]+\s[0-9]+\)")
    expresiones = re.findall("\d+", comandos)
    result = 0
    if patron.search(comandos):
        for i in range(0, len(expresiones)):
            result += int(expresiones[i])
    print(expresiones)
    return result

def main():
    comandos = str(input("calculadora >> "))

    # comandos ingresados se ingresen como argumentos a cada subrutina

    print("respuesta >>", suma(comandos))

    if comandos == "quit":
        print("Saliendo...")
        return
    main()

    return

main()