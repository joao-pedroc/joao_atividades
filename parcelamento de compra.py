# Solicita ao usoario o valor total da compra 
valor_total = float(input("Digite o valor total a compra; R$ "))

# Calcula o valor de cada uma das 5 pretações (sem juros)
prestacao = valor_total / 5

#Exibe os resultados 
print("\nresumo da Compra: ") 
print(f"valor total da compra: R$ {valor_total:.2f}")
print("valor de cada prestações: R$ {prestacao:.2f}")