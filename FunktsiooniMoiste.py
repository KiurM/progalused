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

def calculate_hypotenuse_length(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

func_result = calculate_hypotenuse_length(5, 4)
print(func_result)


print(" ")

# Teise kaateti leidmine ühe kaateti ja hüpotenuusi abil

def calculate_cathetus_length(a: int, b: int):
    c = math.sqrt(a**2 - b**2)
    return c

    print(float(c))

print(calculate_cathetus_length(6.4, 4))
