import os
import random
import time

os.system('cls')
jogadores = []
for i in range(1, 5):
    while True:
        nome = input(f'Nome do jogador {i}: ').strip()
        if not nome:
            print('Nome vazio. Digite novamente.')
            continue
        # Comparação sem diferenciar maiúsculas/minúsculas
        if any(nome.lower() == jogador for jogador in jogadores):
            print('Nome já cadastrado. Escolha outro nome.')
            continue
        jogadores.append(nome)
        break
print('Preparando os dados...')
time.sleep(0.2)

resultados = {}
# Usando enumerate para mostrar número do jogador na rolagem
for num, jogador in enumerate(jogadores, 1):
    dado = random.randint(1,6)
    resultados[jogador] = dado
    print(f'Jogador {num} ({jogador}) rolou o dado e tirou {dado}.')
    time.sleep(0.2)
print('Calculando os resultados finais...')
time.sleep(0.2)

# Ordenar jogadores por pontuação (maior para menor)
jogadores_ordenados = sorted(resultados.items(), key=lambda x: x[1], reverse=True)

print('------Resultados finais------')
# Usando enumerate para gerar posições automaticamente
for posição, (jogador, pontos) in enumerate(jogadores_ordenados, 1):
    sufixo = 'º' if posição == 1 else 'º'
    print(f'{posição}{sufixo} lugar - {jogador}: {pontos} pontos')