numero1 = 0
numero2=0
operador = ''
resultado = 0 


print('Bem vindo a calculadora em Python')

while True:
        numero1 = float(input('Digite o primeiro número:'))
        operador= input('Digite qual a operação desejada: ')
        numero2 = float(input('Digite o segundo número:'))

        if operador == '+':
            resultado = numero1+numero2
        elif operador == '-':
            resultado = numero1 - numero2
        elif operador == '*':
            resultado = numero1 * numero2
        elif operador == '/':
            resultado = numero1 - numero2
        else:
            resultado = 'Operação inválida!!'


        print('O valor é:' , str(numero1) + '' + str(operador) + '' + str(numero2)+ '=' + str(resultado)) 

    