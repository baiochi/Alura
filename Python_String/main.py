# terminal colors
WHITE = '\033[39m'
CYAN = '\033[36m'
GREEN = '\033[32m'
RED = '\033[31m'

from url_extractor import UrlExtractor

print()

url = 'http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'


extractor = UrlExtractor(url)

print(f'{CYAN}Base url:{WHITE} {extractor.get_base_url()}')

print(f'{CYAN}Params:{WHITE} {extractor.get_url_params()}')

print(len(url))

print(extractor)