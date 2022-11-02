"""Tingimuslause (if-statement)"""

# Ül 1

def are_equal(num_a: int, num_b: int) -> str:
    if (num_a == num_b):
        return "equal"
    else:
        return "not equal"

print(are_equal(4, 4))
print(are_equal(4, 5))

print(" ")

# Ül 2

def positive_or_negative(num_a: int) -> str:
    if (num_a == 0):
       return "zero"
    if (num_a > 0):
        return "positive"
    else:
        return "negative"

print(positive_or_negative(-5))
print(positive_or_negative(0))
print(positive_or_negative(4))

print(" ")

# Ül 3

def is_in_string(letter: str, word: str) -> bool:
    if str(letter) in (word):
        return "True"
    else:
        return "False"

print(is_in_string("a", "car"))
print(is_in_string("o", "car"))

print(" ")

# Ül 4

def are_same_length(str_a: str, str_b: str) -> bool:
    if len(str_a) == len(str_b):
        return "True"
    else:
        return "False"

print(are_same_length("aaa", "foa"))
print(are_same_length("aa", "rga"))

print(" ")

# Ül 5

def is_letter_or_digit(symbol: str) -> str:
    if type(symbol) == str:
        return "letter"
    if type(symbol) == int:
        return "digit"
    else:
        return "other"

print(is_letter_or_digit("j"))
print(is_letter_or_digit(6))
print(is_letter_or_digit(6.7))

print(" ")

# Ül 6

def are_last_symbols_same(str_a: str, str_b: str) -> bool:
    if str_a[-1] == str_b[-1]:
        return "true"
    else:
        return "false"

print(are_last_symbols_same("tere", "ekfegaole"))
print(are_last_symbols_same("tere", "ekffff"))

print(" ")

# Ül 7

def hundred(num_a: int) -> int:
    if num_a > int(100):
        return print(num_a % 100)
    if num_a < int(100):
        return print(100 - num_a)

hundred(110)
hundred(45)
