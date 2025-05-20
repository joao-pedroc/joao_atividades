opcao=-1
while opcao !=0:
    print("--- Calculadora ---")
    print("1 - Somar")
    print("1 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")
    
    opcao = int(input("Escolha uma opçâo: "))

    if opcao == 0:
        print ("Programa encerrado!")
        break

    elif opcao == 1:
        num1 = int(input("Escolha o primeiro numero: "))
        num2 = int(input("Escolha o segundo numero: "))
        resultado = (num1 + num2)
        print (f"Seu resultado é = {resultado}")
    elif opcao == 2:
        num1 = int(input("Escolha o primeiro nemero: "))
        num2 = int(input("Escolha o segundo numero:"))
        resultado = (num1 - num2)
        print (f"Seu resultado é = {resultado}")
    elif opcao ==3:
        num1 = int(input("Escolha o primeiro numero:"))
        num2 = int(input("Escolha o segundo numero:"))
        resultado = (num1 / num2)
        print (f"Seu resultado é = {resultado}")
    else:
        print ("Numero de opção inválida!")