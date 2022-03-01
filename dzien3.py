# https://github.com/pkiczko/GCKChotomow

cytat = "A niechaj narodowie wżdy postronni znają, iż Polacy nie gęsi, iż swój język mają."
abc = "abcdef "
#      0123456

print(len(cytat))
print(len(abc))
print(cytat[2]) #n
print(cytat[-1]) #ostatni znak stringu
print(abc[0:3]) #od 0wego elemntu (czyli pierwszego) do 3 wyłącznie
print(abc[0:3:2]) #

zdanie = "Ala \t ma\tkota. \nKota ma Ala."

print(zdanie)
print("\\ \" ")

opis1 = "Ile razy występuje w cytacie litera a? "
print(opis1, cytat.count('a'))
print(zdanie.expandtabs(10)) #zwiększa odstęp tabulatora (\t)

#przykład tabelki
wiersz1= "\t1.\t2.\t3."
wiersz2= "\n\tPoznań\tWarszawa\tOstrołęka"
wiersz3= "\n\tpomarańczowy\tzielony\tturkusowy"
print(wiersz1.expandtabs(20), wiersz2.expandtabs(20), wiersz3.expandtabs(20))
#dzięki zwiekszeniu odstępów \t tabelka nie rozjeżdża się

print(zdanie.endswith("Ala."))  #True (Tak)
print(zdanie.endswith("Ala"))   #False (Nie)
print(zdanie.endswith("a."))    #True (Tak)

zdanie2 = "Rumcajs ma czarną brodę i modne trzewiki."

print(zdanie.find("Ala")) #0 bo pierwszse wystąpianie na pozycji 0
print(zdanie2.find("od")) #20 bo 20sta pozycja
#find znajduje tylko pierwsze wystąpienie wyszukiwanych liter/znaków

#isalpha() - sprawdza czy dany string ma znaki zawarte w alfabecie

print(cytat.isalpha())
slowo = "Wżdy "
print(slowo.isalpha())

cyfra = "50"
cyfra2 = 50
cyfra3 = 50.5
print(cyfra.isdigit()) #można sprawdzić czy zawaratość stringu to liczba
print(type(cyfra))  #sprawdzenie typu zmiennej
print(type(cyfra2)) #'int' czyli integer - liczba całkowita
print(type(cyfra3)) #'float' znaczy liczba ułamkowa

print("cyfra".isidentifier()) #True - znaczy ze to jest poprawna nazwa
                              #wg Pythona dla zmiennej

#zielonyTrawnik nazewnictwo w stylu tzw. "camelback"
print("###### Mała/Wielka litera #######")
#sprawdzanie czy słowo/słowa są wszystkie napisane małą literą
print(abc.islower()) #True, bo string zawiera tylko małe litery
print(abc.isupper()) #False

print(abc.upper()) #zamienia wszystkie litery na wielkie
print(cytat.lower()) #jak wyżej, tylko na małe

##komendy split() oraz join()

print(cytat.split(" ")) #znakiem dzielącym jest tu spacja (" ")
print(cytat) #by na stałe podzieliło cytat na zbiór słów
            #należy przypisać do tego zmienną, jako poniżej
podzielone = cytat.split(" ")
print(podzielone)
polaczone = "-".join(podzielone)
print(polaczone)

#### replace() - zamiana znaków w stringu #####

print(cytat.replace(',', '').replace('.', ''))  #w ten sposób pozbyliśmy się
                                                #całej interpunkcji z cytatu
oddzielne_slowa = cytat.replace(',', '').replace('.', '').split(" ")

print(oddzielne_slowa)

print(oddzielne_slowa[1][0:3])

zlozony_zbior = [ [[1,2,3], [5,5,5], "zielony"],'abc' ]

print(zlozony_zbior[0][1]) #[5,5,5]
print(zlozony_zbior[0][1][1]) #5 - ta środkowa!

#zadanie 1
#Połącz słowa 'Trzydzieści', 'Dni' oraz "Python'a" - wynik  "Trzydzieści Dni Python'a".

#Zadanie 2
#Podziel string "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
# używając przecinków jako miejsce podziału

#Zadanie 3
#Połącz zbiór ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'] w jeden string,
#znak łączenia niech będzie "_".

#Zadanie 4
#Używając metod drukowania stringów napisać:
'''
 8 + 6 = 14 #print('8 + 6 = ', 8+6)
 8 - 6 = 2
 8 * 6 = 48
 8 / 6 = 1.33
 8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''

