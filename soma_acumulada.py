soma = 0
numero = 1
while numero !=0:
    numero= int(input("Digite um numero(0 para sair)"))
    soma = soma + numero
    if numero !=0:
        print (f"A soma ate o momento é {soma}")
    print (f"A soma dos numero digitados é {soma}")