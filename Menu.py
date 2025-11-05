import os
import sys
import time
import subprocess
from Login import fazer_login

# Configurações
ROOT = os.path.dirname(__file__)
CORES = {
    'titulo': 36,    # Ciano
    'secao': 32,     # Verde
    'destaque': 33,  # Amarelo
    'erro': 31,      # Vermelho
    'sucesso': 32    # Verde
}

def find_scripts(root):
    """Procura por arquivos .py na pasta do projeto e retorna uma lista ordenada.
    Exclui o próprio menu, o login e o encerramento (este último é tratado separadamente).
    """
    exclude = {os.path.basename(__file__).lower(), 'login.py', 'encerramento.py'}
    files = []
    try:
        for f in os.listdir(root):
            lf = f.lower()
            # somente arquivos .py
            if not lf.endswith('.py'):
                continue
            if lf in exclude:
                continue
            # ignorar arquivos ocultos e pastas especiais
            if f.startswith('.') or f.startswith('__'):
                continue
            files.append(f)
    except Exception:
        return []
    # ordenar por nome (case-insensitive)
    return sorted(files, key=lambda s: s.lower())


def get_encerramento(root):
    """Procura pelo arquivo Encerramento.py na pasta."""
    try:
        for f in os.listdir(root):
            if f.lower() == 'encerramento.py':
                return f
    except Exception:
        pass
    return None


SCRIPTS = {}  # será preenchido dinamicamente no início do main()
ENCERRAMENTO = None  # será preenchido no início do main()


def clear():
    os.system('cls')


def color(text, tipo='normal'):
    """Colore o texto usando códigos ANSI. Usa as cores definidas em CORES."""
    if tipo in CORES:
        return f"\033[{CORES[tipo]}m{text}\033[0m"
    return text

def mostrar_carregando(texto, duracao=1):
    """Mostra uma mensagem de carregamento com animação de pontos."""
    print(f"\n{texto}", end='', flush=True)
    for _ in range(3):
        time.sleep(duracao/3)
        print(".", end='', flush=True)
    print()


def run_script(filename: str):
    """Executa um script Python e gerencia seu ciclo de vida."""
    path = os.path.join(ROOT, filename)
    if not os.path.exists(path):
        print(color(f"\nErro: Arquivo não encontrado: {filename}", 'erro'))
        input('\nPressione ENTER para voltar ao menu...')
        return

    clear()
    print(color(f"Iniciando {filename}...", 'destaque'))
    mostrar_carregando("Carregando", 1)
    
    try:
        subprocess.run([sys.executable, path])
    except KeyboardInterrupt:
        print(color('\nExecução interrompida pelo usuário.', 'erro'))
    except Exception as e:
        print(color(f'\nErro ao executar {filename}: {e}', 'erro'))
    
    print(color('\nExecução concluída!', 'sucesso'))
    resp = input('\nPressione ENTER para voltar ao menu ou S para sair: ').strip().lower()
    if resp == 's':
        clear()
        print(color('Encerrando sistema...', 'destaque'))
        mostrar_carregando("Saindo", 1)
        sys.exit(0)


def main():
    """Função principal que gerencia o menu interativo."""
    # Detectar scripts disponíveis
    scripts = find_scripts(ROOT)
    encerramento = get_encerramento(ROOT)
    
    if not scripts:
        print(color('Nenhum exercício encontrado na pasta!', 'erro'))
        return

    # Construir menu de opções
    SCRIPTS.clear()
    for i, fname in enumerate(scripts, 1):
        SCRIPTS[str(i)] = fname

    while True:
        clear()
        # Cabeçalho
        print(color('╔═════════════════════════╗', 'titulo'))
        print(color('║     MENU PRINCIPAL      ║', 'titulo'))
        print(color('╚═════════════════════════╝\n', 'titulo'))
        
        # Seção de exercícios
        print(color('▶ Exercícios:', 'secao'))
        for chave in sorted(SCRIPTS, key=lambda x: int(x)):
            print(f"  {chave} - Executar {SCRIPTS[chave]}")
        
        # Seção de encerramento (se existir)
        if encerramento:
            print(color('\n▶ Encerramento:', 'secao'))
            print(f"  E - Executar {encerramento}")
        
        # Opção de saída
        print(color('\n▶ Sistema:', 'secao'))
        print('  0 - Sair')
        
        # Input do usuário
        escolha = input(color('\nEscolha uma opção: ', 'destaque')).strip().lower()

        if escolha == '0':
            clear()
            print(color('Encerrando sistema...', 'destaque'))
            mostrar_carregando("Saindo", 1)
            break

        if escolha == 'e' and encerramento:
            clear()
            print(f'Iniciando {encerramento}...')
            run_script(encerramento)
            continue

        if escolha not in SCRIPTS:
            print('Opção inválida. Tente novamente.')
            input('Pressione ENTER para continuar...')
            continue

        # Ao selecionar, limpamos a tela e executamos o script.
        clear()
        print(f'Iniciando {SCRIPTS[escolha]}... (menu ficará oculto enquanto a atividade roda)')
        run_script(SCRIPTS[escolha])


if __name__ == '__main__':
    clear()
    # Se chamado diretamente, verifica se veio do Login.py
    if fazer_login():
        mostrar_carregando("Iniciando sistema", 1)
        main()
    else:
        print(color('\nAcesso negado.', 'erro'))
        mostrar_carregando("Encerrando", 1)
