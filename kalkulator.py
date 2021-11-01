import logging 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

def kalk(oblicz, a, b):
    if oblicz == 1:
        suma = a + b
    elif oblicz == 2:
        roznica = a - b
    elif oblicz == 3:
        iloczyn = a * b
    else:
        iloraz = a / b

if __name__ == "__main__":
    oblicz = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    a = input("Podaj pierwszą liczbę: ")
    b = input("Podaj drugą liczbę: ")
    kalk(oblicz, a, b)