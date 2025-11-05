import os
import sys
import time
import subprocess
from getpass import getpass  # para esconder a senha digitada

def clear():
    os.system('cls')

def fazer_login():
    """Retorna True se o login for bem sucedido, False caso contrário."""
    tentativas = 3
    # Usuário e senha padrão (você pode modificar)
    USUARIO = 'admin'
    SENHA = '123'
    
    while tentativas > 0:
        clear()
        print('=== SISTEMA DE LOGIN ===')
        print(f'Tentativas restantes: {tentativas}')
        usuario = input('Usuário: ').strip()
        senha = getpass('Senha: ').strip()  # getpass esconde a senha
        
        if usuario == USUARIO and senha == SENHA:
            clear()
            print('Login realizado com sucesso!')
            time.sleep(1)
            return True
        
        clear()
        print('Usuário ou senha incorretos.')
        time.sleep(1)
        tentativas -= 1
    
    print('Número máximo de tentativas excedido.')
    time.sleep(2)
    return False

def executar_menu():
    """Executa o arquivo Menu.py"""
    menu_path = os.path.join(os.path.dirname(__file__), 'Menu.py')
    if os.path.exists(menu_path):
        # Executa o Menu.py usando o mesmo interpretador Python
        subprocess.run([sys.executable, menu_path])
    else:
        print('Erro: arquivo Menu.py não encontrado!')
        time.sleep(2)

if __name__ == '__main__':
    # Se executado diretamente, tenta fazer login
    if fazer_login():
        clear()
        print('Redirecionando para o menu principal...')
        time.sleep(1)
        executar_menu()
    else:
        print('Falha no login.')