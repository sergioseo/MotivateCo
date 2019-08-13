#!/usr/bin/env python
# coding: utf-8

# # Trabalhando o dataSet para primeiras análises 

# In[50]:


# coding: utf-8
import csv
import matplotlib.pyplot as plt


# In[51]:


# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")


# In[52]:


# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))


# In[53]:


# Imprimindo a primeira linha de data_list para verificar se funcionou.
# É o cabeçalho dos dados, para que possamos identificar as colunas.
print("Linha 0: ")
print(data_list[0])


# In[54]:


# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])


# ## Vamos imprimir as primeiras 20 linhas usando um loop para identificar os dados.

# In[55]:


# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]


# In[56]:


# Primeiras 20 listas da data_list
print(data_list[0:20])


# ### Vamos Imprimir os gêneros das primeiras 20 linhas usando loop

# In[57]:


# Primeiros 20 Gêneros separados em lista
for i, line in enumerate(data_list[:20],start=1):
    print(f"Line : {i}\tGender: {line[-2]}")


# In[58]:


# Vamos criar uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
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
    for i in data_list:
        column_list.append(i[index])
    return column_list


# In[80]:


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nImprimindo a lista de gêneros das primeiras 20 amostras:")
print(column_to_list(data_list, -2)[:20])


# In[60]:


# Vamos contar cada gênero.
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
print("\nImprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)


# In[79]:


# Vamos criar uma função para contar os gêneros e retornar uma list.
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


print("\nImprimindo a lista de count_gender:")
print(count_gender(data_list))


# ## Descobrindo qual o Gênero mais popular

# In[62]:


# Vamos Criar uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
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

    male = 0
    female = 0
# Fazendo o Loop na data_list, iremos conseguir os valores de "male" e "female".
    for gender in data_list:
        if gender[-2] == "Male":
            male = male + 1

        elif gender[-2] == "Female":
            female = female + 1

    return [male, female]


# In[78]:


# Agora vamos definir qual o gênero mais popular
def most_popular_gender(data_list):
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
    answer = ""

    if male > female:
        return("Male")

    elif female > male:
        return("Female")

    elif male == female:
        return("Equal")

    return answer

print("\nQual é o gênero mais popular na lista?")
print("R:", most_popular_gender(data_list))


# * Assim descobrimos que o gênero que mais fez uso da bike, de acordo com o dataFrame, foi o gênero Masculino

# In[64]:


# Através deste gráfico podemos ver a diferença do numero de gêneros
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


# ## Trabalhando com o User_types

# In[65]:


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


# In[66]:


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


# In[67]:


# Plotando gráfico para ver os resultados
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


# * Assim podemos perceber que temos um numero muito maior de "Subscriber" do que de "Customer".

# ## Trabalhando com Trip_duration

# In[68]:


# Vamos trabalhar com trip_duration (duração da viagem) agora.
# Primeiro iremos achar a duração de viagem Mínima, Máxima, Média, e Mediana usando uma função.
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


# In[69]:


# Vamos encontrar a quantidade de itens da Lista
x = len(trip_duration_list)


# In[70]:


# Vamos ordenar a lista do menor para o maior, já que não podemos usar o max() e o min()
ordered_list = sorted(trip_duration_list, key = int)


# In[71]:


# Agora teremos o menor e o maior valor da lista
min_trip = int(ordered_list[0])
max_trip = int(ordered_list[-1])


# In[72]:


# Agora faremos a contagem para achar a media
lista_num = map(int, ordered_list)
soma = sum(lista_num)
mean_trip = soma / x
mean_trip = round(mean_trip)


# In[73]:


# Vamos achar a mediana da lista
if x % 2 == 0:
    median_trip = (ordered_list[int((x/2)-1)] + ordered_list[int((x/2))])/2
else:
    median_trip = int(ordered_list[int(((x-1)/2))])


# In[74]:


# Printando os resultados
print("\nImprimindo o mínimo, máximo, média, e mediana")
print("Minimo: ", min_trip, "\nMaximo: ", max_trip, "\nMédia: ", mean_trip, "\nMediana: ", median_trip)


# ## Trabalhando com Start_stations

# In[75]:


# Vamos rerificar quantos tipos de start_stations nós temos
start_station = column_to_list(data_list, 3)
user_types = set(start_station)

print("\nImprimindo as start stations:")
print(len(user_types))


# In[ ]:




