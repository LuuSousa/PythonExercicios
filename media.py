nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
nota3 = float(input('Digite a terceira nota:'))
media = (nota1 + nota2 + nota3) / 3
print('Somando {:.1f} + {:.1f} + {:.1f}, a média do aluno {:.1f}'.format(nota1, nota2, nota3, media))
if 6 > media >= 0:
    print('O Aluno está em REPROVADO!!!')
elif media > 6:
    print('O Aluno está APROVADO!!')

