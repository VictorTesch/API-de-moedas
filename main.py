import requests
import json
import pandas as pd

# resultado = requests.get(f'https://www.receitaws.com.br/v1/cnpj/'
# json.loads((requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}')).text)

''' ETL = Extract, Transform and Load'''

cambio = json.loads((requests.get(f'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')).text)
dolar = float(cambio['USDBRL']['high'])
euro = float(cambio['EURBRL']['high'])
bitcoin = float(cambio['BTCBRL']['high'])

df = pd.read_csv('C:\\teste\\victor\\API-de-moedas\\historico.csv')
listadf = df.values.tolist()

def dolarreal():
    real = float(input('Digite um Valor:'))
    print('O Real para Dolar na cotação atual é de:', real*dolar)

def realdolar():
    real = float(input('Digite um Valor:'))
    print('O Dolar para Real na cotação atual é de:', real/dolar)

def realeuro():
    real = float(input('Digite um Valor:'))
    print('O Real para Euro na cotação atual é de:', real/euro)

def euroreal():
    real = float(input('Digite um Valor:'))
    print('O Euro para Real na cotação atual é de:', real*euro)

def realbitcoin():
    real = float(input('Digite um Valor:'))
    print('O Real para Bitcoin na cotação atual é de:', real/bitcoin)

def bitcoinreal():
    real = float(input('Digite um Valor:'))
    print('O Bitcoin para Real na cotação atual é de:', real*bitcoin)

print('1 - Para converter de Real Para Dolar')
print('2 - Para converter de Dolar Para Real')
print('3 - Para converter de Real Para Euro')
print('4 - Para converter de Euro Para Real')
print('5 - Para converter de Bitcoin Para Real')
print('6 - Para converter de Real Para Bitcoin')


a = input('Escolha sua função:')
if a == '1':
    rr = realdolar()
    listadf.append(str(rr))

if a == '2':
    rr = dolarreal()
    listadf.append(str(rr))

if a == '3':
    rr = realeuro()
    listadf.append(str(rr))

if a == '4':
    rr = euroreal()
    listadf.append(str(rr))

if a == '5':
    rr = bitcoinreal()
    listadf.append(str(rr))
    
if a == '6':
    rr = realbitcoin()
    listadf.append(str(rr))

dffinal = pd.DataFrame(listadf)
dffinal.to_csv('C:\\teste\\victor\\API-de-moedas\\historico.csv')