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
a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))

dodawanie = a+b
print(dodawanie)

odejmowanie = b-a
print(odejmowanie)

mnozenie = a*b
print(mnozenie)

dzielenie = b/a
print(dzielenie)

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
pow(e, 10)

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

piosenka = ('la la la la la');
print 'ilosc la w piosence : ', piosenka.count('la)';

#Zad.9 Napisz skrypt, w którym zadeklarujesz zmienne typu:
# string, float i szestnastkowe. Następnie wyświetl je wykorzystując odpowiednie formatowanie.
string = 'Hello'
print(_type(string))

float = 2.5
print(_type(float))

hex = A1
print(_type(hex))
