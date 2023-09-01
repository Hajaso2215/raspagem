import requests
from bs4 import BeautifulSoup as bs
from lxml import html
import re

url = 'https://fbref.com/pt/jogadores/72d0e1b6/gabriel-barbosa'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

requisicao = requests.get(url, headers=headers)

site = bs(requisicao.text, "html.parser")

# Encontre o nome do jogador
nome_jogador = site.find('div', id='meta').find('strong').text.strip()

# Usar XPath para encontrar a posição do jogador
pagina = html.fromstring(requisicao.content)
posicao = pagina.xpath('//*[@id="meta"]/div[2]/p[2]/text()')
pe = pagina.xpath('//*[@id="meta"]/div[2]/p[2]/text()')
peso_text = pagina.xpath('//*[@id="meta"]/div[2]/p[3]/text()')


if  posicao:
    posicao = posicao[0].strip()
    pe = pe[1].strip()
    
    # Extrair apenas o valor numérico do peso
    peso_match = re.search(r'(\d+)lb', peso_text[0])
    if peso_match:
        peso_lb = float(peso_match.group(1))
        peso_kg = round(peso_lb * 0.45359237, 2)
        peso = f"{peso_kg} kg"
        
        
    else:
        peso = "Peso não encontrado"
else:
    posicao = "Posição não encontrada"
    pe = "Pé não encontrado"
    peso = "Peso não encontrado"


print("Nome do Jogador:", nome_jogador)
print("Posição:", posicao)
print("Pé favorito:", pe)
print("Peso:", peso)
#print("Data de Nacimento:", dt_nascimentp)