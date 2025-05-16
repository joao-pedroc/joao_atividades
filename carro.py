# Exibir a tabela de preços
print("\n--- Tabela de preços ---")
print("Valor por dia alugado: R$90.00")
print("Valor por Km rodado: R$0.20")

# Solicita os dados ao usuário
dias = int(input("\nQuantos dias o carro foi alugado? "))
Kms = float(input("Quatos KMs foram percorridos? "))

# Calcula os valores
valor_dias = dias* 90.00
valor_Kms = Kms* 0.20
total = valor_dias +valor_Kms

# Exibe o recibo detalhado
print("\n--- Recibo do Aluguel ---")
print(f"Total de dias alugados: {dias} dia(s) - R$ {valor_dias:.2f}")
print(f"Total de KMs percorridos: {Kms:.2f} km - R$ {valor_Kms:.2f}")
print(f"\nValor total a pagar: R$ {total:.2f}")