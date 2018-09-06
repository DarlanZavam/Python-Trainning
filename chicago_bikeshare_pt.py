# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

# ------Solução T1------
count= -1
for line in data_list:
    count += 1
    if count <= 19:
        print("Linha {}:\n{}".format(count,line))
#----------------------------

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

# ------Solução T2-------
count = -1
for line in data_list:
    count += 1
    if count <= 19:
        data_genre = data_list[count]
        print("Linha {}: {}".format(count,data_genre[6]))
#---------------------------

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem

# -------Solução T3-----------
def column_to_list(data:list, index:int):
    """
    Função para transformar um colunas de uma lista em um lista somente.
    Argumentos:
        data: Lista contendo os dados, o input é preciso ser uma lista.
        index: Número da coluna desejada para isolar, necessário ser um numero inteiro.
    Retorna:
        Uma lista dos valores referentes a coluna que se pretende isolar.
    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for line in data:
        column_list.append(line[index])
    return column_list
#---------------------------------

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.

# -------Solução T4-------
male = 0
female = 0
for line in data_list:
    if line[-2] == "Male":
        male += 1
    elif line[-2] == "Female":
        female += 1
#--------------------------------    

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)

# -------Solução T5-------
def count_gender(data_list:list):
    """
    Função específica para conta gênero de uma coluna de um dataset também específico.
    Argumento:
        data_list: É a lista na qual será contada o numero de gêneros.
    Retorna:
        Duas variáveis de valor inteiro que foram usadas como contadores no processo da função
        no qual cada variável é referente ao valor de ocorrência de cada gênero da lista.
    """
    male = 0
    female = 0
    for line in data_list:
        if line[-2] == "Male":
            male += 1
        elif line[-2] == "Female":
            female += 1
        
    return [male, female]
#--------------------------------

print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.

# -------Solução T6------------
def most_popular_gender(data_list:list):
    """
    Função que diz qual o gênero de usuário de um dataset e mais popular.
    Argumento:
        data_list: lista de dados no qual será extraido os gêneros.
    Retorna:
        Uma string que é referenciada pela avaliação booleana de duas variáveis,
        a maior das variáveis será apresentada como respota da função.
    """
    male, female = count_gender(data_list)
    if male > female:
        gender = "Masculino"
    elif female > male:
        gender = "Feminino"
    else:
        gender = "Igual"
    answer = gender
    return answer
#----------------------------------

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

# -------Solução T7--------------------
def count_user(data_list:list):
    """
    Função criada para contar o número de usários de uma coluna de um 
    determinado dataset e específicar quais são eles.
    Argumento:
        data_list: lista de dados no qual será retirado os tipos de usuários
        e quantidade de cada um.
    Retorna:
        Duas variáveis de valor inteiro com os respectivos nomes de cada tipo de usuário
        contido em uma coluna do dataset.
    """
    subscriber = 0
    customer = 0
    for line in data_list:
        if line[-3] == "Subscriber":
            subscriber += 1
        elif line[-3] == "Customer":
            customer += 1
        
    return [subscriber, customer]

user_list = column_to_list(data_list,5)
types_user = ["Subscriber","Customer"]
quantity_user = count_user(data_list)
y_position = list(range(len(types_user)))
plt.bar(y_position, quantity_user)
plt.ylabel('Quantidade')
plt.xlabel('Usuário')
plt.xticks(y_position, types_user)
plt.title('Quantidade por Usuário')
plt.show(block=True)
#---------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "A verificação booleana da equação não é verdadeira pois considera apenas a soma de duas variveis na coluna de gênero, quanto na verdade são classificadas em três variavéis, Male, Female e 'espaço em branco', logo a soma do aparecimento dessas três variaveis resultaria em true na verificação booleana."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

# -------Solução T9-----------------------------------
# Convertendo a lista de string para lista de inteiros.
integer_trip_duration_list = []
for line in trip_duration_list:
    integer_trip_duration_list.append(int(line))
sorted_trip_duration_list = sorted(integer_trip_duration_list)
min_trip = sorted_trip_duration_list[0]
max_trip = sorted_trip_duration_list[-1]

# Calculando a média das viagens.
sum_of_term = 0
number_of_term = len(sorted_trip_duration_list)
for line in sorted_trip_duration_list:
    sum_of_term += line
mean_trip = sum_of_term/number_of_term

# Calculando a mediana das viagens.
# Para mediana com números de termos pares, precisamos
# pegar os dois valores centrais (n,N) e obter a média
# entre eles, ((n/N)/2).
# Ex: (23,25,27,28,29,30)
# Mediana = ((27+28)/2)
if (len(sorted_trip_duration_list)%2) == 0:
    center_position = (len(sorted_trip_duration_list))/2
    first_center_term = sorted_trip_duration_list[center_position]
    second_center_term = sorted_trip_duration_list[center_position+1]
    median_trip = (first_center_term+second_center_term)/2
# Para mediana com números de termos ímpares, precisamos
# achar o termo central, porem ao dividir um número ímpar
# por um número par , teremos um número com parte
# decimal, por isso a importância de somar mais 0,5 ao
# resultado para encontrarmos o termo central.
# Ex: (1,2,3,4,5,6,7,8,9)
# 9/2 = 4,5 , porem o termo central é 5, logo somando
# 0,5 acharemos 5.
else:
    center_term = (len(sorted_trip_duration_list))/2
    adjust = 1/2
    center_term_plus_adjust = int(center_term + adjust)
    median_trip = sorted_trip_duration_list[center_term_plus_adjust] 
#-----------------------------------------------------------

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()

#-------Solução T10-------------------------------
start_station_list = column_to_list(data_list, 3)
user_types = set(start_station_list)
#--------------------------------------------------

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:

"""
Função de exemplo com anotações.
Argumentos:
    param1: O primeiro parâmetro.
    param2: O segundo parâmetro.
Retorna:
    Uma lista de valores x.
"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

#--------------Solução T12---------------------------------
def count_items(column_list:list):
    """
    Função que obtem informações de um lista inputada dizendo quais os elementos possiu
    e quantidade de cada um deles.
    Argumento:
        column_list: lista onde contem os elementos que serão
        usados no calculo da função.
    Retorna:
        Duas listas, onde uma considera os tipos de variáveis
        e outra considera a quantidade de variáveis por tipo existente na
        lista inicial inputada.
    """
    item_types = list(set(column_list))
    count_items = [0 for row in range(len(item_types))]
    for line in column_list:
        index = 0
        while line != item_types[index]:
            index +=1
        count_items[index] +=1
    return item_types, count_items
#-----------------------------------------------------------

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------