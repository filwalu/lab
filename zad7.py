#lab4zad5
# import random
# punkty=[round(random.uniform(0,50),2)for i in range (15)]
#
# print(punkty)
#
# print(f"Najwiecej punktów: {max(punkty)}, najmniej zdobytych punktów: {min(punkty)}")
# liczba = float(input("Podaj liczbe punktow: "))
# print (punkty.index(liczba))
# if liczba in punkty:
#  print(punkty.index(liczba))
# else:
#  print("Liczba nie występuje w liscie punkty: ")
# suma=sum(punkty)
# średnia = round(suma/len(punkty),2)
# print("Średnie punkty: ", średnia)
#
# powyżej=[]
# for p in punkty:
#  if p>średnia:
#   powyżej.append(p)
#   print(powyżej)
#
# poniżej=[p for p in punkty if p < średnia]
# print(poniżej, len)

import random
punkty = [round(random.uniform(0,50),2) for i in range(15)]
print(punkty)
print(f"Najwięcej zdobytych punktów: {max(punkty)}, najmniej zdobytych punktów: {min(punkty)}")
liczba = float(input("Podaj liczbę punktów : "))
print(punkty.index(liczba))
if liczba in punkty:
    print(punkty.index(liczba))
else:
    print("Liczba nie występuje w liście PUNKTY")
suma = sum(punkty)
srednia = suma/len(punkty)
print(f"Średnia punktów: {srednia}")

lista1 =[]
for p in punkty:
    if p > średnia:
        lista1.append(p)
print(lista1, len(lista1))
lista2 =[p for p in punkty if p < średnia]
print(lista2, len(lista2))
