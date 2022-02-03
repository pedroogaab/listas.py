#!/usr/bin/python3
import csv
import re
import operator


erros = r"((ERROR): [\w\s-]+)" #Filtro que irá buscar por mensagens de erro no arquivo log
info = r"((INFO): [\w\s]+)" #Filtro que irá buscar por mensagens de info no arquivo log
usuario = r"\(\w+" #Filtro que irá buscar por usuarios no arquivo log   


with open("C:/Users/plech/Downloads/log.txt") as file: #Abrindo o arquivo log.txt

    errors = {} 
    for lilha in file: #Irá ler linha por linha do arquivo txt
        regular = re.search(erros,lilha) 
        if regular != None: #Se ele não encontrar mensagem de erro na mensagem ele irá retorna None, então precisa ser verificado se ele encontrou algum ERROR na mensagem
            regular = regular[0].replace("ERROR:"," ").strip() #removendo o ERROR: da mensagem e tirando os espaços
            if regular not in errors: #Verficando se o erro já existe no dicionário§
                errors[regular] = 0 #Caso não existir, estará criando uma key nova com nome do erro para contabiliza-lá
            errors[regular] += 1 #Contabilizando + 1 no erro
    error_list = [] #Criando uma lista para armazenar o que foi salvo no dicionário (isso servirá para a criação do arquivo .csv)
    nome_coluna_erro = ["ERRORS,   ""NUMBER OF OCCURRENCES"] #Lista com os nomes das colunas no arquivo .csv
    for erro, ocorrencia in errors.items(): 
        error_list.append([erro , ocorrencia ]) 
    error_list.sort(key=operator.itemgetter(1),reverse=True)
    with open("error_log.csv","w") as erro_log:
        arquivo_de_erro = csv.writer(erro_log) 
        arquivo_de_erro.writerow(nome_coluna_erro) #Escrevendo os nomes das colunas como a primeira linha da tabela
        for linha in error_list: # {Escrevendo na tabela tudo o que está armazenado
            arquivo_de_erro.writerow(linha) # em error_list}
            



with open("C:/Users/plech/Downloads/log.txt") as file: #Abrindo o arquivo log.txt

    dicionario = {} #Dicionário que servirá para contabilizar a ocorrência dos erros
    for linha in file:  #Irá ler linha por linha do arquivo txt
        user = re.search(usuario, linha)    #Irá procurar a mensagem utilizando a expressão regular "erros" como filtro
        user = user[0].replace("("," ").strip( )
        if user not in dicionario:
            dicionario[user] = (0,0)
        erro , info = dicionario[user]
        if re.search(erros , linha):
            erro += 1
        else:
            info += 1
        dicionario [user ] = ( erro, info )
    lista = []
    for user, ocorrencia in dicionario.items():
        lista.append([user , ocorrencia [0] , ocorrencia [1]])
    lista.sort()
    with open("tabela.csv","w") as arquivo:
        arquivo_de_busca = csv.writer(arquivo) 
        arquivo_de_busca.writerow(["USERS,    ""NUMBER OF ERROR,     ""NUMBER OF INFO"])
        for linha in lista: # {Escrevendo na tabela tudo o que está armazenado
            arquivo_de_busca.writerow(linha) # em error_list}
            
            