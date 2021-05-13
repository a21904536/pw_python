def pede_nome(nomeFicheiro):
    verificacao = False
    while verificacao:
        if not (nomeFicheiro is None):
            print(f"{nomeFicheiro}")
            verificacao = True


def gera_nome(nomeFicheiro):
    fileName = ""
    if not(nomeFicheiro is None):
        fileName = nomeFicheiro.split(".")[0] + ".json"
        return fileName


def ler_linhas(nomeFicheiro):
    f = open(nomeFicheiro, encoding = "utf-8")
    lista = f.readlines()
    f.close
    return lista

def ler_texto(nomeFicheiro):
    f = open(nomeFicheiro, encoding = "utf-8")
    text = f.read()
    f.close
    return text