palavrachave = "amor"
resposta = ["_"] * len(palavrachave)
erros = []
tentativas = 6

while True:
    print(" ".join(resposta))
    print(f"Erros: {' - '.join(erros)}")
    print(f"Tentativas restantes :{tentativas}")
    entrada_usuário = input("Digite uma letra: ")
    acertou = False

    for index, letra_secreta in enumerate(palavrachave):
        if entrada_usuario == letra_secreta:
            resposta[index] = entrada_usuario
            acertou = True

    if not acertou:
        tentativas -= 1
        erros.append(entrada_usuario)

    if tentativas == 0:
        print("Você Perdeu ! ")
        break

    if "".join(resposta) == palavrachave:
        print("Você Venceu! ")
        break

print(print(" ".join(resposta)))
print(f"Erros: {' - '.join(erros)}")
