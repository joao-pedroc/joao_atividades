ano_atual = 2025
ano_nascimento = int(input("Digite seu ano de nascimento"))
idade = ano_atual-ano_nascimento
print (f"Voce tem {idade} anos. ")
if idade <16:
    print ("Voce nao pode votar!")
elif idade <18 or idade>70:
    print("Seu voto e facultativo!")
elif idade >=18:
    print ("Seu voto e obrigatorio!")
    