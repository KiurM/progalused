# ====================================================================
# Ülesanne 1
# Autor: Kiur Mölder
# Kuupäev: 12.12.2022
# ====================================================================
# Koosta programm, mis aitab lastel treenida liitmist. Programm peaks pakkuma välja juhuslike
# arvudega liitmistehteid ning ootama kasutajalt vastust. Kui vastus on õige, kiitma kasutajat,
# kui aga vale, andma õige vastuse ja esitama uue tehte. Järjest esitatavate tehete hulk võib
# olla programmis ette antud (näiteks 10), samuti võib olla ette antud piirid, kui suuri arve
# kasutajalt küsitakse (näiteks 1 kuni 50). Programm peaks pidama arvestust ka õigete vastuste
# üle ning väljastama pärast viimast tehet tulemuse.
#
# Muutke programmi selliselt, et kasutajalt küsitakse ka teisi tehteid (lahutamine, korrutamine,
# jagamine). Tehte võite küsida kasutajalt või lasta arvutil genereerida erinevad tehted iga
# arvutuse kohta.
#
# Muutke programmi nii, et esitavate arvude piirid saab kasutaja ette anda – nii maksimumi kui
# ka miinimumi.
# ====================================================================

import random

def liitmine():
    from random import randrange
    print("Tere! Mis numbrid valid, mille vahel hakkab arvutus ülesandeid tulema?")
    min = input("Minimaalne number: ")
    max = input("Maksimaalne number: ")
    if int(min) > int(max):
        print("Vabandust, aga minimaalne number peab olema väiksem, kui maksimaalne.")
        return
    rngn = randrange(int(min), int(max))
    rngm = randrange(int(min), int(max))
    print(rngn, "+", rngm, "= ?")
    kasutajainput = input("Mis on vastus: ")
    vastusa = rngn + rngm
    if kasutajainput == str(vastusa):
        print("Tubli! Õige vastus.")
    else:
        print("Vale vastus, õige vastus on ", vastusa)

    return

def lahutamine():
    from random import randrange
    print("Tere! Mis numbrid valid, mille vahel hakkab arvutus ülesandeid tulema?")
    min = input("Minimaalne number: ")
    max = input("Maksimaalne number: ")
    if int(min) > int(max):
        print("Vabandust, aga minimaalne number peab olema väiksem, kui maksimaalne.")
        return
    rngn = randrange(int(min), int(max))
    rngm = randrange(int(min), int(max))
    print(rngn, "-", rngm, "= ?")
    kasutajainput = input("Mis on vastus: ")
    vastusa = rngn - rngm
    if kasutajainput == str(vastusa):
        print("Tubli! Õige vastus.")
    else:
        print("Vale vastus, õige vastus on ", vastusa)

    return


def korrutamine():
    from random import randrange
    print("Tere! Mis numbrid valid, mille vahel hakkab arvutus ülesandeid tulema?")
    min = input("Minimaalne number: ")
    max = input("Maksimaalne number: ")
    if int(min) > int(max):
        print("Vabandust, aga minimaalne number peab olema väiksem, kui maksimaalne.")
        return
    rngn = randrange(int(min), int(max))
    rngm = randrange(int(min), int(max))
    print(rngn, "*", rngm, "= ?")
    kasutajainput = input("Mis on vastus: ")
    vastusa = rngn * rngm
    if kasutajainput == str(vastusa):
        print("Tubli! Õige vastus.")
    else:
        print("Vale vastus, õige vastus on ", vastusa)

    return


def jagamine():
    from random import randrange
    print("Tere! Mis numbrid valid, mille vahel hakkab arvutus ülesandeid tulema?")
    min = input("Minimaalne number: ")
    max = input("Maksimaalne number: ")
    if int(min) > int(max):
        print("Vabandust, aga minimaalne number peab olema väiksem, kui maksimaalne.")
        return
    rngn = randrange(int(min), int(max))
    rngm = randrange(int(min), int(max))
    print(rngn, "/", rngm, "= ?")
    kasutajainput = input("Mis on vastus: ")
    vastusa = rngn / rngm
    if kasutajainput == str(vastusa):
        print("Tubli! Õige vastus.")
    else:
        print("Vale vastus, õige vastus on ", vastusa)

    return


def ulesanne():
    ul_arv = input("Tere! Mitu korda soovite ülesandeid lahendada: ")
    ul = input("Tere! Mis sorti ülesandeid soovite lahendada: ")
    if ul == liitmine:
        for n in range(int(ul_arv)):
            liitmine()
    if ul == lahutamine:
        for n in range(int(ul_arv)):
            lahutamine()
    if ul == korrutamine:
        for n in range(int(ul_arv)):
            korrutamine()
    if ul == jagamine:
        for n in range(int(ul_arv)):
            jagamine()

print(ulesanne())