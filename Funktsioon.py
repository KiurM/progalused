"""Ülesanne: Funktsioon"""

# Ülesanne 1

def func():
    print("I´m inside the function")

func()

# Ülesanne 2

def my_name_is(name):
    print(f"My name is {name}")

my_name_is("Emili")

# Ülesanne 3

def sum_six(num):
    num = print(int(num) + int(6))
    return num
sum_six(int(6))

# Ülesanne 4

def  sum_numbers(a, b):
    return (int(a) + int(b))

print(sum_numbers(15, 5))

# Ülesanne 5

def usd_to_eur(usd):
    return(int(usd) - (int(usd) / 100 * 20))

print(usd_to_eur(10))
