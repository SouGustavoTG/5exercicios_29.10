import os
import sys
import subprocess

os.system('cls')

ROOT = os.path.dirname(__file__)

def find_scripts(root):
    """Procura por arquivos E*.py na pasta do projeto e retorna uma lista ordenada."""
    files = []
    try:
        for f in os.listdir(root):
            lf = f.lower()
            if lf.startswith('e') and lf.endswith('.py'):
                files.append(f)
    except Exception:
        return []
    return sorted(files)


SCRIPTS = {}  # será preenchido dinamicamente no início do main()


def clear():
    os.system('cls')


def color(text, code=32):
    # Retorna texto colorido em terminals que suportam ANSI. code 32 = verde por padrão.
    return f"\033[{code}m{text}\033[0m"


def run_script(filename: str):
    path = os.path.join(ROOT, filename)
    if not os.path.exists(path):
        print(f"Arquivo não encontrado: {filename}")
        input('Pressione ENTER para voltar ao menu...')
        return
    # Executa com o mesmo interpretador Python
    try:
        subprocess.run([sys.executable, path])
    except KeyboardInterrupt:
        # Permitir que o usuário saia com Ctrl+C dentro do script
        print('\nExecução interrompida pelo usuário.')
    # Depois que o script terminar, só voltamos ao menu quando o usuário pedir
    resp = input('\nPressione ENTER para voltar ao menu ou digite S para sair: ').strip().lower()
    if resp == 's':
        sys.exit(0)


def main():
    # detectar scripts automaticamente
    scripts = find_scripts(ROOT)
    if not scripts:
        print('Nenhum arquivo E*.py encontrado na pasta.')
        return
    # construir dicionário de opções
    SCRIPTS.clear()
    for i, fname in enumerate(scripts, 1):
        SCRIPTS[str(i)] = fname

    while True:
        clear()
        print('=== MENU PRINCIPAL ===')
        for chave in sorted(SCRIPTS, key=lambda x: int(x)):
            print(f"{chave} - Executar {SCRIPTS[chave]}")
        print('0 - Sair')
        escolha = input('\nEscolha uma opção: ').strip()

        if escolha == '0':
            print('Saindo...')
            break

        if escolha not in SCRIPTS:
            print('Opção inválida. Tente novamente.')
            input('Pressione ENTER para continuar...')
            continue

        # Ao selecionar, limpamos a tela e executamos o script.
        clear()
        print(f'Iniciando {SCRIPTS[escolha]}... (menu ficará oculto enquanto a atividade roda)')
        run_script(SCRIPTS[escolha])


if __name__ == '__main__':
    main()
