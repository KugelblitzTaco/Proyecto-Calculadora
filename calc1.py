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

#2. El resultado de la operacion principal

def operacion(comandos):
    # Check for expresiones
    if suma.search(comandos) or rest.search(comandos) or mult.search(comandos) or divs.search(comandos) or raiz.search(comandos) or cuad.search(comandos) or seno.search(comandos) or coseno.search(comandos) or tangente.search(comandos) or cociente.search(comandos) or residuo.search(comandos) or factorial.search(comandos):
        expresiones = re.findall('\d+', comandos)
        print(expresiones)
    
    expresion = []

    if suma.search(comandos):
        expresion = re.findall('\d+', comandos)
        result = int(expresion[0]) + int(expresion[1])
        print(result)
    if rest.search(comandos):
        expresion = re.findall('\d+', comandos)
        result = int(expresion[0]) - int(expresion[1])
        print(result)    
    if mult.search(comandos):
        expresion = re.findall('\d+', comandos)
        result = int(expresion[0]) * int(expresion[1])
        print(result)
    if divs.search(comandos):
        expresion = re.findall('\d+', comandos)
        result = int(expresion[0]) / int(expresion[1])
        print(result)
    if raiz.search(comandos):
        expresion = re.findall('\d+', comandos)
        result = math.sqrt(int(expresion[0]))
        print(result)
    if cuad.search(comandos):
        expresion = re.findall('\d+', comandos)
        result = math.pow(int(expresion[0]), 2)
        print(result)
    if seno.search(comandos):
        expresion = re.findall('\d+', comandos)
        result = math.sin(math.radians(int(expresion[0]), 2))
        print(result)
    if coseno.search(comandos):
        expresion = re.findall('\d+', comandos)
        result = math.cos(math.radians(int(expresion[0]), 2))
        print(result)
    if tangente.search(comandos):
        expresion = re.findall('\d+', comandos)
        result = math.tan(math.radians(int(expresion[0]), 2))
        print(result)
    if cociente.search(comandos):
        expresion = re.findall('\d+', comandos)
        result = int(expresion[0]) // int(expresion[1])
        print(result)
    if residuo.search(comandos):
        expresion = re.findall('\d+', comandos)
        result = int(expresion[0]) %  int(expresion[1])
        print(result)
    if factorial.search(comandos):
        expresion = re.findall('\d+', comandos)
        result = math.factorial(int(expresion[0]))
        print(result)
        
    
    return expresion

#3. El detector de errores
# Numeros negativos, floats/racionales


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