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
