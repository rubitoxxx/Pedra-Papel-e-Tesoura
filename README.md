# 🎮 Jogo Pedra, Papel e Tesoura com IA Generativa

[![Badge - Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![Badge - IA](https://img.shields.io/badge/IA_Generativa-FF6B6B?style=for-the-badge)]()
[![Badge - Status](https://img.shields.io/badge/Status-Funcional-brightgreen?style=for-the-badge)]()

> Projeto demonstrativo de IA Generativa aplicada ao desenvolvimento de jogos, criando um jogo clássico de Pedra, Papel e Tesoura com geração dinâmica de conteúdo.

---

## 📌 Visão Geral

Este projeto demonstra como a **Inteligência Artificial Generativa** pode ser aplicada no desenvolvimento de jogos, mesmo em projetos simples. O jogo de Pedra, Papel e Tesoura foi enriquecido com IA que gera frases únicas e personalizadas para cada jogada, tornando a experiência mais envolvente e criativa.

Inclui:
- Jogo clássico de Pedra, Papel e Tesoura
- IA generativa para criação de frases dinâmicas
- Sistema de geração de conteúdo personalizado
- Análise detalhada do funcionamento da IA

---

## 🤖 Funcionalidades da IA Generativa

- 🎯 **Escolha Inteligente**: IA seleciona jogadas de forma aleatória e imprevisível
- 💬 **Geração de Frases**: Cria respostas únicas para cada resultado do jogo
- 🎨 **Personalização**: Adapta as mensagens baseadas nas escolhas do jogador
- 🔄 **Variedade**: Oferece múltiplas opções de resposta para evitar repetição

---

## 📂 Estrutura do Projeto

```
projeto ia/
├── jogo_pedra_papel_tesoura_ia.py  # Jogo principal com IA generativa
├── README.md                        # Documentação e análise do código
└── (arquivos do projeto)
```

---

## 💡 Tecnologias Utilizadas

- **Python** para lógica do jogo e implementação da IA
- **Random Module** para geração de jogadas e seleção de frases
- **String Formatting** para personalização das mensagens
- **Loop Control** para experiência de jogo contínua

---

## 🧠 Análise do Código da IA

### Como Funciona a IA Generativa no Jogo:

**1. Escolha da Jogada da IA:**
```python
jogada_ia = random.choice(opcoes)
```
A IA seleciona aleatoriamente entre 'pedra', 'papel' ou 'tesoura', simulando um adversário imprevisível.

**2. Geração Generativa de Frases:**
```python
def gerar_frase(jogada_ia, jogada_usuario, resultado):
    # Listas de frases para cada situação
    frases_vitoria = [...]
    frases_derrota = [...]
    frases_empate = [...]
    
    # Seleção aleatória baseada no resultado
    return random.choice(frases_apropriadas)
```

**3. Personalização e Variedade:**
- As frases incluem as escolhas do usuário e da IA
- Variações de linguagem para cada situação
- Sensação de criatividade e resposta única a cada jogada

**4. Fluxo do Jogo:**
- Loop contínuo de jogadas
- Validação de entrada do usuário
- Geração dinâmica de conteúdo
- Experiência personalizada

---

## 🎯 Objetivo do Projeto

- Demonstrar na prática como a IA generativa pode enriquecer jogos simples
- Mostrar conceitos de geração de conteúdo dinâmico
- Exemplificar aplicações de IA no desenvolvimento de jogos
- Educar sobre as características da IA generativa

---

## 🚀 Como Executar

1. Certifique-se de ter Python instalado
2. Execute o arquivo: `python jogo_pedra_papel_tesoura_ia.py`
3. Siga as instruções na tela para jogar
4. Digite 'sair' para encerrar

---

## 📚 Conceitos de IA Generativa Aplicados

### Características Demonstradas:
- **Criatividade**: Gera conteúdos novos e variados
- **Adaptação**: Modifica respostas conforme o contexto
- **Personalização**: Cria experiências únicas
- **Automação**: Reduz trabalho manual de desenvolvimento

### Aplicações no Desenvolvimento de Jogos:
- Geração de diálogos dinâmicos
- Criação de cenários e mapas
- Missões e desafios personalizados
- Narração adaptativa

---

## 🙋‍♂️ Autor

**Rubens Gabriel e Silva Santos**  
📫 [rubensgabrielesilvasantos@gmail.com](mailto:rubensgabrielesilvasantos@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/rubens-gabriel-221679263)  
💻 [GitHub](https://github.com/rubitoxxx)

---

> Projeto educacional — Demonstração de IA Generativa aplicada ao desenvolvimento de jogos 🚀

