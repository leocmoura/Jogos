import random

def jogar():

    print("***********************************")
    print("Bem vindo ao jogo de ADIVINHAÇÃO!")
    print("***********************************")
        
    numero_secreto = random.randrange(0,101)
    chances = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print(" 1 - EASY | 2 - MEDIUM | 3 - HARD")

    nivel = int(input("Defina um nível:"))
    if(nivel == 1):
        numero_secreto = random.randrange(0,101)
        intervalo = 100
        chances = 20
        print("Você tem {} tentativas".format(chances))
    elif(nivel == 2):
        numero_secreto = random.randrange(0,501)
        intervalo = 500
        chances = 10
        print("Você tem {} tentativas".format(chances))
    else:
        numero_secreto = random.randrange(0,1001)
        intervalo = 1000
        chances = 5
        print("Você tem {} tentativas".format(chances))

    for rodadas in range(1, chances + 1):
        print("Rodada {} de {} ".format(rodadas, chances))
        chute_str = input("Digite um número entre 1 e {}:".format(intervalo))
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > intervalo):
            print("Você deve digitar um número entre 1 e {}!".format(intervalo))
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto
        game_over = rodadas == chances

        if(acertou):
            print("Você ACERTOU e sua PONTUAÇÃO FOI: {}".format(pontos))
            break
        else:
            if(maior):
                print("Você ERROU! O seu chute foi MAIOR")
                if(game_over):
                    print("O número secreto era {}. Pontuação: {}".format(numero_secreto, pontos))
            elif(menor):
                print("Você ERROU! O seu chute foi MENOR")
                if (game_over):
                    print("O número secreto era {}. Pontuação: {}".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    print("Fim do Game!")

if(__name__ == "__main__"):
    jogar()