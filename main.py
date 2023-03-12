
import datetime

while True:
    nome = input("Digite seu nome e sobrenome: ")
    ano_nasc = input("Digite o ano de nascimento (entre 1922 e 2021): ")

    if not ano_nasc.isdigit():
        print("Informação inválida. Tente novamente.")
        continue

    ano_nasc = int(ano_nasc)

    if ano_nasc < 1922 or ano_nasc > 2021:
        print("Informação inválida. Tente novamente.")
        continue

    idade = datetime.date.today().year - ano_nasc

    print(f"\nNome Completo: {nome}")
    print(f"Idade: {idade} anos \n")


