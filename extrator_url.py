import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url);
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("URL vazia")

        padrao = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        combinou = padrao.match(self.url)

        if not combinou:
            raise ValueError("A URL não é valida")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        return self.url[:indice_interrogacao]

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        return self.url[indice_interrogacao+1:]

    def get_valor_parametros(self, parametro_busca):
        indice_parametro = self.url.find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1  # +1 para pular o '='
        indice_e_comercial = self.url.find('&', indice_valor)
        if indice_e_comercial == -1:
            return self.url[indice_valor:]
        else:
            return self.url[indice_valor:indice_e_comercial]


url = "https://www.bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator = ExtratorURL(url)
#print(extrator.get_valor_parametros('quantidade'))