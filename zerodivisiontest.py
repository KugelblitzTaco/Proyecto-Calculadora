from decimal import DivisionByZero


def main(): 
    def division(dividendo, divisor):
        try:
            cociente = dividendo / divisor
            return cociente
        except ZeroDivisionError:
            return "Indefinida"
    print(division(5, 0))


main()