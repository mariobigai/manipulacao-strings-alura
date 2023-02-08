url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

#Separando a base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:] # indice_interrogacao + 1 para pular o '?'
print(url_parametros)

#Extraindo os valores dos parâmetros
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1 # +1 para pular o '='
indice_e_comercial = url_parametros.find('&', indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)