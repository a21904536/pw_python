from .acessorio import ler_texto
from collections import Counter

def calcula_linha(nomeFicheiro):
    with open(nomeFicheiro) as f:
        text = f.readLines()
        return len(text)

def calcula_carateres(nomeFicheiro):
    countCarateres = 0
    with open(nomeFicheiro) as f:
        text = f.readLines()
        for linha in text:
            countCarateres += len(linha)

    return countCarateres


def calcula_palavra_comprida(nomeFicheiro):
    texto = ler_texto(nomeFicheiro)
    listaPalavras = texto.split()
    palavraMaisComprida = max(listaPalavras, key = len())

    return palavraMaisComprida


def calcula_ocorrencia_de_letras(nomeFicheiro):
    texto = Counter(nomeFicheiro)
    print(texto)




