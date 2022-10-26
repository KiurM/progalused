"""Ülesanne: Kasutaja sisend ja arvutused"""

nimi = input("Sisestage oma nimi: ")
lubatud = input("Sisestage lubatud kiirus (km/h): ")
tegelik = input("Sisestage tegelik kiirus (km/h): ")

lubatud = int(lubatud)
tegelik = int(tegelik)

esialgne_tulemus = (tegelik - lubatud) * 3

trahv = min(190, esialgne_tulemus)

trahv = str(round(trahv))

print(nimi + ", kiiruse ületamise eest on teie trahv " + trahv)
