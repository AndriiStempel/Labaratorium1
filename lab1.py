# 1 Zdanie
a = 1 + 2
print(a, type(a))

b = 1 + 4.5
print(b, type(b))

c = 3 / 2
print(c, type(c))

d = 4 / 2
print(d, type(d))

f = 3 // 2
print(f, type(f))

g = -3 // 2
print(g, type(g))

e = 11 % 2 
print(e, type(e))

h = 2 ** 10
print(h, type(h))

k = 8 ** (1/3)
print(k,type(k))

#Zdanie 1b

print(int(3.0))
print(float(3))
print(float("3"))
print(str(12.4))
print(bool(0))

#Zdanie 2

uczelnia = "Studiuję na WSIiZ"
print(uczelnia)

#Zdanie 3 

imię = 'Jan'
wiek = 20
wzrost = 178

print("Nazywam się", imię,"i mam", wiek, "\nMój wzrost to", wzrost, "cm" )

#Zdanie 4

Cena = 39.99
Rabat = 0.2

Cena_po_rabacie = Cena*(1-Rabat)
print("Cena po rabacie:", Cena_po_rabacie)

#Zdanie 5
print("\n\n\n\n")
długośc_piersza = float(input("Wprowadź pierwszy bok prostokąta: "))
długośc_druga = float(input("Wprowadź drugej bok prostokąta: "))
pole =  długośc_piersza * długośc_druga
obwod = 2 * (długośc_piersza + długośc_druga)

print("Pole: ", pole,"\n obwod: ", obwod )

#Zdanie 6
import random
dystans = random.randint(1,100000)
cena_paliwa = float(input("Podaj aktualną cenę paliwa za litr: "))
spalanie = float(input("Podaj średnie spalenie paliwa(litry na 100km: "))

zyzycie_paliwa = dystans = (spalanie / 100)
koszt_podrozy = zyzycie_paliwa + cena_paliwa

print("Przewidywane zużycie paliwa w litrach: ", zyzycie_paliwa)
print("Szacowany koszt podróży w zl: ", koszt_podrozy)

#Zdanie 7 

print("\n\nRózwazanie równiania: ax+b=0")

a = float(input("Wprowadż a:" ))
b = float(input("Wprowadż b:" ))

if a == 0:
    if b == 0:
        print('Równanie tożsamościowe')
    else:
        print('Równanie sprzeczne')
else:
    x = -b/a
    print('x =', x)

#Zdanie 8
print("Rozwianzanie ax2+bx+c=0")
import math

a = float(input("Podaj wartość a: "))
b = float(input("Podaj wartość b: "))
c = float(input("Podaj wartość c: "))

delta = b**2 - 4*a*c
print("Delta= ",delta)

if delta > 0:
    # Dla delta > 0
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print("Równanie ma dwa rozwiązania: x1= ", x1, "x2= ", x2)
elif delta == 0:
    # Dla delta = 0
    x = -b / (2 * a)
    print("Równanie ma jedno rozwiązanie: x = ",x)
else:
    # Dla delta < 0
    print("Równanie nie ma rozwiązań w zbiorze liczb rzeczywistych.")


print("\n\n\n")
#Zadanie 9

number_pierszyj = float(input("Wprowadź pierwszą liczbę: "))
number_drugij = float(input("Wprowadź drugą liczbę: "))
sign = input("Wprowadź znak: +, -, *, /, **2: ")

if sign == '+' :
    result = number_pierszyj + number_drugij
    print("Wynik: ", str(result))
elif sign == '-' :
    result = number_pierszyj - number_drugij
    print("Wynik: ", str(result))
elif sign == '*' :
    result = number_pierszyj * number_drugij
    print("Wynik: ", str(result))
elif sign == '/' :
    result = number_pierszyj / number_drugij
    print("Wynik: ", str(result))
elif sign == '**2' :
    result1 = number_pierszyj **2
    result2 = number_drugij **2
    print("Wynik: ", str(result1))
    print("Wynik: ", str(result2))
else:
    print("Wprowadzono zły znak")










  

 
       
