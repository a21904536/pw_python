import analise_pasta

def main():
    pasta = analise_pasta.pede_pasta()
    dicionario = analise_pasta.faz_calculos(pasta)
    analise_pasta.guarda_resultados(dicionario, pasta)
    analise_pasta.faz_grafico_queijos(dicionario)
    analise_pasta.faz_grafico_barras(dicionario)

if __name__  == "__main__":
    main()