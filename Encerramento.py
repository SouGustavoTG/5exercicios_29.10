import os
os.system('cls')

while True:
    print("escreva [menu] para voltar ao menu principal")
    print("escreva [sair] para Sair")

    opcao = input("Escolha uma opção: ").lower()

    if opcao == 'menu':
        print("Voltando ao menu")
    elif opcao == 'sair':
        print("Encerrando o programa")
        break 
    else:
        print("Opção inválida, tente de novamente")

        print("-=" * 30)
        print('Trabalho feito por:')
        print('Luiz Carlos Borges D\'Amico')
        print('Gustavo Souza Valim')
        print('Rodrigo Borges')
        input("Vinicius de Paula Bekert")
