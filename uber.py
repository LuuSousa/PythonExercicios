'''Sabemos que andar somente por aplicativo nos dá muitas facilidades, 
como não precisar investitr em garagem, seguro e nem encontrar um bom mecânico. 
Além disso, o custo fixo em andar por aplicativo é zero, porém o custo variável é bem mais alto do que ao possuir um carro. 
Sem contar que ao investir o dinheiro ao invés de comprar um carro à vista, isso ainda geraria uma renda pelos investimentos, 
que seria utilizada para abater parte dos custos da viagem pelo Uber.

Vamos aos números:
Valor base de um veículo: R$ 41.150,00
Seguro anual do veículo: 8%
Custo de combustível por km: R$ 0,32
Custo de revisão por km: R$ 0,42
Estacionamento anual: R$ 3600,00
IPVA (anual): 1528,40

Custo por km utilizando um aplicativo: R$ 1,92
Rendimento anual do investimento: 13,65%

Percebe-se que se o usuário percorre pequenas distâncias mensalmente, vale muito a pena andar por aplicativo e não se preocupar em possuir um veículo.

Construa um programa que, com base nos dados acima, pergunta ao usuário quantos km ele anda por mês e o informa qual é a opção mais indicada.
'''


km_por_mes = float(input("Quanto km por mês você roda? "))

valor_base_veiculo = 41150
seguro_anual = valor_base_veiculo * 0.08
custo_combustivel = 0.32 * km_por_mes
custo_revisao = 0.42 * km_por_mes
estacionamento_anual = 3600
ipva_anual = 1528.40

custo_total_carro = valor_base_veiculo / 12 + seguro_anual / 12 + custo_combustivel + custo_revisao + estacionamento_anual / 12 + ipva_anual / 12

print('Custo do carro por mês: {:.2f}'.format(custo_total_carro))

custo_uber_km = 1.92 * km_por_mes
rendimento_anual_investimento = valor_base_veiculo * 0.1365
rendimento_mensal_investimento = rendimento_anual_investimento / 12
custo_rendimento_uber = rendimento_mensal_investimento - custo_uber_km

print('O custo mensal por mês com uber: {:.2f}'.format(custo_uber_km))
print('O valor por km utilizando do rendimento mensal: {:.2f}'.format(custo_rendimento_uber))

if custo_rendimento_uber >= 0:
    print('É melhor andar de uber ')
else:
    print('É melhor você comprar um carro')
