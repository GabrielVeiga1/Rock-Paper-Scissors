import random

pontuacao_jogador = 0
pontuacao_computador = 0

def jogo():
    global pontuacao_jogador, pontuacao_computador

    while True:
        print('*' * 11)
        print('Vamos jogar?')
        print('*' * 11)
        usuario = input("Escolha pedra, papel, tesoura: ").lower()
        if usuario not in ['pedra', 'papel', 'tesoura']:
            print("Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura.")
            continue

        computador = random.choice(['pedra', 'papel', 'tesoura']) 

        print('-' * 25)
        print(f'Você escolheu: {usuario.capitalize()}') 
        print(f'Eu escolhi: {computador.capitalize()}') 

        if usuario == computador: 
            print('Nós empatamos!')
        elif vitoria(usuario, computador):
            print('Você ganhou!')
            pontuacao_jogador += 1
        else: 
            print('Você perdeu!')
            pontuacao_computador += 1

        print('-' * 25) # linha separação

        print(f'Pontuação - Jogador: {pontuacao_jogador}')
        print(f'Pontuação - Computador: {pontuacao_computador}')

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
