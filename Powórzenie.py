#1 Wczytywanie danych od użytkownika:

'''x = input('Podaj liczbę')

#a) zatrzymanie się
#b) wyświetla komunikat 'Podaj liczbę'
#c) czeka na to co poda użytkownik
#d) to co poda użytkownik trafi do zmiennej x - jako TEKST

print(type(x)) #pokazujemy jakiego typu jest dana w zmiennej x

#2 Jak wczytać inną daną niż tekst

y = input('Podaj liczbę')
z = int(y) #zmienna y zostaje zamieniona na typ int i zapisana w zmiennej z

print(type(y)) #y to tekst
print(type(z)) #z to liczba

#3 Jak wczytać inną daną niż tekst - wersja krótsza
y = int(input('Podaj liczbę'))'''

#4 Jak wczytać inną daną niż tekst - przykład z float
y = float(input('Podaj liczbę'))
print(type(y))