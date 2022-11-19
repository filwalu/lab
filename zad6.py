import random
n = int(input('Podaj ilość liczb na liscie: '))
zestaw1 = []
for i in range (n):
    k = random.randint(1, 10)
    zestaw1.append(k)
print(zestaw1)

n = int(input('Podaj ilość liczb na liscie: '))
zestaw2= [random.randint(5, 15) for i in range (n)]
print(zestaw2)

x=int(input('Podaj liczbę: '))
if x in zestaw1 and zestaw2:
    print ("liczba  z obydwu zestawów")
elif  x in zestaw2:
    print("Liczba  z zestawu 2")
elif x in zestaw1:
    print ("liczba z zestawu 1")
else:
    print("nie ma tej liczby  w obu zestawach")

zestaw12= zestaw1+zestaw2
zestaw12.sort()
print()
print(zestaw12)
