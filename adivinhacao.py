from random import randint

numeroMagico = randint(0, 10)
print("Bem-vindo ao jogo do número mágico.")
print("Estou pensando em um número , você precisa adivinhar =)")
acertou = False
erros = 0
while not acertou:
    jogador = int(input(" e ai qual é o seu palpite ? "))
    erros += 1
    if jogador == numeroMagico:
        acertou = True
    else:
        if jogador < numeroMagico:
            print("ta frio hemmm , tenta um número maior")
        elif jogador > numeroMagico:
            print("ta queeente , ja ta proximo ")
        if erros == 5:
            print("Você perdeu!!!")
            break
print("Acertou com {} erros. Parabéns!!!".format(erros))
