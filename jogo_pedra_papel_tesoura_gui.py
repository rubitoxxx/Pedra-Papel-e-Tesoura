import tkinter as tk
from tkinter import ttk
import random
from tkinter import messagebox

class JogoPedraPapelTesouraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Pedra, Papel e Tesoura com IA Generativa")
        self.root.geometry("800x700")
        self.root.configure(bg='#1a1a2e')
        
        # Variáveis do jogo
        self.pontuacao_jogador = 0
        self.pontuacao_ia = 0
        self.opcoes = ['pedra', 'papel', 'tesoura']
        self.emojis = {
            'pedra': '🪨',
            'papel': '📄',
            'tesoura': '✂️'
        }
        
        # Frases para diferentes resultados
        self.frases = {
            'vitoria': [
                "A IA escolheu {jogada_ia} e você {jogada_usuario}. Vitória da IA! Que tal tentar de novo?",
                "{jogada_ia} supera {jogada_usuario}. A máquina leva essa!",
                "Com {jogada_ia}, a IA foi imbatível desta vez!"
            ],
            'derrota': [
                "Você escolheu {jogada_usuario} e venceu a IA que jogou {jogada_ia}! Parabéns!",
                "{jogada_usuario} derrota {jogada_ia}. Você ganhou!",
                "A IA tentou com {jogada_ia}, mas você foi melhor!"
            ],
            'empate': [
                "Ambos escolheram {jogada_usuario}. Empate!",
                "{jogada_usuario} contra {jogada_ia}. Ninguém venceu desta vez.",
                "Empate! Que tal mais uma rodada?"
            ]
        }
        
        self.criar_interface()
        
    def criar_interface(self):
        # Título principal
        titulo = tk.Label(
            self.root,
            text="🎮 Pedra, Papel e Tesoura com IA Generativa",
            font=("Arial", 20, "bold"),
            bg='#1a1a2e',
            fg='white'
        )
        titulo.pack(pady=20)
        
        # Frame do placar
        placar_frame = tk.Frame(self.root, bg='#1a1a2e')
        placar_frame.pack(pady=20)
        
        # Placar
        placar_label = tk.Label(
            placar_frame,
            text="PLACAR",
            font=("Arial", 16, "bold"),
            bg='#1a1a2e',
            fg='white'
        )
        placar_label.pack()
        
        placar_scores = tk.Frame(placar_frame, bg='#1a1a2e')
        placar_scores.pack(pady=10)
        
        # Score do jogador
        self.score_jogador_label = tk.Label(
            placar_scores,
            text="0",
            font=("Arial", 24, "bold"),
            bg='#1a1a2e',
            fg='white'
        )
        self.score_jogador_label.pack(side=tk.LEFT, padx=20)
        
        # VS
        vs_label = tk.Label(
            placar_scores,
            text="×",
            font=("Arial", 24, "bold"),
            bg='#1a1a2e',
            fg='white'
        )
        vs_label.pack(side=tk.LEFT, padx=20)
        
        # Score da IA
        self.score_ia_label = tk.Label(
            placar_scores,
            text="0",
            font=("Arial", 24, "bold"),
            bg='#1a1a2e',
            fg='white'
        )
        self.score_ia_label.pack(side=tk.LEFT, padx=20)
        
        # Labels dos scores
        scores_labels = tk.Frame(placar_frame, bg='#1a1a2e')
        scores_labels.pack()
        
        tk.Label(
            scores_labels,
            text="Você",
            font=("Arial", 12),
            bg='#1a1a2e',
            fg='white'
        ).pack(side=tk.LEFT, padx=20)
        
        tk.Label(
            scores_labels,
            text="IA",
            font=("Arial", 12),
            bg='#1a1a2e',
            fg='white'
        ).pack(side=tk.LEFT, padx=20)
        
        # Frame da área de jogo
        jogo_frame = tk.Frame(self.root, bg='#1a1a2e')
        jogo_frame.pack(pady=20)
        
        # Escolhas dos jogadores
        escolhas_frame = tk.Frame(jogo_frame, bg='#1a1a2e')
        escolhas_frame.pack()
        
        # Jogador
        jogador_frame = tk.Frame(escolhas_frame, bg='#1a1a2e')
        jogador_frame.pack(side=tk.LEFT, padx=20)
        
        tk.Label(
            jogador_frame,
            text="Sua Escolha",
            font=("Arial", 16, "bold"),
            bg='#1a1a2e',
            fg='white'
        ).pack()
        
        self.escolha_jogador_label = tk.Label(
            jogador_frame,
            text="❓",
            font=("Arial", 48),
            bg='#1a1a2e',
            fg='white'
        )
        self.escolha_jogador_label.pack(pady=10)
        
        # VS
        vs_jogo_label = tk.Label(
            escolhas_frame,
            text="VS",
            font=("Arial", 20, "bold"),
            bg='#1a1a2e',
            fg='white'
        )
        vs_jogo_label.pack(side=tk.LEFT, padx=20)
        
        # IA
        ia_frame = tk.Frame(escolhas_frame, bg='#1a1a2e')
        ia_frame.pack(side=tk.LEFT, padx=20)
        
        tk.Label(
            ia_frame,
            text="IA Escolheu",
            font=("Arial", 16, "bold"),
            bg='#1a1a2e',
            fg='white'
        ).pack()
        
        self.escolha_ia_label = tk.Label(
            ia_frame,
            text="❓",
            font=("Arial", 48),
            bg='#1a1a2e',
            fg='white'
        )
        self.escolha_ia_label.pack(pady=10)
        
        # Botões de escolha
        botoes_frame = tk.Frame(self.root, bg='#1a1a2e')
        botoes_frame.pack(pady=20)
        
        tk.Label(
            botoes_frame,
            text="Faça sua escolha:",
            font=("Arial", 16, "bold"),
            bg='#1a1a2e',
            fg='white'
        ).pack(pady=10)
        
        botoes_escolha = tk.Frame(botoes_frame, bg='#1a1a2e')
        botoes_escolha.pack()
        
        # Botão Pedra
        self.criar_botao_escolha(botoes_escolha, 'pedra', '🪨', 'Pedra')
        
        # Botão Papel
        self.criar_botao_escolha(botoes_escolha, 'papel', '📄', 'Papel')
        
        # Botão Tesoura
        self.criar_botao_escolha(botoes_escolha, 'tesoura', '✂️', 'Tesoura')
        
        # Resultado
        resultado_frame = tk.Frame(self.root, bg='#1a1a2e')
        resultado_frame.pack(pady=20)
        
        self.resultado_label = tk.Label(
            resultado_frame,
            text="Escolha uma opção para começar!",
            font=("Arial", 14),
            bg='#1a1a2e',
            fg='white',
            wraplength=600
        )
        self.resultado_label.pack()
        
        # Botão Reset
        reset_button = tk.Button(
            self.root,
            text="🔄 Resetar Placar",
            font=("Arial", 12, "bold"),
            bg='#dc2626',
            fg='white',
            command=self.resetar_jogo,
            relief=tk.FLAT,
            padx=20,
            pady=10
        )
        reset_button.pack(pady=20)
        
    def criar_botao_escolha(self, parent, escolha, emoji, texto):
        button_frame = tk.Frame(parent, bg='#1a1a2e')
        button_frame.pack(side=tk.LEFT, padx=10)
        
        button = tk.Button(
            button_frame,
            text=f"{emoji}\n{texto}",
            font=("Arial", 16),
            bg='#2d2d44',
            fg='white',
            command=lambda: self.jogar(escolha),
            relief=tk.FLAT,
            padx=20,
            pady=15
        )
        button.pack()
        
        # Efeito hover
        def on_enter(e):
            button.configure(bg='#3d3d54')
            
        def on_leave(e):
            button.configure(bg='#2d2d44')
            
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        
    def gerar_frase(self, jogada_ia, jogada_usuario, resultado):
        frases_array = self.frases[resultado]
        frase_escolhida = random.choice(frases_array)
        return frase_escolhida.replace('{jogada_ia}', jogada_ia).replace('{jogada_usuario}', jogada_usuario)
        
    def decidir_resultado(self, jogada_usuario, jogada_ia):
        if jogada_usuario == jogada_ia:
            return 'empate'
        elif (jogada_usuario == 'pedra' and jogada_ia == 'tesoura') or \
             (jogada_usuario == 'papel' and jogada_ia == 'pedra') or \
             (jogada_usuario == 'tesoura' and jogada_ia == 'papel'):
            return 'derrota'  # derrota da IA, vitória do usuário
        else:
            return 'vitoria'  # vitória da IA
            
    def jogar(self, escolha_usuario):
        # Escolha da IA
        escolha_ia = random.choice(self.opcoes)
        
        # Atualizar interface
        self.escolha_jogador_label.config(text=self.emojis[escolha_usuario])
        self.escolha_ia_label.config(text=self.emojis[escolha_ia])
        
        # Decidir resultado
        resultado = self.decidir_resultado(escolha_usuario, escolha_ia)
        
        # Atualizar pontuação
        if resultado == 'derrota':  # vitória do usuário
            self.pontuacao_jogador += 1
            self.score_jogador_label.config(text=str(self.pontuacao_jogador))
        elif resultado == 'vitoria':  # vitória da IA
            self.pontuacao_ia += 1
            self.score_ia_label.config(text=str(self.pontuacao_ia))
        
        # Gerar e mostrar frase
        frase = self.gerar_frase(escolha_ia, escolha_usuario, resultado)
        self.resultado_label.config(text=frase)
        
        # Cor do resultado
        if resultado == 'derrota':  # vitória do usuário
            self.resultado_label.config(fg='#10b981')  # verde
        elif resultado == 'vitoria':  # vitória da IA
            self.resultado_label.config(fg='#ef4444')  # vermelho
        else:
            self.resultado_label.config(fg='#f59e0b')  # amarelo
            
    def resetar_jogo(self):
        self.pontuacao_jogador = 0
        self.pontuacao_ia = 0
        self.score_jogador_label.config(text="0")
        self.score_ia_label.config(text="0")
        self.escolha_jogador_label.config(text="❓")
        self.escolha_ia_label.config(text="❓")
        self.resultado_label.config(text="Escolha uma opção para começar!", fg='white')

def main():
    root = tk.Tk()
    app = JogoPedraPapelTesouraGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
