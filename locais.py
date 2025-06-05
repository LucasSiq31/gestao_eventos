# Gerenciador de Eventos
# Módulo: Locais
# Data: 04/06/2025
# Autor: Igor Bitencourt Laura Rodrigues, Lucas Alves, Wagner Silva

#Importação de biblioteca
import os

#Dicionário locais = {"id": id, "nome": nome, "endereco": enderco}
locais = {}

def adicionar(): #Função que adiciona uma entidade no dicionário
    os.system('cls') #Limpa a tela
    
    print('\033[1;36m \n-- Preencha os dados para adicionar um lugar: \033[m ')

    id = int(input('ID do Lugar: ')) #Pega o id para cadastrar
    
    #Verifica se ja existe um id cadastrado
    if id in locais:
        print(f'\033[1;31m O ID: {id} já está sendo usado - Tente outro \033[m ')
    else:
        #Entrada dos dados da entidade
        nome = input("Lugar: ")
        endereco = input("Endereço: ")

        #Adicionar informações ao dicionário
        locais[id] = {
            "id": id,
            "nome": nome,
            "endereco": endereco
        }

        #Saída dos dados cadastrados
        print('\n -------------------------------------------- \n')
        print('\033[1;32mLocal Cadastrado \033[m ')
        print(f'ID: {id} | {nome.upper()} - {endereco}')

    input('\033[1;35m \nPressione ENTER para continuar \033[m')


def atualizar(): #Função que atualiza os dados de uma entidade
    os.system('cls') #Limpa a tela

    print('\033[1;36m \n -- Atualizar os dados do local: \033[m ')
   
    #Pega o id da entidade que será atualizada
    id = int(input(f'Digite o ID do local que você deseja alterar: '))
   
    #Verifica se o ID existe
    if id in locais:
       
        #Resgatar valores desse cadastro
        id = locais[id].get("id")
        nome = locais[id].get("nome")
        endereco = locais[id].get("endereco")
       
        print(f'\033[1;36m \nDados do ID: {id}: \033[m ')
       
        #Exibe os dados antes de atualizar
        print(f'ID: {id} | {nome.upper()} - {endereco}')
       
        #Perguntas do que deseja alterar
        resposta = input(f'\nDeseja alterar o nome do local? sim ou não: ')
        if resposta == "sim" or resposta == "Sim":
            nome = input('Nome: ')
           
        resposta = input('\nDeseja alterar o endereço? sim ou não: ')
        if resposta == "sim" or resposta == "Sim":
            endereco = input('Endereço: ')
        
        #Atualiza os dados
        locais[id] = {
            "id": id,
            "nome": nome,
            "endereco": endereco
        }

        #Confirmação de atualização
        print(f' \033[1;32m  \n -- Dados do local alterados com sucesso ✔: \033[m  ')
        print(f'ID: {id} | {nome.upper()} - {endereco}')
    else:
        print(f'\033[1;31m -- Não existe nenhum local com o ID: {id} - Tente novamente: \033[m ')

    input('\033[1;35m \nPressione ENTER para continuar \033[m')


def exibirTodos(): #Função que exibe todas as entidades cadastradas no dicionário
    os.system('cls') #Limpa a tela

    print('\033[1;36m \n -- Todos os locais \033[m ')
    
    #Loop que roda por todo o dicionário
    for id in locais:
        print("-"*75)
        #Saída dos dados
        print(f'ID: {locais[id].get("id")} | {locais[id].get("nome").upper()} - {locais[id].get("endereco")}')
        
    input('\033[1;35m \nPressione ENTER para continuar \033[m')


def buscaEspecifica(): #Função que exibe uma entidade específica do dicionário
    os.system('cls') #Limpa a tela

    print('\033[1;36m \n -- Buscar por local específico: \033[m ')
   
    #Pega o id da entidade que será buscada
    id = int(input('\n Digite o ID do local: '))
       
    #Verifica se o ID existe
    if id in locais:
            print("-"*75)
            #Saída dos dados
            print(f'ID: {locais[id].get("id")} | {locais[id].get("nome").upper()} - {locais[id].get("endereco")}')
    else:
        print(f'\033[31m Não foi encontrado nenhum local com o ID: {id} \033[m')   

    input('\033[1;35m \nPressione ENTER para continuar \033[m')


def apagar(): #Função que apaga uma entidade do dicionário
    os.system('cls') #Limpa a tela

    print('\033[1;36m \n-- Apagar local: \033[m ')
    
    #Pega o id da entidade que será deletada
    id =  int(input("\nDigite o ID que deseja apagar: "))
    
    #Confirma se o usuário quer realmente apagar o cadastro
    confirmacao = int(input(f'\nDeseja mesmo apagar o ID: {id} ? \n\033[1;92m 1- Sim \n\033[1;91m 2- Não \033[0;0m\n\nDigite sua escolha: '))
    
    #Verifica a escolha do usuário
    if(confirmacao== 1):
        #Consultar para excluir
        if id in locais:
            del locais[id] #Apaga o cadastro
            print(f'\033[1;32m\nInformações do local com ID: {id} apagados com sucesso ✔ \n \033[m')
        else:
            print(f'\n\n\033[31mO ID: {id} não existe - Tente novamente \033[m ')
    else:
        print(f'Os dados do ID {id} não foram apagados')

    input('\033[1;35m \nPressione ENTER para continuar \033[m')