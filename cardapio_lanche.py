opcao = 0
while opcao != 5:
    print ("===Cardapio===")
    print ("1- hambuerguer")
    print ("2- pizza")
    print ("3- salada")
    print ("4- refrigerante")
    print ("5- sair")
    opcao = int(input("Escolha uma opcao: "))
    if opcao == 1:
        print ("Voce escolheu hamburguer!!")
    elif opcao == 2:
        print("Voce escolheu pizaa.")
    elif opcao == 3:
        print("Voce escolheu salada.")
    elif opcao == 4:
        print("Voce escolheu refrigerante.")
    elif opcao == 5:
        print("Saindo do cardapio.")
        break