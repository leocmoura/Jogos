import random

def jogar():

    mensagem_abertura()

    palavra_secreta = carrega_sorteia_palavra()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = captura_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            print("Letra não encontrada. Chances restantes: {}".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print_message_winner()
    else:
        print_message_loser(palavra_secreta)

def print_message_loser(palavra_secreta):
    print("Você perdeu!")
    print("A palavra era {}".format(palavra_secreta))
    
def print_message_winner():
    print("Você ganhou!")

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

def carrega_sorteia_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

if(__name__ == "__main__"):
    jogar()