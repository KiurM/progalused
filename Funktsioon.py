"""Ülesanne: Funktsioon."""


def func():
    print("I´m inside the function")


func()


def my_name_is(name):
    print(f"My name is {name}")


my_name_is("Emili")


def sum_six(num: int):
    num = num + 6
    return num


sum_six(6)


def sum_numbers(a, b):
    return (int(a) + int(b))


print(sum_numbers(15, 5))


def usd_to_eur(usd: int):
    return((usd) - ((usd) / 100 * 20)) 


print(usd_to_eur(100))
