import csv
import random
import math

### CONSTANTES ###
MIN = 0
MAX = 1
NUMERO_NEURONIOS = 6
##################


def normalizar_dados(dados):
    min_max = obter_min_max_de_cada_atributo(dados)

    for i in range(len(dados)):
        # deixa o atributo alvo de fora (tam vetor dados - 1)
        for j in range(len(dados[i]) - 1):
            dados[i][j] = (min_max[j][MAX] - dados[i][j]) / (min_max[j][MAX] - min_max[j][MIN])

    return dados


def obter_min_max_de_cada_atributo(dados):
    min_max = inicializar_lista_min_max(dados)

    for i in range(len(dados)):
        # deixa o atributo alvo de fora (tam vetor dados - 1)
        for j in range(len(dados[i]) - 1):
            if min_max[j][MAX] < dados[i][j]:
                min_max[j][MAX] = dados[i][j]
            if min_max[j][MIN] > dados[i][j]:
                min_max[j][MIN] = dados[i][j]

    return min_max


def inicializar_lista_min_max(dados):
    minmax = list()
    for i in range(len(dados[0]) - 1):
        minmax.append([999, 0])
    return minmax


# obtem a matriz com os dados convertidos e tratados
def preparar_dados_arquivo_entrada(entrada):
    arquivo = open(entrada, 'r')
    reader = csv.reader(arquivo)

    dados = list()
    for row in reader:
        i = reader.line_num - 1
        dados.append(row)
        for j in range(len(row)):
            # se idade nao informada seta como 0
            if dados[i][j] == '?':
                dados[i][j] = 30
            else:
                dados[i][j] = int(dados[i][j])

    arquivo.close()
    return dados


def separar_lista_atributos(dados):
    atributos = list()
    for linha in dados:
        atributos.append(linha[:-1])
    return atributos


def print_matriz_dados(lista):
    for row in lista:
        print(row)


def obter_matriz_pesos_valores_aleatorios(num_neuronios, tam_entrada):
    matriz = list()

    for i in range(num_neuronios):
        matriz.append(list())
        for j in range(tam_entrada):
            matriz[i].append(random.uniform(0.0, 0.5))

    return matriz


def obter_lista_alvo(lista_dados):
    a = list()
    for row in lista_dados:
        a.append(row[len(row) - 1])
    return a

def calcular_ativacoes(vetor_entrada, pesos):
    ativacoes = list()
    for i_neu in range(len(pesos)):
        ativacoes.append(0)
        for i in range(len(pesos[i_neu])):
            ativacoes[i_neu] += vetor_entrada[i] * pesos[i_neu][i]
    return ativacoes


def inserir_bias_aos_vetores_entrada(lista):
    for i in range(len(lista)):
        lista[i].insert(0, -1.0)
    return

def sinal(valor):
    retorno = 1
    if valor <= 0:
        retorno = 0
    return retorno

def calcular_saidas(ativacoes):
    y = list()
    for i_neu in range(len(ativacoes)):
        y.append(sinal(ativacoes[i_neu]))
    return y


def calcular_erros(saidas, desejado):
    erros = list()
    for i in range(len(saidas)):
        d_i = 0
        if desejado == i + 1:
            d_i = 1
        erros.append(d_i - saidas[i])
    return erros


def atualizar_pesos(pesos, tx_aprendizagem, erros, entrada):
    for i_neu in range(len(pesos)):
        for i in range(len(pesos[i_neu])):
            pesos[i_neu][i] = pesos[i_neu][i] + tx_aprendizagem * erros[i_neu] * entrada[i]


def treinar_rede(lista_treinamento, treinamento):

    num_acertos = 0
    num_testes = 0
    for vetor_entrada in lista_treinamento:
        # vetor_entrada[:-1] = remove o ultimo valor do vetor (atributo alvo) do calculo da ativacao
        ativacoes_neuronios = calcular_ativacoes(vetor_entrada[:-1], lista_pesos)

        lista_saida = calcular_saidas(ativacoes_neuronios)

        acertou = acertou_previsao(lista_saida, vetor_entrada[-1])

        if acertou:
            num_acertos += 1
        num_testes += 1

        if treinamento:
            # vetor_entrada[-1] = ultimo item do vetor = atributo alvo
            lista_erros = calcular_erros(lista_saida, vetor_entrada[-1])
            atualizar_pesos(lista_pesos, N, lista_erros, vetor_entrada[:-1])

    return num_acertos / num_testes


def acertou_previsao(lista_saida, valor):
    acertou = True
    #print(lista_saida)
    for index in range(len(lista_saida)):
        if valor - 1 != index:
            if lista_saida[index] > 0:
                acertou = False
        elif lista_saida[index] != 1:
            acertou = False
    return acertou


#################################### inicio main #################################################
N = 0.01

dados = preparar_dados_arquivo_entrada('dermatology.data')
dados = normalizar_dados(dados)

#print_matriz_dados(dados)

lista_pesos = obter_matriz_pesos_valores_aleatorios(NUMERO_NEURONIOS, len(dados[0]))
inserir_bias_aos_vetores_entrada(dados)


t = 0

tam_trein = math.floor(len(dados) * 0.7)

rodadas = 0
while rodadas < 100:
    index_alvo = len(dados) - 1
    dados.sort()
    print_matriz_dados(dados)
    #for i in range(len(dados[0])):
    #    for j in range(len(dados)):

    #andom.shuffle(dados)

    treinamento = dados[:tam_trein]
    teste = dados[tam_trein:]

    print('Treinamento ' + str(rodadas) + ': ')
    #print(treinar_rede(treinamento, True))
    print('Teste ' + str(rodadas) + ': ')
    #print(treinar_rede(teste, False))
    print()

    rodadas += 1
