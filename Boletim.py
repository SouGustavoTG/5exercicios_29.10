import os
os.system('cls')

print('='*37)
print("Bem vindo. Faça o Cadastro dos Alunos")
print('='*37)

cadastro = dict()

for c in range(1, 5):
    print(f"----- {c}° Aluno -----")
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))
    os.system('cls')
    media = (nota1 + nota2 + nota3 + nota4) / 4
    cadastro[nome] = {
        'notas': [nota1, nota2, nota3, nota4],
        'media': media
    }
    print("-------------------")

os.system('cls')
print("----- Boletim dos Alunos -----")
for k, v in cadastro.items():
    print(f"O aluno(a) {k} teve média {v['media']:.1f}")
print("------------------------------")

while True:
    consulta = str(input("Deseja consultar a média e notas de algum aluno? (s/n): ")).lower().strip()
    if consulta == 's':
        os.system('cls')
        aluno = str(input("Digite o nome do aluno: "))
        if aluno in cadastro:
            notas_aluno = cadastro[aluno]['notas']
            media_aluno = cadastro[aluno]['media']
            
            os.system('cls')
            print(f"----- Dados do Aluno: {aluno} -----")
            print(f"Nota 1: {notas_aluno[0]:.1f}")
            print(f"Nota 2: {notas_aluno[1]:.1f}")
            print(f"Nota 3: {notas_aluno[2]:.1f}")
            print(f"Nota 4: {notas_aluno[3]:.1f}")
            print(f"Média: {media_aluno:.1f}")
            
            if media_aluno >= 7.0:
                print("Situação: Aprovado ")
            else:
                print("Situação: Reprovado ")
            print("----------------------------------")
        else:
            print("Aluno não encontrado.")
    elif consulta == 'n':
        os.system('cls')
        print("Encerrando o programa. Obrigado!")
        break
    else:
        print("Opção inválida. Por favor, Digite 's' para sim ou 'n' para não.")