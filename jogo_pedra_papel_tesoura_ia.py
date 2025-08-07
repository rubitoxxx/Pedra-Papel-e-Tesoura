import random

# Lista de opções
opcoes = ['pedra', 'papel', 'tesoura']

# Função de IA generativa para criar frases únicas para cada jogada
def gerar_frase(jogada_ia, jogada_usuario, resultado):
    frases_vitoria = [
        f"A IA escolheu {jogada_ia} e você {jogada_usuario}. Vitória da IA! Que tal tentar de novo?",
        f"{jogada_ia.capitalize()} supera {jogada_usuario}. A máquina leva essa!",
        f"Com {jogada_ia}, a IA foi imbatível desta vez!"
    ]
    frases_derrota = [
        f"Você escolheu {jogada_usuario} e venceu a IA que jogou {jogada_ia}! Parabéns!",
        f"{jogada_usuario.capitalize()} derrota {jogada_ia}. Você ganhou!",
        f"A IA tentou com {jogada_ia}, mas você foi melhor!"
    ]
    frases_empate = [
        f"Ambos escolheram {jogada_usuario}. Empate!",
        f"{jogada_usuario.capitalize()} contra {jogada_ia}. Ninguém venceu desta vez.",
        f"Empate! Que tal mais uma rodada?"
    ]
    if resultado == 'vitoria':
        return random.choice(frases_vitoria)
    elif resultado == 'derrota':
        return random.choice(frases_derrota)
    else:
        return random.choice(frases_empate)

def decidir_resultado(jogada_usuario, jogada_ia):
    if jogada_usuario == jogada_ia:
        return 'empate'
    elif (jogada_usuario == 'pedra' and jogada_ia == 'tesoura') or \
         (jogada_usuario == 'papel' and jogada_ia == 'pedra') or \
         (jogada_usuario == 'tesoura' and jogada_ia == 'papel'):
        return 'derrota'  # derrota da IA, vitória do usuário
    else:
        return 'vitoria'  # vitória da IA

def main():
    print("Bem-vindo ao Pedra, Papel e Tesoura com IA Generativa!")
    while True:
        jogada_usuario = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()
        if jogada_usuario == 'sair':
            print("Obrigado por jogar!")
            break
        if jogada_usuario not in opcoes:
            print("Opção inválida. Tente novamente.")
            continue
        jogada_ia = random.choice(opcoes)
        resultado = decidir_resultado(jogada_usuario, jogada_ia)
        frase = gerar_frase(jogada_ia, jogada_usuario, resultado)
        print(frase)

if __name__ == "__main__":
    main()
