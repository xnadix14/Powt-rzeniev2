#Co wypisuje print? - cokolwiek

#a) zamienną
'''x = 'Teodor'
print(x)

#b) tekst
print('informatyka')

#c) wyniki działań
print(2 * (6 +3) / 7)

#d) zaawansowane typy
lista1 = ['x', 6, 'słoń', 12, 9.6]
print(lista1)

#e coś
print(True)

#f) komunikaty złożone
imie = 'Janusz'
wiek = 45
nazwisko = 'Kowal'

print(imie + '\t' + nazwisko + '\tma\t ' + str(wiek) + ' lat ')

print('{0} {1}\n\t ma lat\n\t\t {2}'.format( imie, nazwisko, wiek ))

#\n - przejście do nowej linii
#\t - tabulator'''





#if

wiek= int(input('podaj wiek'))

if wiek <= 24:
    print('ucz się ucz')
elif wiek > 24 and wiek < 65:
    print('do roboty!')
else:
    print('miłej emerytury')