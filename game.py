import tkinter as tk
import random

pontuacao_jogador = 0
pontuacao_computador = 0

# CONDIÇÃO
def vitoria(jogador, adversario):
    return (jogador == 'pedra' and adversario == 'tesoura') or \
           (jogador == 'tesoura' and adversario == 'papel') or \
           (jogador == 'papel' and adversario == 'pedra')

# GAME
def jogar(escolha_usuario):
    global pontuacao_jogador, pontuacao_computador

    computador = random.choice(['pedra', 'papel', 'tesoura'])

    if escolha_usuario == computador:
        resultado = "Empate!"
        cor_resultado = "gray"
    elif vitoria(escolha_usuario, computador):
        resultado = "Você ganhou!"
        cor_resultado = "green"
        pontuacao_jogador += 1
    else:
        resultado = "Você perdeu!"
        cor_resultado = "red"
        pontuacao_computador += 1

    label_resultado["text"] = f"Você: {escolha_usuario}\nComputador: {computador}\n{resultado}"
    label_resultado["fg"] = cor_resultado
    label_pontuacao["text"] = f"Jogador: {pontuacao_jogador} | Computador: {pontuacao_computador}"


def zerar_jogo():
    global pontuacao_jogador, pontuacao_computador
    pontuacao_jogador = 0
    pontuacao_computador = 0
    label_resultado["text"] = ""
    label_pontuacao["text"] = "Jogador: 0 | Computador: 0"

# JAN
janela = tk.Tk()
janela.title("Jogo: Pedra, Papel e Tesoura")
janela.geometry("300x330")


tk.Label(janela, text="Escolha uma opção:").pack(pady=10)

# BOTÕES
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=5)
tk.Button(frame_botoes, text="Pedra", width=10, command=lambda: jogar("pedra")).pack(side="left", padx=5)
tk.Button(frame_botoes, text="Papel", width=10, command=lambda: jogar("papel")).pack(side="left", padx=5)
tk.Button(frame_botoes, text="Tesoura", width=10, command=lambda: jogar("tesoura")).pack(side="left", padx=5)

# PLACAR
label_resultado = tk.Label(janela, text="", pady=10)
label_resultado.pack()
label_pontuacao = tk.Label(janela, text="Jogador: 0 | Computador: 0")
label_pontuacao.pack()

# RESET
tk.Button(janela, text="Zerar Jogo", command=zerar_jogo).pack(pady=10)

janela.mainloop()
