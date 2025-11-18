import os
os.system('cls')

jogador = {}
gols = []
total = 0

jogador['nome'] = str(input('Qual o nome do jogador?'))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(partidas):
    gol = int(input(f'Quantos gols na partida {i+1}? '))
    gols.append(gol)
    total += gol

jogador['gols'] = gols[:]
jogador['total'] = total

print('-=' * 20)
print(jogador)
print('-=' * 20)

print(f'O jogador {jogador["nome"]} jogou em  {partidas} partidas.')
for i, g in enumerate(jogador['gols']):
    print(f'Na partida {i+1}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')