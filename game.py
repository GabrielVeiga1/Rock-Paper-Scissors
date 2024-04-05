import random

from colorama import Fore, Style

import random

pontuacao_jogador = 0
pontuacao_computador = 0

def jogo():
    global pontuacao_jogador, pontuacao_computador

    while True:
        print(Fore.YELLOW + '*' * 11)
        print('Vamos jogar?')
        print('*' * 11 + Style.RESET_ALL)
        usuario = input("Escolha pedra, papel, tesoura: ").lower()
        if usuario not in ['pedra', 'papel', 'tesoura']:
            print(Fore.RED + "Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura." + Style.RESET_ALL)
            continue

        computador = random.choice(['pedra', 'papel', 'tesoura']) 

        print('-' * 25)
        print(f'Você escolheu: {Fore.GREEN}{usuario.capitalize()}{Style.RESET_ALL}') # mostra escolha do user
        print(f'Eu escolhi: {Fore.GREEN}{computador.capitalize()}{Style.RESET_ALL}') # mostra escolha do computador

        if usuario == computador: # verifica se houve empate
            print(Fore.CYAN + 'Nós empatamos!' + Style.RESET_ALL)
        elif vitoria(usuario, computador): # verifica se houve vitoria do jogador e adiciona na pontuação
            print(Fore.GREEN + 'Você ganhou!' + Style.RESET_ALL)
            pontuacao_jogador += 1
        else: # verifica se houve vitoria do computador e adiciona na pontuação
            print(Fore.RED + 'Você perdeu!' + Style.RESET_ALL)
            pontuacao_computador += 1

        print('-' * 25) # linha separação

        print(f'Pontuação - Jogador: {Fore.GREEN}{pontuacao_jogador}{Style.RESET_ALL}')
        print(f'Pontuação - Computador: {Fore.RED}{pontuacao_computador}{Style.RESET_ALL}')

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        print('------------------------') # linha separação
        if jogar_novamente != 's':
            break

def vitoria(jogador, adversario):
    if (jogador == 'pedra' and adversario == 'tesoura') \
    or (jogador == 'tesoura' and adversario == 'papel') \
    or (jogador == 'papel' and adversario == 'pedra'):
        return True
    return False

jogo()





















