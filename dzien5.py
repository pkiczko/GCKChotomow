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

#ze strony https://github.com/Asabeneh/30-Days-Of-Python/blob/master/10_Day_Loops/10_loops.md
person = {      
    'first_name':'Asabeneh',    #biblioteka(dictionary) zawiera zestawy klucz:wartość
    'last_name':'Yetayeh',      #wartość może też być zbiorem, biblioteką etc.
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items(): #dzięki tej operacji wyciągniemy z biblioteki person (dictionary) zarówno klucze jak i wartości
    print(key, ':' , value)

#Napisz funkcję używając pętli by uzyskać następujący wynik:
  #
  ##
  ###
  ####
  #####
  ######
  #######
#podpowiedź
symbol = '#'
symbol += '#'
print(len(symbol)) #długość '##' to 2
print('\t1\t2\t3')
czubek = '  #'
srodek = ' ###'
dol='#####'
print(czubek)
print(srodek)
print(dol)

spacja = ' '
symbol_hash = "#"
for k in range(5):
    print((5-k)*spacja, k*2*symbol_hash)

