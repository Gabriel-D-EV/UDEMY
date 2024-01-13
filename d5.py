num = int(input("Number: "))
somap = 0
for n in range(0, num +1):
    if n % 2 == 0:
        somap += n

print(somap)

#-------------------------------------------#

num = 100

for n in range(0, num +1):
    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)

#-------------------------------------------#
import random
print("Criador de Senhas")
print("=-" * 10)

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

simbolos = ["*", "-", "+", ":", ";", "@", "#", "$"]

senhal = []
senha = ""
ql = int(input("Digite a quantidade de letras: "))
qn = int(input("Digite a quantidade de numeros: "))
qs = int(input("Digite a quantidade de simbolos: "))

for c in range(1, ql + 1 ):
    senhal += random.choice(letras)

for c in range(1, qn + 1 ):
    senhal += random.choice(numeros)

for c in range(1, qs + 1 ):
    senhal += random.choice(simbolos)


print(senhal)
random.shuffle(senhal)
for n in senhal:
    senha += n

print(senha)