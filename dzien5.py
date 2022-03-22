#pętle 

for i in range(5): #zaczyna od i=0 koczy na i=4
    print(i)
    if(i == 3):
        print("mamy trzy!")
    elif (i == 4):
        print("koniec pętli!")
    else:
        print(" ")#w przeciwnym wypadku pusta 

cyfra = 9
while (cyfra >= 1):
    print("Cyfra = ", cyfra)
    cyfra-=1     #trzeba zmienić zmienną cyfra - w przeciwnym wypadku pętla while
                 #nigdy nie przestanie działać
                 #aby przerwać program możemy w koncoli nacisnąć Ctrl + c !

imiona = ['Adam', 'Beata', 'Celina', 'Damian']
liczba_iteracji = 0
for imie in imiona:
    print(imie)
    liczba_iteracji+=1
print("liczba iteracji: ", liczba_iteracji)

zbior_A = [1, 1, 2, 3, 5, 8, 13]
suma = 0

for liczba in zbior_A:
    suma += liczba
print('Suma liczb ze zbioru A to: ', suma)
