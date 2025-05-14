import random
numero_secreto = random.randint (1,100)
tentativas = 0
contagem_tentativas = 0
print ("==Bem-Vindo ao Jogo do Numero Secreto==")
print("Tente advinhar o numero secreto entre 1 e 100.")
while tentativas != numero_secreto:
    numero = int(input("Digite um numero: "))
    contagem_tentativas= contagem_tentativas+1
    if numero == numero_secreto:
        print("Parabens, voce acertou o numero secreto")
        print(f"Voce precisou de {contagem_tentativas}")
        break
    elif numero < numero_secreto:
        print ("O numero secreto e maior.")
    else:
        print ("O numero secreto e menor")




