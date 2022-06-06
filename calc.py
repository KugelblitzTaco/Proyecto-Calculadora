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

    if suma.search(comandos):
        result = int(expresion[-2]) + int(expresion[-1])
        newString += re.sub(suma, str(result), comandos, 1)
        print(newString)
        operacion(newString)
    if rest.search(comandos):
        result = int(expresion[-2]) - int(expresion[-1])
        newString += re.sub(rest, str(result), comandos, 1)
        print(newString)
        operacion(newString)
    if mult.search(comandos):
        result = int(expresion[-2]) * int(expresion[-1])
        newString += re.sub(mult, str(result), comandos, 1)
        print(newString)
        operacion(newString)
    if divs.search(comandos):
        result = int(expresion[-2]) / int(expresion[-1])
        newString += re.sub(divs, str(result), comandos, 1)
        print(newString)
        operacion(newString)
    if cociente.search(comandos):
        result = int(expresion[-2]) // int(expresion[-1])
        newString += re.sub(cociente, str(result), comandos, 1)
        print(newString)
        operacion(newString)
    if residuo.search(comandos):
        result = int(expresion[-2]) % int(expresion[-1])
        newString += re.sub(residuo, str(result), comandos, 1)
        print(newString)
        operacion(newString)
    if raiz.search(comandos):
        result = math.sqrt(int(expresion[-1]))
        newString += re.sub(raiz, str(result), comandos, 1)
        print(newString)
        operacion(newString)
    if cuad.search(comandos):
        result = math.pow(int(expresion[-1]), 2)
        newString += re.sub(cuad, str(result), comandos, 1)
        print(newString)
        operacion(newString)
    if seno.search(comandos):
        result = math.sin(math.radians(int(expresion[-1])))
        newString += re.sub(seno, str(result), comandos, 1)
        print(newString)
        operacion(newString)
    if coseno.search(comandos):
        result = math.cos(math.radians(int(expresion[-1])))
        newString += re.sub(coseno, str(result), comandos, 1)
        print(newString)
        operacion(newString)
    if tangente.search(comandos):
        result = math.tan(math.radians(int(expresion[-1])))
        newString += re.sub(tangente, str(result), comandos, 1)
        print(newString)
        operacion(newString)
    if factorial.search(comandos):
        result = math.factorial(int(expresion[-1]))
        newString += re.sub(factorial, str(result), comandos, 1)
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