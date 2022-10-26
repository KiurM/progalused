"""mata avaldised, 14 ülesannet"""
import math
from typing import re

num_a = 4
num_b = 6
riba = "-----------------------------------------------------------------------"

sum = num_a + num_b
#print(sum)
print(f"{num_a} + {num_b} = {sum}")
print(riba)

# 1

difference = num_a - num_b
#print(difference)
print(f"{num_a} - {num_b} = {difference}")
print(riba)

#

division = num_a / num_b
#print(division)
print(f"{num_a} / {num_b} = {division}")
print(riba)

# 1

division2 = (num_a // num_b)
#print(division2)
print(f"{num_a} // {num_b} = {division2}")
print(riba)

# 2

multiply_numbers = num_a * num_b
#print(multiply_numbers)
print(f"{num_a} * {num_b} = {multiply_numbers}")
print(riba)

# 3

power = num_a ** num_b
print(f"{num_a} ** {num_b} = {power}")
print(riba)

# 4

remainder = num_a % num_b
#print(remainder)
print(f"{num_a} % {num_b} = {remainder}")
print(riba)

# 5

avarage = (num_a + num_b) / 2
print(f"({num_a} + {num_b}) / 2 = {avarage}")
print(riba)

# 6

radius = 5
circle_area = (radius ** 2) * math.pi
#print(circle_area)
#answer = str(round(answer, 2))
print(f"({radius} ** 2) * {math.pi} = {round(circle_area, 2)}")
print(riba)

# 7

side_lenght = 3
kõrgus1 = (side_lenght ** 2 + (side_lenght / 2) ** 2)
#print(kõrgus1)
kõrgus2 = math.sqrt(kõrgus1)
#print(kõrgus2)
triangle_area = round((kõrgus2 * side_lenght) / 2)
#print(triangle_area)
print(f"({math.sqrt(side_lenght ** 2 + (side_lenght / 2) ** 2)} * {side_lenght}) / 2 = {triangle_area}")
print(riba)

# triangle_area = (math.sqrt(3) / 4) * side_lenght ** 2
# triangle_area = round(triangle_area)
# print(f"Triangle area is {triangle_area} if side lenght is {side_lenght}")

# 8

#discriminant = b² - 4ac
dis_a = 2
dis_b = 3
dis_c = 4
discriminant = (dis_b ** 2) - 4 * dis_a * dis_c
print(f"({dis_b} ** 2) - 4 * {dis_a} * {dis_c} = {discriminant}")
print(riba)

##Loo muutuja c, mille väärtuseks on kahe kaateti pikkuste a ja b abil arvutatud hüpotenuusi pikkus.
#Hüpotenuusi pikkus võib olla ujukoma arv, kaatetite pikkused on alati positiivsed täisarvud.

# 9

#Meeldetuletus: Pythagorase teoreemist a² + b² = c².

kaatet_a = 4
kaatet_b = 7
hupotenuus_c = math.sqrt(kaatet_a ** 2 + kaatet_b ** 2)
#print (float(hupotenuus_c))
print(f"math.sqrt({kaatet_a} ** 2 + {kaatet_b} ** 2) = {hupotenuus_c}")
print(riba)

# 10

hupotenuus_c2 = 14.4
kaatet_a2 = 6
kaatet_b2 = math.sqrt(hupotenuus_c2 ** 2 - kaatet_a2 ** 2)
print(f"math.sqrt({hupotenuus_c2} ** 2 - {kaatet_a2} ** 2) = {kaatet_b2}")
print(riba)

# 11

seconds = 163
minutes = seconds // 60, seconds % 60
print(minutes)
print(riba)

# 12. Student helper

angle = 35
sine = (math.sin(math.pi / angle))
cosine = (math.cos(math.pi * angle))
print(round(sine, 1))
print(round(cosine, 1))
print(riba)

# 13. Greetings

n = 5
lots_of_heys = n * "Hey"
print(lots_of_heys)
print(riba)

# 14. Adding numbers

num_a = 123
num_b = 431
string_numbers = str(num_a) + str(num_b)
print(string_numbers)
print(riba)
