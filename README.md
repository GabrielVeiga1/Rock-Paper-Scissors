# Pedra, Papel ou Tesoura - Jogo com Tkinter 🎮

Este é um projeto simples de Pedra, Papel ou Tesoura criado com a biblioteca `Tkinter` do Python. Ideal para iniciantes que estão aprendendo lógica de programação, estruturas condicionais e interfaces gráficas.

## 💡 Sobre o Projeto

- O jogador escolhe entre **Pedra**, **Papel** ou **Tesoura**.
- O computador escolhe aleatoriamente uma opção.
- O resultado da rodada é exibido com uma cor diferente:
  - 🟢 **Verde** para vitória do jogador.
  - 🔴 **Vermelho** para derrota.
  - 🔵 **Azul** para empate.
- A pontuação de ambos é atualizada a cada jogada.
- Possui um botão para **zerar o jogo** e começar do zero.

## 📷 Interface

A interface foi feita com `Tkinter`, com botões alinhados lado a lado para tornar o jogo mais intuitivo.

## 🧠 Lógica

A lógica do jogo usa condições simples para verificar quem ganhou:
- Pedra ganha de Tesoura
- Tesoura ganha de Papel
- Papel ganha de Pedra

## ▶️ Como rodar

1. Certifique-se de ter o Python instalado (versão 3.6 ou superior).
2. Clone ou baixe este repositório.
3. Execute o script:

```bash
python pedra_papel_tesoura.py
