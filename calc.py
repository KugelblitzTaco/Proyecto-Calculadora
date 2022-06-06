import re
import math
import os

#   El codigo se divide en tres partes:
#1. El analisis de sintaxis usando regex

##  Detectar cada digito como int para operar 
suma = re.compile(r"\(\+\s[0-9]+\s[0-9]+\)")
rest = re.compile(r"\(\-\s[0-9]+\s[0-9]+\)")
mult = re.compile(r"\(\*\s[0-9]+\s[0-9]+\)")
divs = re.compile(r"\(\/\s[0-9]+\s[0-9]+\)")
raiz = re.compile(r"\(sqroot\s[0-9]+\)")
cuad = re.compile(r"\(sqr\s[0-9]+\)")
seno = re.compile(r"\(sen\s[0-9]+\)")
coseno = re.compile(r"\(cos\s[0-9]+\)")
tangente = re.compile(r"\(tan\s[0-9]+\)")
cociente = re.compile(r"\(div\s[0-9]+\s[0-9]+\)")
residuo = re.compile(r"\(%\s[0-9]+\s[0-9]+\)")
factorial = re.compile(r"\(fact!\s[0-9]+\)")

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

#input: string; output: comandos
def operacion(comandos):
    expresion = re.findall('\d+', comandos)
    newString = ''
    found = ''
    if suma.search(comandos):
        result = int(expresion[-1]) + int(expresion[-2])
        newString += re.sub(suma, str(result), comandos, 1)
        print(newString)
        operacion(newString)


    print(expresion)
    return newString

def main():
    comandos = input("calculadora >> ")
    operacion(comandos)

    clear = lambda: os.system("cls")

    if comandos == "clear":
        clear()
    if comandos == "quit":
        print("Saliendo...")
    else:
        main()  
    return
     
main()    