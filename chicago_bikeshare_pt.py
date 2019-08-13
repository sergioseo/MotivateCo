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

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]
"""
    Criando codigo para criar uma lista com os 20 primeiros itens da lista
    INPUT:
        Buscar em data_list os primeiros 20 itens da lista.
    OUTPUT:
        Gera Uma lista nova lista de valores com os 20 primeiros da lista.
"""
# Primeiras 20 listas da data_list
print(data_list[0:20])

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
"""
    Criando codigo para imprimir uma lista com os 20 primeiros generos da lista
    INPUT:
        Buscar em data_list os primeiros 20 generos da lista.
    OUTPUT:
        Imprimi uma lista nova com os 20 primeiros generos da data_list.
"""
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

# Primeiros 20 Gêneros separados em lista
for i, line in enumerate(data_list[:20],start=1):
    print(f"Line : {i}\tGender: {line[-2]}")

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """
    Definir uma função com objetivo de criar lista de generos dentro dos 20 primeiros itens da lista.
    INPUT:
        param1: data representa a lista de onde serão colhidos itens para a amostra.
        param2: index representa a posição na lista da qual serão colhidos valores.
    OUTPUT:
        Imprimi uma lista de valores da nova lista.
        """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for i in data_list:
        column_list.append(i[index])
    return column_list


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
"""
    Loop usando for para contar quantos itens possuem em cada lista.
    INPUT:
        param1: if para achar o numero exato do item Male.
        param2: elif para achar o numero exato do item Female.
    OUTPUT:
        Imprimi duas listas de valores com a contagem de Male e Female.
"""
male = 0
female = 0
others = 0

for genero in data_list:
    if genero[-2] == "Male":
        male = male + 1

    elif genero[-2] == "Female":
        female = female + 1

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
"""
    Loop usando for para contar quantos itens possuem em cada lista.
    INPUT:
        param1: if para achar o numero exato do item Male.
        param2: elif para achar o numero exato do item Female.
    OUTPUT:
        Return: Junta os valores com a contagem de Male e Female em uma só lista.
"""
def count_gender(data_list):
    male = 0
    female = 0
    # Fazendo o Loop na data_list, iremos conseguir os valores de "male" e "female".
    for gender in data_list:
        if gender[-2] == "Male":
            male = male + 1

        elif gender[-2] == "Female":
            female = female + 1

    return [male, female]


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
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
"""
    Definindo a primeira função para fazer a contagem individual dos generos.
    Depois, usamos loop para descobrir qual os valores das listas Male e Female
    INPUT:
        param1: data_list para buscar valores dos generos.
        if para descobrir valores da lista Male.
        elif para descobrir valores da lista Female.
    OUTPUT:
        Return: Junta os valores com a contagem de Male e Female em uma só lista.
"""
def most_popular_gender(data_list):
    male = 0
    female = 0
# Fazendo o Loop na data_list, iremos conseguir os valores de "male" e "female".
    for gender in data_list:
        if gender[-2] == "Male":
            male = male + 1

        elif gender[-2] == "Female":
            female = female + 1

    return [male, female]

"""
    Depois definimos a segunda função para descobrir o valor do item mais popular.
    Usamos loop para definir o item mais popular.
    INPUT:
        param1: data_list para buscar valores dos generos.
        if se Male for maior que Female.
        elif se Female for maior que Male.
        elif se Male for igual a Female.
    OUTPUT:
        Return: Retorna uma lista com o genero predominante.
"""
# Função para definir qual o genero mais popular
def most_popular_gender(data_list):
    answer = ""

    if male > female:
        return("Male")

    elif female > male:
        return("Female")

    elif male == female:
        return("Equal")

    return answer

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
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
"""
    Definir uma função para fazer a contagem do tipo de usuario dentro da data_list.
    Usamos loop para fazer a contagem os itens
    INPUT:
        param1: data_list para buscar valores dos user_types.
        if para contagem do item Customer.
        elif para contagem do item Subscriber.
    OUTPUT:
        Return: Retorna uma lista com a contagem dos user_types.
"""
def count_user(data_list):
    customer = 0
    subscriber = 0
# Fazendo o Loop na data_list, iremos conseguir os valores de "Customer" e "Subscriber".
    for user in data_list:
        if user[-3] == "Customer":
            customer = customer + 1

        elif user[-3] == "Subscriber":
            subscriber = subscriber + 1

    return [customer, subscriber]

"""
    Depois definimos a segunda função para descobrir o valor do item mais popular.
    Usamos loop para definir o item mais popular dentro da data_list.
    INPUT:
        param1: data_list para buscar valores dos user_types.
        if se Customer for maior que Subscriber.
        elif se Subscriber for maior que Customer.
        elif se Customer for igual a Subscriber.
    OUTPUT:
        Return: Retorna uma lista com o user_type predominante.
"""
# Função para definir qual o user mais popular
def most_popular_user(data_list):
    answer = ""

    if customer > subscriber:
        return("Customer")

    elif subscriber > customer:
        return("Subscriber")

    elif customer == subscriber:
        return("Equal")

    return answer

# Se tudo está rodando como esperado, verifique este gráfico!
user_type_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber"]
quantity = count_user(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Usuário')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Essa resposta é falsa porque na somatória teria que se incluir mais um usuário (others)" \
          "\nE sem esse terceiro usuário o resultado não será igual"
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
"""
    Definir uma função para descobrir os valor da coluna trip_duration.
    Definir atraves do sorted o valor minino e o valor maximo da data_list.
    Definir atraves de map, sum e round o valor medio da lista data-list.
    Definir atraves de if e elif o valor mediano da lista data_list.
    INPUT:
        Usar len para definir a quantidade de itens da coluna trip_duration.
        Usar sorted para organizar uma lista com os valores na ordem crescrente.
        Usar map, sum e round para definir a media da lista somando todos os itens e dividindo pelo total de itens da coluna trip_duration.
        Usar if para valores pares e elif para valores impares
    OUTPUT:
        Retorna uma lista de valores para os itens min_trip
        Retorna uma lista de valores para os itens max_trip
        Retorna uma lista de valores para os itens mean_trip
        Retorna uma lista de valores para os itens median_trip
"""
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

# Vamos encontrar a quantidade de itens da Lista
x = len(trip_duration_list)

# Vamos ordenar a lista do menor para o maior, já que não podemos usar o max() e o min()
ordered_list = sorted(trip_duration_list, key = int)

# Agora teremos o menor e o maior valor da lista
min_trip = int(ordered_list[0])
max_trip = int(ordered_list[-1])

# Agora faremos a contagem para achar a media
lista_num = map(int, ordered_list)
soma = sum(lista_num)
mean_trip = soma / x
mean_trip = round(mean_trip)

#Vamos achar o valor mediano da lista

if x % 2 == 0:
    median_trip = (ordered_list[int((x/2)-1)] + ordered_list[int((x/2))])/2
else:
    median_trip = int(ordered_list[int(((x-1)/2))])

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
"""
    Definir um codigo para fazer a contagem de start_stations dentro da data_list.
    Usamos set para separar os user_types dentro da coluna start_stations.
    Usamos len para fazer a contagem dos user_types.
    INPUT:
        param1: data_list para buscar valores de start_station.
        param2: posição dos valores de start_station.
        Set para categorizar e organizar a lista da coluna start_station.
        Usar len para contar os user_types dentro da coluna start_station.
    OUTPUT:
        Retorna uma lista com a contagem dos user_types da coluna start_station.
"""
start_station = column_to_list(data_list, 3)
user_types = set(start_station)

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))

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
answer = "no"

def count_items(column_list):
    item_types = []
    count_items = []
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------
