import random

def jogar():

    tipo_jogo = mensagem_abertura()
    palavra = carrega_sorteia_palavra(tipo_jogo)
    
    letras_acertadas = inicializa_letras_acertadas(palavra)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    letras_usadas = []
    
    while(not enforcou and not acertou):

        chute = captura_chute()
        

        if(chute in palavra):
            marca_chute_correto(palavra, chute, letras_acertadas)
        else:
            
            erros = chute_errado(letras_usadas, erros, chute)
            

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print_message_winner()
    else:
        print_message_loser(palavra)

def desenho_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def print_message_loser(palavra_secreta):
    print("Você foi ENFORCADO!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("A palavra secreta era {}".format(palavra_secreta))
    
def print_message_winner():
    print("Você GANHOU!")
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def chute_errado(letras_usadas, erros, chute):
     
    if (chute in letras_usadas):
        print("Letra {} já foi usada".format(chute))
        print("Letras usadas: {}".format(letras_usadas))
        desenho_forca(erros)
        return erros
    else:
        erros += 1
        print("Letra {} não encontrada. Chances restantes: {}".format(chute,7-erros))
        print("Letras erradas:{}, {}".format(", ".join(letras_usadas), chute))
        desenho_forca(erros)

    letras_usadas.append(chute)
    return erros
        
def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def captura_chute():
    chute = input("Escolha uma letra:")
    chute = chute.strip().upper()
    return chute

def mensagem_abertura():
    print("***********************************")
    print("Bem vindo ao jogo da Forca!")
    print("***********************************")
    print("Qual tipo de palavras?")
    print(" 1 - FRUTAS | 2 - PAÍSES | 3 - ESTADOS BRASILEIROS")
    tipo_jogo = int(input("Defina um tipo de palavra:"))
    return tipo_jogo

def carrega_sorteia_palavra(tipo_jogo):
    if (tipo_jogo == 1):
        arquivo = open("frutas.txt", "r")
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
        
        arquivo.close()

    elif (tipo_jogo == 2):
        arquivo = open("paises.txt", "r")
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()
    
    else:
        arquivo = open("estados_br.txt", "r")
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()

    #arquivo = open("palavras.txt", "r")
    #palavras = []

    #for linha in arquivo:
    #    linha = linha.strip()
    #    palavras.append(linha)

    #arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

if(__name__ == "__main__"):
    jogar()