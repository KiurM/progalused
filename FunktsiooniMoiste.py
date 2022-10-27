"""Ülesanne: Funktsiooni mõiste"""

import math
from math import sqrt

def print_helloworld():
    print("Hello")

def get_hello():
    return print_helloworld()
#
def ask_name_and_greet_user():
    nimi = input("Sisesta nimi: ")
    cap_name = nimi.capitalize()
    if cap_name == "Thanos":
        print("Get out of here Thanos!!!")
    else:
        print("Hi, " + cap_name + ". Would you like a hamburger.")

ask_name_and_greet_user()

print(" ")

# ülesanne 2

def calculate_hypotenuse_length():
    kaatet1 = input("Sisesta 1. kaateti pikkus: ")
    kaatet2 = input("Sisesta 2. kaateti pikkus: ")
    kaatet1 = int(kaatet1)
    kaatet2 = int(kaatet2)

    hupotenuus = math.sqrt((kaatet1 ** 2) + (kaatet2 ** 2))

    hupotenuus = float(hupotenuus)
    print(hupotenuus)

calculate_hypotenuse_length()

print(" ")

# Teise kaateti leidmine ühe kaateti ja hüpotenuusi abil

def calculate_cathetus_length():
    uuskaatet1 = input("Sisesta 1. kaateti pikkus: ")
    uushupotenuus = input("Sisesta kolmnurga hüpotenuusi pikkus: ")
    uuskaatet1 = int(uuskaatet1)
    uushupotenuus = int(uushupotenuus)

    uuskaatet2 = math.sqrt((uushupotenuus ** 2) - (uuskaatet1 ** 2))
    uuskaatet2 = float(uuskaatet2)

    print("Teise kaateti pikkus on: " + str(uuskaatet2))

calculate_cathetus_length()
