import json

f = open('dados.json')
data = json.load(f)

def buscarMenorFatura(data):
    menorFaturamento = data[0]['valor']
    dia = ""
    for i in data:
        if i['valor'] < menorFaturamento and i['valor'] != 0:
            menorFaturamento = i['valor']
            dia = i['dia']
    return [menorFaturamento, dia]

def buscarMaiorFatura(data):
    menorFaturamento = data[0]['valor']
    dia = ""
    for i in data:
        if i['valor'] > menorFaturamento and i['valor']:
            menorFaturamento = i['valor']
            dia = i['dia']
    return [menorFaturamento, dia]

def buscarQtdDiasSemFaturamento(data):
    diasSemFaturamento = 0
    for i in data:
        if i['valor'] == 0:
            diasSemFaturamento +=1
    return diasSemFaturamento

def calcularMediaMensal(data):
    soma = 0
    diasCalculaveis = len(data) - buscarQtdDiasSemFaturamento(data)
    for i in data:
        if i['valor'] != 0:
            soma += i['valor']
    return soma / diasCalculaveis

def diasFaturamentoMaiorQueMedia(data):
    qtdDias = 0
    for i in data:
        if i['valor'] > calcularMediaMensal(data):
            qtdDias +=1
    return qtdDias

menorFatura = buscarMenorFatura(data)
maiorFatura = buscarMaiorFatura(data)
dias = diasFaturamentoMaiorQueMedia(data)

print(f'O menor faturamento foi R${menorFatura[0]:,.2f} no dia {menorFatura[1]}')
print(f'O maior faturamento foi R${maiorFatura[0]:,.2f} no dia {maiorFatura[1]}')
print(f'Neste mês, o faturamento de {dias} dias foi maior que o faturamento mensal')