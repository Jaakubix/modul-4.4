import logging 
logging.basicConfig(level=logging.DEBUG)

def kalk(oblicz, a, b):
    if oblicz == 1:
        suma = a + b
        logging.info(f"Dodaję {a} i {b}")
        logging.info(f"Wynik to {suma}")
    elif oblicz == 2:
        roznica = a - b
        logging.info(f"Odejmuję {a} i {b}")
        logging.info(f"Wynik to {roznica}")
    elif oblicz == 3:
        iloczyn = a * b
        logging.info(f"Mnożę {a} i {b}")
        logging.info(f"Wynik to {iloczyn}")
    elif oblicz == 4:
        iloraz = a / b
        logging.info(f"Dzielę {a} i {b}")
        logging.info(f"Wynik to {iloraz}")
    else:
        exit(1)

if __name__ == "__main__":
    oblicz = float(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    kalk(oblicz, a, b)