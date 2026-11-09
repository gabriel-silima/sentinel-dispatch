"""SENTINEL DISPATCH — atividade acadêmica da Aula 06 (SENAC/PMGO)."""

while True:
    try:
        entrada = input("Qual o prefixo numérico da viatura para despacho? ")
        numero = int(entrada)

        if numero == 999:
            print("Despacho encerrado. Retornando à base.")
            break

        print(f"Viatura {numero} despachada com sucesso.")

    except ValueError:
        print("Prefixo inválido. O sistema aceita apenas números.")
        continue
