import logging
logging.basicConfig(level=logging.DEBUG)

def suma():
    x_liczby = input("Podaj liczby oddzielone przecinkami bez używania spacji: ")
    x = x_liczby.split(',')
    z = float(x)
    result = 0
    for items in z:
        result = result + items
    logging.info(f"Dodaję liczby z {x}")
    logging.info(f"Wynik to {result}")
def roznica():
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    result = a - b
    logging.info(f"Odejmuję {a} i {b}")
    logging.info(f"Wynik to {result}")
def iloczyn():
    x_liczby = input("Podaj liczby oddzielone przecinkami bez używania spacji: ")
    x = x_liczby.split(',')
    z = float(x)
    result = 1
    for items in z:
        result = result * items
    logging.info(f"Mnożę liczby z {x}")
    logging.info(f"Wynik to {result}")
def iloraz():
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    result = a / b
    logging.info(f"Dzielę {a} i {b}")
    logging.info(f"Wynik to {result}")

if __name__ == "__main__":
    oblicz = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))