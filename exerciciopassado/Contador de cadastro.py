import os
os.system('cls')

pessoas = []
soma_idades = 0

while True:
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))

    sexo = input("Sexo [M/F]: ").strip().upper()
    while sexo not in ("M", "F"):
        sexo = input("Sexo inválido. Digite apenas M ou F: ").strip().upper()

    pessoas.append({"nome": nome, "idade": idade, "sexo": sexo})
    soma_idades += idade

    if input("Quer continuar? [S/N]: ").strip().upper() == "N":
        break

print("-=" * 30)

media = soma_idades / len(pessoas)
mulheres = [p["nome"] for p in pessoas if p["sexo"] == "F"]
acima_media = [p for p in pessoas if p["idade"] > media]

print(f"A) Total de pessoas cadastradas: {len(pessoas)}")
print(f"B) Média de idade: {media:.2f}")
print(f"C) Mulheres cadastradas: {', '.join(mulheres) if mulheres else 'nenhuma'}")
print("D) Pessoas acima da média:")
for p in acima_media:
    print(f"   Nome: {p['nome']}; Sexo: {p['sexo']}; Idade: {p['idade']}")