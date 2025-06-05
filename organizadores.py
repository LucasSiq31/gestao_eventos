# Gerenciador de Eventos
# Módulo: Organizadores
# Data: 05/06/2025
# Autor: Igor Bitencourt Laura Rodrigues, Lucas Alves, Wagner Silva

#Importação de biblioteca
import os

#Dicionário organizadores = {"id": id, "nome": nome, "cnpj": cnpj}
organizadores = {}

def cadastrar(): #Função que adiciona uma entidade no dicionário
    os.system('cls') #Limpa a tela

    print('\033[1;36m \n-- Preencha os dados para cadastrar um organizador: \033[m ')

    id = int(input('ID do organizador: ')) #Pega o id para cadastrar
    
    #Verifica se ja existe um id cadastrado
    if id in organizadores:
        print(f'\033[1;31m O ID: {id} já está sendo usado - Tente outro \033[m ')
    else:
        #Entrada dos dados da entidade
        nome = input("Empresa organizadora: ")
        cnpj = input("CNPJ da empresa organizadora: ")

        #Adicionar informações ao dicionário
        organizadores[id] = {
            "id": id,
            "nome": nome,
            "cnpj": cnpj,
        }

        #Saída dos dados cadastrados
        print('\n -------------------------------------------- \n')
        print('\033[1;32mEmpresa organizadora cadastrado \033[m ')
        print(f'ID: {id}')
        print(f'Empresa: {nome}')
        print(f'CNPJ: {cnpj}')

    input('\033[1;35m \nPressione ENTER para continuar \033[m')


def atualizar(): #Função que atualiza os dados de uma entidade
    os.system('cls') #Limpa a tela

    print('\033[1;36m \n -- Atualizar os dados do organizador: \033[m ')
    
    #Verifica se o ID existe
    id = int(input(f'Digite o ID do organizador que você deseja alterar: '))
   
    #Verifica se o ID existe
    if id in organizadores:
       
        #Resgatar valores desse cadastro
        id = organizadores[id].get("id")
        nome = organizadores[id].get("nome")
        cnpj = organizadores[id].get("cnpj")

       
        print(f'\033[1;36m \nDados do ID: {id}: \033[m ')
       
        #Exibe os dados antes de atualizar
        print(f'\nNome da empresa organizadora: {nome}')
        print(f'CNPJ: {cnpj}')
       
        #Perguntas do que deseja alterar
        resposta = input(f'\nDeseja alterar o nome da empresa organizadora? sim ou não: ')
        if resposta == "sim" or resposta == "Sim":
            nome = input('Nome: ')
           
        resposta = input('\nDeseja alterar o CNPJ da empresa organizadora? sim ou não: ')
        if resposta == "sim" or resposta == "Sim":
            cnpj = input('CNPJ: ')
        
        #Atualiza os dados
        organizadores[id] = {
            "id": id,
            "nome": nome,
            "cnpj": cnpj
        }

        #Confirmação de atualização
        print(f' \033[1;32m  \n -- Dados do organizador alterados com sucesso ✔: \033[m  ')
        print(f' ID: {id} \n Nome: {nome} \n CNPJ: {cnpj}')
    else:
        print(f'\033[1;31m -- Não existe nenhum organizador com o ID: {id} - Tente novamente: \033[m ')

    input('\033[1;35m \nPressione ENTER para continuar \033[m')


def exibirTodos(): #Função que exibe todas as entidades cadastradas no dicionário
    os.system('cls') #Limpa a tela

    print('\033[1;36m \n -- Todos os palestrantes \033[m ')
   
    print('\n   ID   |   NOME   |   CNPJ')
    for id in organizadores: #Loop que roda por todo o dicionário
        print("-"*75)
        #Saída dos dados
        print(organizadores[id].get("id"), "-", organizadores[id].get("nome"), "-", organizadores[id].get("cnpj"))

    input('\033[1;35m \nPressione ENTER para continuar \033[m')


def buscaEspecifica(): #Função que exibe uma entidade específica do dicionário
    os.system('cls') #Limpa a tela
    
    print('\033[1;36m \n -- Buscar por organizador específico: \033[m ')
   
    #Pega o id da entidade que será buscada
    id = int(input('\n Digite o ID do organizador: '))
       
    #Verifica se o ID existe
    if id in organizadores:
            print('\n   ID   |   NOME   |   CNPJ')
            print("-"*75)
            #Saída dos dados
            print(organizadores[id].get("id"), "-", organizadores[id].get("nome"), "-", organizadores[id].get("cnpj"))
    else:
        print(f'\033[31m Não foi encontrado nenhum organizador com o ID: {id} \033[m')   

    input('\033[1;35m \nPressione ENTER para continuar \033[m')


def descadastrar(): #Função que apaga uma entidade do dicionário
    os.system('cls') #Limpa a tela
    print('\033[1;36m \n-- Descadastrar organizador: \033[m ')
    
    #Pega o id da entidade que será deletada
    id =  int(input("\nDigite o ID que deseja descadastrar: "))
    
    #Confirma se o usuário quer realmente apagar o cadastro
    confirmacao = int(input(f'\nDeseja mesmo descadastrar o ID: {id} ? \n\033[1;92m 1- Sim \n\033[1;91m 2- Não \033[0;0m\n\nDigite sua escolha: '))
    
    #Verifica a escolha do usuário
    if(confirmacao== 1):
        #Consultar para excluir
        if id in organizadores:
            del organizadores[id]#Apaga o cadastro
            print(f'\033[1;32m\nInformações do organizador com ID: {id} descadastrados com sucesso ✔ \n \033[m')
        else:
            print(f'\n\n\033[31mO ID: {id} não existe - Tente novamente \033[m ')
    else:
        print(f'Os dados do ID {id} não foram descadastrados')

    input('\033[1;35m \nPressione ENTER para continuar \033[m')