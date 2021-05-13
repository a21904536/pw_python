import os
from os.path import join

def pede_pasta():
    check = True

    while check:
        print("Insira o caminho para a pasta:")
        nome = input()
        if os.path.isdir(nome):
            return nome

def calcula_tamanho_pasta(pasta):
    tamanho = 0
    ficheiros = os.listdir(pasta)

    for ficheiro in ficheiros:
        if os.isfile(join(pasta, ficheiro)):
            tamanho += os.path.getsize(join(pasta, ficheiro)) / 1024

    return tamanho

def main():
    pasta = pede_pasta()
    print("O tamanho total é:" + calcula_tamanho_pasta(pasta))


if __name__ == "__main__":
        main()

