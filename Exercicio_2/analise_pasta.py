import os
import csv
from os import *
from os.path import join
from matplotlib import pyplot as plt

def pede_pasta():
    print("Insira o caminho para a pasta:")
    return input()

def faz_calculos(caminho):
    dic_info = {}
    caminho = pede_pasta()
    ficheiros = os.listdir(caminho)

    for ficheiro in ficheiros:
        if os.isfile(join(caminho, ficheiro)):
            tipo = os.path.splittext(ficheiro)
            if tipo[1] in dic_info:
                dic_info[tipo[1]]["volume"] += os.path.getsize(join(caminho, ficheiro))/1024
                dic_info[tipo[1]]["quantidade"] += 1
            else:
                dic_info[tipo[1]] = {}
                dic_info[tipo[1]]["volume"] = os.path.getsize(join(caminho, ficheiro))/1024
                dic_info[tipo[1]]["quantidade"] = 1

    return dic_info

def guarda_resultados(dicionario, caminho):
    nome = os.path.basename(path)
    nome += ".csv"
    try:
        file = open(nome, 'w', newline='')
        fields = ["Extensao", "Quantidade", "Tamanho[kByte]"]
        writer = csv.DictWriter(file, fields)
        writer.writeheader()
        for ext in dicionario:
            newLine = [ext, str(dicionario[ext]["quantidade"]), str(dicionario[ext]["volume"])]
            writer = csv.DictWriter(file, newLine)
            writer.writeheader()
        print(f"Os Resultados Foram Guardados No Ficheiro: ´{nome}`")
    except OSError:
        print("Error Creating CSV File")

def faz_grafico_queijos(dicionario):
    listaChaves = []
    listaValores = []

    for tamanho in dicionario:
        listaChaves.append(tamanho)
        listaValores.append(dicionario[tamanho]["volume"])

    plt.pie(listaValores, labels=listaChaves, autopct='%1.0f%%')
    plt.title("Tipos de ficheiros")
    plt.show()

def faz_grafico_barras(dicionario):
    listaChaves = []
    listaValores = []

    for tamanho in dicionario:
        listaChaves.append(tamanho)
        listaValores.append(dicionario[tamanho]["quantidade"])

    plt.bar(listaChaves, listaValores)
    plt.title("Tipos de ficheiros")
    plt.show()
