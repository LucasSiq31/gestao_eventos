# Gerenciador de Eventos
# Módulo: Palestrantes
# Data: 30/05/2025
# Autor: Igor Bitencourt Laura Rodrigues, Lucas Alves, Wagner Silva

#Importação de biblioteca
import os

#Dicionário palestrantes = {"id": id, "nome": nome, "profissao": profissao, "telefone": telefone}
palestrantes = {}

def cadastrar(): #Função que adiciona uma entidade no dicionário
    os.system('cls') #Limpa a tela

    print('\033[1;36m \n-- Preencha os dados para cadastrar um palestrante: \033[m ')
    
    id = int(input('ID do palestrante: ')) #Pega o id para cadastrar
    
    #Verifica se ja existe um id cadastrado
    if id in palestrantes:
        print(f'\033[1;31m O ID: {id} já está sendo usado - Tente outro \033[m ')
    else:
        #Entrada dos dados da entidade
        nome = input("Nome do Palestrante: ")
        profissao = input("Profissão do Palestrante: ")
        telefone = input("Telefone do Palestrante: ")

        #Adicionar informações ao dicionário
        palestrantes[id] = {
            "id": id,
            "nome": nome,
            "profissao": profissao,
            "telefone": telefone
        }

        #Saída dos dados cadastrados
        print('\n -------------------------------------------- \n')
        print('\033[1;32mPalestrante cadastrado \033[m ')
        print(f'ID: {id}')
        print(f'Nome: {nome}')
        print(f'Profissao: {profissao}')
        print(f'Contato: {telefone}')

    input('\033[1;35m \nPressione ENTER para continuar \033[m')


def atualizar(): #Função que atualiza os dados de uma entidade
    os.system('cls') #Limpa a tela

    print('\033[1;36m \n -- Atualizar os dados do palestrante: \033[m ')
    
    #Pega o id da entidade que será atualizada
    id = int(input(f'Digite o ID do palestrante que você deseja alterar: '))
   
    #Verifica se o ID existe
    if id in palestrantes:
       
        #Resgatar valores desse cadastro
        id = palestrantes[id].get("id")
        nome = palestrantes[id].get("nome")
        profissao = palestrantes[id].get("profissao")
        telefone = palestrantes[id].get("telefone")
       
        print(f'\033[1;36m \nDados do ID: {id}: \033[m ')
       
        #Exibe os dados antes de atualizar
        print(f'\nNome do Palestrante: {nome}')
        print(f'Profissão: {profissao}')
        print(f'Contato: {telefone}')
       
        #Perguntas do que deseja alterar
        resposta = input(f'\nDeseja alterar o nome do palestrante? sim ou não: ')
        if resposta == "sim" or resposta == "Sim":
            nome = input('Nome: ')
           
        resposta = input('\nDeseja alterar a profissão? sim ou não: ')
        if resposta == "sim" or resposta == "Sim":
            profissao = input('Profissão: ')
       
        resposta = input('\nDeseja alterar o telefone? sim ou não: ')
        if resposta == "sim" or resposta == "Sim":
            telefone = input('Telefone: ')
        
        #Atualiza os dados
        palestrantes[id] = {
            "id": id,
            "nome": nome,
            "profissao": profissao,
            "telefone": telefone
        }

        #Confirmação de atualização
        print(f' \033[1;32m  \n -- Dados do palestrante alterados com sucesso ✔: \033[m  ')
        print(f' ID: {id} \n Nome: {nome} \n Profissão: {profissao} \n Contato: {telefone}')
    else:
        print(f'\033[1;31m -- Não existe nenhum palestrante com o ID: {id} - Tente novamente: \033[m ')

    input('\033[1;35m \nPressione ENTER para continuar \033[m')


def exibirTodos(): #Função que exibe todas as entidades cadastradas no dicionário
    os.system('cls') #Limpa a tela

    print('\033[1;36m \n -- Todos os palestrantes \033[m ')
   
    print('\n   ID   |   NOME   |   PROFISSÃO   |   CONTATO')
    for id in palestrantes: #Loop que roda por todo o dicionário
        print("-"*75)
        #Saída dos dados
        print(palestrantes[id].get("id"), "-", palestrantes[id].get("nome"), "-", palestrantes[id].get("profissao"), "-", palestrantes[id].get("telefone"))

    input('\033[1;35m \nPressione ENTER para continuar \033[m')


def buscaEspecifica(): #Função que exibe uma entidade específica do dicionário
    os.system('cls') #Limpa a tela

    print('\033[1;36m \n -- Buscar por palestrante específico: \033[m ')
   
    #Pega o id da entidade que será buscada
    id = int(input('\n Digite o ID do palestrante: '))
       
    #Verifica se o ID existe
    if id in palestrantes:
            #Saída dos dados
            print('\n   ID   |   NOME   |   PROFISSÃO   |   CONTATO')
            print("-"*75)
            print(palestrantes[id].get("id"), "-", palestrantes[id].get("nome"), "-", palestrantes[id].get("profissao"), "-", palestrantes[id].get("telefone"))

    else:
        print(f'\033[31m Não foi encontrado nenhum palestrante com o ID: {id} \033[m')   

    input('\033[1;35m \nPressione ENTER para continuar \033[m')


def descadastrar(): #Função que apaga uma entidade do dicionário
    os.system('cls')

    print('\033[1;36m \n-- Descadastrar palestrantes: \033[m ')
    
    #Pega o id da entidade que será deletada
    id =  int(input("\nDigite o ID que deseja descadastrar: "))
    
    #Confirma se o usuário quer realmente apagar o cadastro
    confirmacao = int(input(f'\nDeseja mesmo descadastrar o ID: {id} ? \n\033[1;92m 1- Sim \n\033[1;91m 2- Não \033[0;0m\n\nDigite sua escolha: '))
    
    #Verifica a escolha do usuário
    if(confirmacao== 1):
        #Consultar para excluir
        if id in palestrantes:
            del palestrantes[id] #Apaga o cadastro
            print(f'\033[1;32m\nInformações do Palestrante com ID: {id} descadastrados com sucesso ✔ \n \033[m')
        else:
            print(f'\n\n\033[31mO ID: {id} não existe - Tente novamente \033[m ')
    else:
        print(f'Os dados do ID {id} não foram descadastrados')

    input('\033[1;35m \nPressione ENTER para continuar \033[m')