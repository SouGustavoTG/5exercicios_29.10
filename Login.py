import os
import sys
import time
from getpass import getpass  # para esconder a senha digitada

# Configurações
TENTATIVAS_MAXIMAS = 3
USUARIO_PADRAO = 'admin'
SENHA_PADRAO = '123'

# Cores ANSI
CORES = {
    'titulo': '\033[1;36m',    # Ciano brilhante
    'erro': '\033[1;31m',      # Vermelho brilhante
    'sucesso': '\033[1;32m',   # Verde brilhante
    'aviso': '\033[1;33m',     # Amarelo brilhante
    'reset': '\033[0m'         # Reseta cor
}

def clear():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def colorir(texto, tipo='normal'):
    """Aplica cor ao texto se o tipo existir em CORES."""
    if tipo in CORES:
        return f"{CORES[tipo]}{texto}{CORES['reset']}"
    return texto

def mostrar_cabecalho():
    """Mostra o cabeçalho do sistema de login."""
    clear()
    print(colorir('╔═════════════════════════╗', 'titulo'))
    print(colorir('║    SISTEMA DE LOGIN     ║', 'titulo'))
    print(colorir('╚═════════════════════════╝', 'titulo'))

def mostrar_carregando(texto, duracao=1):
    """Mostra uma mensagem de carregando com animação."""
    print(f"\n{texto}", end='', flush=True)
    for _ in range(3):
        time.sleep(duracao/3)
        print(".", end='', flush=True)
    print()

def fazer_login():
    """Gerencia o processo de login. Retorna True se bem sucedido."""
    tentativas = TENTATIVAS_MAXIMAS
    
    while tentativas > 0:
        mostrar_cabecalho()
        print(colorir(f'\nTentativas restantes: {tentativas}', 'aviso'))
        
        # Entrada do usuário
        usuario = input('\nUsuário: ').strip()
        if not usuario:
            clear()
            print(colorir('Erro: Usuario não pode estar vazio!', 'erro'))
            time.sleep(1)
            continue
            
        # Entrada da senha (oculta quando possível)
        try:
            senha = getpass('Senha: ').strip()
        except Exception:
            # fallback para ambientes que não suportam getpass
            print(colorir('\n(Aviso: seu terminal não permite esconder a senha. A senha será visível enquanto digita.)', 'aviso'))
            senha = input('Senha: ').strip()
        if not senha:
            clear()
            print(colorir('Erro: Senha não pode estar vazia!', 'erro'))
            time.sleep(1)
            continue
        
        # Validação
        if usuario == USUARIO_PADRAO and senha == SENHA_PADRAO:
            clear()
            print(colorir('Login realizado com sucesso!', 'sucesso'))
            mostrar_carregando("Carregando menu", 1)
            return True
        
        # Feedback de erro
        clear()
        print(colorir('Usuário ou senha incorretos!', 'erro'))
        tentativas -= 1
        
        if tentativas > 0:
            print(f'\nVocê ainda tem {tentativas} tentativa(s).')
            time.sleep(2)
    
    # Tentativas esgotadas
    clear()
    print(colorir('Número máximo de tentativas excedido!', 'erro'))
    print(colorir('\nO sistema será encerrado por segurança.', 'aviso'))
    mostrar_carregando("Encerrando", 1)
    return False

def executar_menu():
    """Tenta executar o Menu.py."""
    import subprocess  # importado aqui para evitar conflito com o menu
    
    menu_path = os.path.join(os.path.dirname(__file__), 'Menu.py')
    if not os.path.exists(menu_path):
        print(colorir('\nErro: arquivo Menu.py não encontrado!', 'erro'))
        print(colorir('Verifique se o arquivo está na mesma pasta.', 'aviso'))
        time.sleep(2)
        return
    
    try:
        subprocess.run([sys.executable, menu_path], check=True)
    except subprocess.CalledProcessError:
        print(colorir('\nErro ao executar o menu!', 'erro'))
        time.sleep(2)
    except KeyboardInterrupt:
        print(colorir('\nOperação cancelada pelo usuário.', 'aviso'))
        time.sleep(1)

if __name__ == '__main__':
    # Se executado diretamente, limpa a tela e tenta fazer login
    clear()
    if fazer_login():
        executar_menu()
    sys.exit(0)