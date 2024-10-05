import random 
import os

move_list = ['pedra','papel','tesoura']
player_count = 0
computer_count = 0

print('========================================')
print('Bem vindo ao jogo Pedra, Papel e Tesoura')
print('========================================\n')

def mainPrint():
    print('\nPLACAR:')
    print('Você: {}\nComputador: {}'.format(player_count, computer_count))
    print('\n')
    print('Escolha sua jogada:')
    print('0 - Pedra \n1 - Papel \n2 - Tesoura \n')

def selectMove(): 
    return random.choice(move_list)

def getPlayerMove():
    while True:
        try:
            player_move = int(input())
            if player_move not in [0,1,2]:
                raise
            return move_list[player_move]
        except:
            print('Jogada inválida. Tente novamente')

def selectWinner(p_move, c_move):
    global player_count, computer_count

    if p_move == 'papel':
        if c_move == 'pedra':
            player_count += 1

            return 'player'
        elif c_move == 'tesoura':
            computer_count += 1

            return 'computer'
        else:
            return 'draw'

    if p_move == 'pedra':
        if c_move == 'papel':
            computer_count += 1

            return 'computer'
        elif c_move == 'tesoura':
            player_count += 1
            
            return 'player'
        else:
            return 'draw'

    if p_move == 'tesoura':
        if c_move == 'papel':
            player_count += 1

            return 'player'
        elif c_move == 'pedra':
            computer_count += 1
            
            return 'computer'
        else:
            return 'draw'

again = 1

while again == 1:
    mainPrint()
    player_move = getPlayerMove()
    computer_move = selectMove()
    winner = selectWinner(player_move, computer_move)

    print('')
    print('=================')
    print('Sua jopgada: {}'.format(player_move))
    print('Jogada do computador: {}'.format(computer_move))
    print('=================')

    if winner == 'player':
        print('Você ganhou!')
    elif winner == 'computer':
        print('Você perdeu!')
    else:
        print('Empate!')

    while True:
        print('Jogar novamente? (0 - Sim, 1 - Não)')
        try: 
            next = int(input())
            if next == 0: 
                    break
            elif next == 1:
                again = 0
                break
        except:
            print('Opção inválida. Tente novamente')    
        os.system('cls')