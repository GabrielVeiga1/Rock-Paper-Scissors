import random

from colorama import Fore, Style

pontuacao_jogador = 0
pontuacao_computador = 0

decorative_line = Fore.YELLOW + '─' * 25 + Style.RESET_ALL

def jogo():
    global pontuacao_jogador, pontuacao_computador

    while True:
        print(decorative_line)
        print('{:^27}'.format('*' * 13 + Style.RESET_ALL))
        print('{:^24}'.format('Vamos jogar?'))  # Centralizando o texto "Vamos jogar?"
        print('{:^27}'.format('*' * 13 + Style.RESET_ALL))
        print(decorative_line)
        usuario = input("Escolha pedra, papel, tesoura: ").lower()
        if usuario not in ['pedra', 'papel', 'tesoura']:
            print(Fore.RED + "Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura." + Style.RESET_ALL)
            continue

        computador = random.choice(['pedra', 'papel', 'tesoura']) 

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

        print(decorative_line) # linha separação

        print(f'Pontuação - Jogador: {Fore.GREEN}{pontuacao_jogador}{Style.RESET_ALL}')
        print(f'Pontuação - Computador: {Fore.RED}{pontuacao_computador}{Style.RESET_ALL}')

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            break

def vitoria(jogador, adversario):
    if (jogador == 'pedra' and adversario == 'tesoura') \
    or (jogador == 'tesoura' and adversario == 'papel') \
    or (jogador == 'papel' and adversario == 'pedra'):
        return True
    return False

jogo()
