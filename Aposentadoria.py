import os
import time 
os.system('cls')

print('='*50)
print("Bem vindo ao Sistema de Cadastro para Aposentadoria")
print('='*50)

cadastro = dict()
cadastro['Nome'] = str(input("Digite seu Nome: "))
cadastro['ano de nascimento'] = int(input("Digite seu Ano de Nascimento: "))
cadastro['Carteira de Trabalho (CTPS)'] = int(input("Digite o Número da sua Carteira de Trabalho (CTPS) [0 se não tiver]: "))

ano_atual = time.localtime().tm_year
idade = ano_atual - cadastro['ano de nascimento']

if cadastro['Carteira de Trabalho (CTPS)'] != 0:
    cadastro['ano de contratação'] = int(input("Digite o Ano de Contratação: "))
    cadastro['salário'] = float(input("Digite o Salário: R$"))
    
    anos_trabalhados = ano_atual - cadastro['ano de contratação']
    
    if anos_trabalhados >= 35:
        os.system('cls')
        print(f"O Funcionário {cadastro['Nome']} tem {idade} anos de idade.")
        print(f"Com {anos_trabalhados} anos trabalhados, já pode  aposentar")
    else:
        aposentadoria = 35 - anos_trabalhados
        ano_aposentadoria = ano_atual + aposentadoria
        
        
        idade_aposentadoria = idade + aposentadoria
        
        os.system('cls')
        print(f"O Funcionário {cadastro['Nome']} tem {idade} anos de idade.")
        print(f"Com {anos_trabalhados} anos trabalhados, faltam {aposentadoria} anos para a aposentadoria.")
        print(f"Ele(a) irá se aposentar no ano de {ano_aposentadoria} com {idade_aposentadoria} anos.")
        
else:
    os.system('cls')
    print(f"O Funcionário {cadastro['Nome']} tem {idade} anos de idade.")
    print("Ele(a) não possui Carteira de Trabalho (CTPS) registrada.")