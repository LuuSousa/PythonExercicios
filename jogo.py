from random import randint

computador = randint(0, 10)
print("Sou seu computador... Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhac qual foi?")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual é seu palpite?"))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("ta friooo , digite um número maior .")
        elif jogador > computador:
            print("ta quentee , digite um número menor")
        if palpites < 6:
            print("Você perdeu!!!")
            break
print("Acertou com {} Erros. Parabéns!".format(palpites))
