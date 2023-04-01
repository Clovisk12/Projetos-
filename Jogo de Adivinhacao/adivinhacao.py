import random
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

pontosiniciais=1000


print("Defina o Nivel do Jogo")
print("Nivel (1) Facil , Nivel (2) Medio, Nivel (3) Dificil")

Nivel= int(input("Digite o Valor do Nivel:"))

if (Nivel==1):
    tentativa = 20
elif ( Nivel==2):
    tentativa = 10
else:
    tentativa = 5

numero_secreto = round(random.random() * 100)
rodada=1

while (rodada <= tentativa):
    print("Tetantiva {} de {}".format(rodada,tentativa))
    rodada += 1
    chute = int(input("Digite o seu número: "))
    if (chute <= 0 or chute >= 100):
        print("Digite um numero Valido de 1 ate 100")
        continue
    print("Seu numero", chute)
    diferenca = abs(chute - numero_secreto)

    if(numero_secreto ==chute) :
        print("voce acertou")
        break
    else:
        if(numero_secreto < chute):
            print("errou! Seu numero foi maior!")
        elif (diferenca <= 10):
            print("errou! Seu numero está proximo!")
        elif(numero_secreto > chute):
            print("errou! Seu numero foi menor!")


    pontosiniciais -= diferenca

print("Fim do Jogo")
print( "Voce fez {} Pontos".format(pontosiniciais))