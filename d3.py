print('Bem vindo a grandline, bora achar o One Piece')
print('*' * 45)
one = input('Qual ilha vc escolhe, esquerda ou direita? ')

if one == 'esquerda':
    e = input('vc chegou na ilha da BigMom, vc vai fugir? [S/N] ').upper()
    if  e == 'S':
        s = input('Agora q vc fugiu e conseguiu trinar, vc consegue enfrentar o Kaidou? [S/N] ').upper()
        if s == 'S':
            print('Parabéns!!! depois do kaidou vc achou o One Piece!!')
        else:
            print('Voce nao treinou o suficiente, o Kaidou te venceu')
    else:
        print('A Big Mom te Matou')

elif one == 'direita':
    e = input('vc chegou na ilha do Teach, vc vai fugir? [S/N] ').upper()
    if  e == 'S':
        s = input('Agora q vc fugiu e conseguiu trinar, vc consegue enfrentar o Akainu? [S/N] ').upper()
        if s == 'S':
            print('Parabéns!!! depois do Akainu vc achou o One Piece!!')
        else:
            print('Voce nao treinou o suficiente, o Akainu te venceu')
    else:
        print('O Teach te Matou')
    