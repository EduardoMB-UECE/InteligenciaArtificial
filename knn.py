import csv
import random
import math

arquivo = open('iris.csv', 'r')
leitor = csv.reader(arquivo)

# Lista com todos os valores do arquivo de classificacao_Q3
listaCompleta = list(leitor)


def calcularDistancia(p1, p2):
    acumulada = 0
    for i in range(len(p2)):
        parcial = float(p2[i]) - float(p1[i])
        parcial *= parcial
        acumulada += parcial
    return math.sqrt(acumulada)

def obterPontoMaisProximo(ponto, lista):
    menor = lista[0]
    for item in lista:
        distancia = calcularDistancia(item, ponto)
        if distancia < calcularDistancia(menor, ponto):
            menor = item
    return menor

tam = 150
treinamento = 15

qtdAcertos = 0
qtdErros = 0

while treinamento < tam:

    qtdAcertoMax = 0
    qtdAcertoMin = 151
    # Quantidade acertos totais das 30 rodadas para retirar a media.
    qtdTotalAcertos = 0

    qtdAcertoPorClasse = [0, 0, 0]
    qtdTestePorClasse = [0, 0, 0]

    print('Execucao com tamanho de treinamento: ' + str(treinamento))
    # Executa 30 vezes para obter taxa de acerto medias max e min + medias por classe
    for repeticao in range(30):

        # Faz o embaralhamento da base completa e separa as bases para treinamento e teste
        random.shuffle(listaCompleta)
        listaTreinamento = listaCompleta[:treinamento]
        listaTeste = listaCompleta[treinamento:]

        # Quantidade de acerto por rodada
        qtdAcertos = 0

        for x in listaTeste:
            resultado = obterPontoMaisProximo(x, listaTreinamento[:1])

            # Acerto
            if x[4] == resultado[4]:
                qtdAcertos += 1
                qtdTotalAcertos += 1
                qtdAcertoPorClasse[int(x[4]) - 1] += 1

            # Teste
            qtdTestePorClasse[int(x[4]) - 1] += 1

        if (qtdAcertoMax < qtdAcertos):
            qtdAcertoMax = qtdAcertos
        if (qtdAcertoMin > qtdAcertos):
            qtdAcertoMin = qtdAcertos

    print('Taxa média acertos: ' + str((qtdTotalAcertos / 30) / (tam - treinamento)))
    print('Taxa de acerto max: ' + str(qtdAcertoMax / (tam - treinamento)))
    print('Taxa de acerto min: ' + str(qtdAcertoMin / (tam - treinamento)))
    print('Taxa de acerto por classe:')

    for i in range(len(qtdAcertoPorClasse)):
        print(str(i+1) + ' ' + str(qtdAcertoPorClasse[i] / qtdTestePorClasse[i]))

    treinamento += 15