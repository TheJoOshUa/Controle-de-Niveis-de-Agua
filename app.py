from colorama import Fore, Style
import random

# Criando lista de mensagens de saída
mensagem = ["Muito Baixo (CRITICO)", "Baixo", "Médio", "Alto", "Muito alto (ALERTA)"]
nivel = [1, 2, 3, 4, 5]

# Definindo cores com base no nível
def cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.BLUE
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE

# Escolhendo o nível randomicamente
nivel_escolhido = random.choice(nivel)

# Colhendo a mensagem da lista criada de acordo com o nível escolhido randomicamente
texto_mensagem = mensagem[nivel_escolhido - 1]

# Colhendo a cor da lista de cores criada de acordo com o nível escolhido randomicamente
cor_mensagem = cor(nivel_escolhido - 1)

# Exibindo a mensagem em sua determinada cor
print(f"{cor_mensagem}{texto_mensagem}{Style.RESET_ALL}")