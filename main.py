#zad 1
#Napisz pierwszy skrypt, w którym zadeklarujesz po dwie zmienne każdego typu a następnie wyświetl te zmienne

napis = 'zadanie pierwsze'
print(napis)

liczba_calkowita = 4
print(liczba_calkowita)

liczba_rzeczywista = 2.5
print(liczba_rzeczywista)

#zad 2
#Stwórz skrypt kalkulator, w którym wykorzystać wszystkie podstawowe działania arytmetyczne
# #zad2
# pierwsza_liczba = input("Podaj pierwszą liczbę: ")
# znak = input("Podaj znak działania: ")
# druga_liczba = input("Podaj drugą liczbę: ")
#
#
# if znak == "+":
#     suma = int(pierwsza_liczba) + int(druga_liczba)
#     print(suma)
# elif znak == "-":
#     roznica = int(pierwsza_liczba) - int(druga_liczba)
#     print(roznica)
# elif znak == "*":
#     iloczyn = int(pierwsza_liczba) * int(druga_liczba)
#     print(iloczyn)
# elif znak == "/":
#     iloraz = int(pierwsza_liczba) / int(druga_liczba)
#     print(iloraz)
# else:
#     print("error")

#zad 3
#Napis skrypt, w którym stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %
a = 1; b = 3; c = 6; d = 8; e = 4

a+=1
print(a)

b*=2
print(b)

c/=2
print(c)

d**=2
print(d)

e%=2
print(e)

#zad 4
# Napisz skrypt, który policzy i wyświetli następujące wyrażenia:

a = exp(10)

print(a)
sinus = sin(8)**2
logarytm = log(5 + sinus) ** (1/6)
# b = pow(logarytm, 1/6)
print(logarytm)

c = floor(3.55)
print(c)
d = ceil(4.8)
print(d)

#Zad.5 Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie wielkimi literami.
# Użyj odpowiedniej metody by wyświetlić je pisane tak, że pierwsza litera jest wielka a poszostałe małe.
# (trzeba użyć metody capitalize

imie = "patryk"
nazwisko = "mucharski"
print(imie.capitalize())
print(nazwisko.capitalize())

#Zad.6 Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z powtarzającymi
# się słowami np. „la la la”. Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”.
# (trzeba użyć metody count)

napis = ('la la la la la')
print(napis.count('la))'
#zad.7

napis1 = 'tekst do sprawdzenia'
print(napis1[1], napis1[len(napis1)-1])
#zad.8

print(napis.split())
#Zad.9 Napisz skrypt, w którym zadeklarujesz zmienne typu:
# string, float i szestnastkowe. Następnie wyświetl je wykorzystując odpowiednie formatowanie.

napis2 = "Jest dziś poniedziałek"
print("Jaki mamy dziś dzień? %s " %  (napis2))
liczba = 5.677
print("twoja liczba to: %(z1)f" % {'z1': liczba})
liczba_szesnastkowo = 0xf351
print(liczba_szesnastkowo)
print("%x" % (liczba_szesnastkowo))
