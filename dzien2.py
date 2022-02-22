#materiały: 
#https://github.com/Asabeneh/30-Days-Of-Python/blob/master/03_Day_Operators/03_operators.md

x = 5
y = '123 test @@@'

print(x)
print(y)
print('y')
#print(z) #błąd - z nie jest zdefiniowane

#x = x + 3
x += 3 #do x dodajemy 3 - więc x będzie równe 8

print("Nowa wartość x: ", x)

#x %= 3
z = x % 3 #również równe 2 - reszta z dzielenia 8 przez 3

print("Reszta z dzielenia x przez 3: ", z )

print(x // 3) 
# 2 ** 3 = 2*2*2

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 8 it means 2 * 2 * 2

#x, y, z  - zdefiniowane - z czego x oraz z jako liczby
y += 'abc'  #dodawanie stringów (słów, zdań)
print('string y po dodaniu "abc": ', y)

a = 1
b = 4

suma = a + b                # 5
roznica = a - b             # -3
mnozenie = a * b            # 4
dzielenie = a / b           # 0.25
reszta_z_dzielenia = a % b  # 1
pierwiastek = a // b        # 1
potega = a ** b             # 1*1*1*1

'''https://github.com/pkiczko/GCKChotomow'''

dlugosc = 10
szerokosc = 20
pole_prostokata = dlugosc * szerokosc
print('Pole prostokąta:', pole_prostokata)

print(x != y) # jeśli x nie jest równe y, to otrzymamy
              # True (prawda, tak), w przeciwnym wypadku
              # False (fałsz, nie prawda)
if (x != y): #czy x nie jest równe y
    print("Nie są sobie równe!") #kiedy x i y nie są równe
    #dodatkowe linijki
    #

else: #w innym wypadku
    print("Są sobie równe!") #w każdym innym wypadku
    print("Dodatkowa linijka")

print("a < b: ", a < b)
print("a < 1: ", a < 1)
print("a <= 1: ", a <= 1)

            # gdy w nawiasie wartość ostateczna to prawda(True)
if (True):  # wtedy kondycja spełniona, kod poniżej zostanie wykonany
    print("Prawda jest prawdą?")
print(a<b)  # True
print(a==1) # True
print(True)
print(True and False)   # dla operatora and wszystko musi 
                        # być True by całość była też True           
print(True or False)    # tu wystarczy jedno True

#przykładowe dane
ciasteczka = False
mleko = False
pada_deszcz = True
brak_chmur = False
podroz_mikolaja = 0

if (ciasteczka and mleko):
    podroz_mikolaja += 1 # jeśli są ciasteczka oraz mleko
                         # wtedy ten kod jest użyty
#wezmiemy prarasolke jest bedzie padac deszcz
#albo nie bedzie chmur na niebie (upał)
if (pada_deszcz or brak_chmur):
    print("bierzemy parasolkę")



