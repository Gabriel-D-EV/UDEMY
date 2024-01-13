l1 = [" "," ", " "]
l2 = [" "," ", " "]
l3 = [" "," ", " "]
map = [l1,l2,l3]
print("marque um x para achar o tesouro")

position = input()

letra = position[0].lower()
abc = ["a", "b", "c"]
letra_1 = abc.index(letra)
n_1 = int(position[1]) - 1
map[n_1][letra_1] = "X"


print(f"{l1}\n{l2}\n{l3}")
print(letra_1)

#---------------------------------------------

from random import randint

pedra = '''
    ______
---´  __  |
     (__|_|_)
     (______)
     (______)
---._(_____)
'''

papel = '''
    ______
---´  ____)_____
        _________)
        __________)
       __________)
---.___________)
'''

tesoura = '''
    ______
---´  __  |_____
        |_|______)
        __________)
     (______)
---._(_____)
'''

print("JOKENKU")
j = int(input("1 para pedra, 2 para papel e 3 para tesoura, Qual vc escolhe: "))
pc = randint(1, 3)

if j == 1 and pc == 1:
    print(f"vc escolheu \n {pedra}\n o pc escolheu \n {pedra}\n Empatou")

elif j == 1 and pc == 2:
    print(f"vc escolheu \n {pedra}\n o pc escolheu \n {papel}\n Vc Perdeu")

elif j == 1 and pc == 3:
    print(f"vc escolheu \n {pedra}\n o pc escolheu \n {tesoura}\n Vc Ganhou")

elif j == 2 and pc == 1:
    print(f"vc escolheu \n {papel}\n o pc escolheu \n {pedra}\n Voce Ganhou")

elif j == 2 and pc == 2:
    print(f"vc escolheu \n {papel}\n o pc escolheu \n {papel}\n Empatou")

elif j == 2 and pc == 3:
    print(f"vc escolheu \n {papel}\n o pc escolheu \n {tesoura}\n Vc Perdeu")

elif j == 3 and pc == 1:
    print(f"vc escolheu \n {tesoura}\n o pc escolheu \n {pedra}\n Voce Perdeu")

elif j == 3 and pc == 2:
    print(f"vc escolheu \n {tesoura}\n o pc escolheu \n {papel}\n Vc Ganhou")

elif j == 3 and pc == 3:
    print(f"vc escolheu \n {tesoura}\n o pc escolheu \n {tesoura}\n Empatou")


