from extrator_url import ExtratorURL

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = float(extrator_url.get_valor_parametro("quantidade"))

# considerando apenas conversão dolar - real ou real - dolar // Assim se a moeda destino não for dólar só pode ser real

if (moeda_destino == 'dolar'):
    conversao = float(quantidade)/VALOR_DOLAR
    print('Real: R$ %.2f -- Dolar: $ %.2f' %(quantidade, conversao))
else:
    conversao = float(quantidade)*VALOR_DOLAR
    print('Dolar: $ %.2f -- Real: R$ %.2f' %(quantidade, conversao))
