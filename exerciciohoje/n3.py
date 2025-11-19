def leiaInt(msg):
    while True:
        valor = input(msg).strip()
        if valor.lstrip('-').isdigit():   # permite números negativos
            return int(valor)
        else:
            print("Erro! Digite um número válido.")

# Programa principal
n = leiaInt("Digite um número: ")
print(f"Você digitou o número: {n}")