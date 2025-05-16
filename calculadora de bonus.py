# Entrada de dados
nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: R$ "))
total_vendas = int(input("Digite o total de vendas efetuadas: "))
# Verificação da meta
if total_vendas >= 20:
    bonus = 0.15 * salario_fixo
    salario_recebido = salario_fixo + bonus
    print("\nMeta atingida!")
    print(f"Vendedor: {nome}")
    print(f"Salário final: R$ {salario_recebido:.2f}")
    print(f"Bônus (15%): R$ {bonus:.2f}")
else:
    print("\nMeta não foi atingida.")
    print(f"Vendedor: {nome}")