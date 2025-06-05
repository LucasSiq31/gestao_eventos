# Gerenciador de Eventos
# Módulo: Eventos
# Data: 26/05/2025
# Autor: Igor Bitencourt Laura Rodrigues, Lucas Alves, Wagner Silva

#Importação de biblioteca
import os

#Dicionário eventos = {"id": id, "nome": nome, "data": data, "local": local, "palestrante": palestrante, "organizador": organizador}
eventos = {}

#Função que adiciona uma entidade no dicionário
def adicionar():
    os.system('cls')#Limpa a tela

    print('\033[1;36m \n-- Preencha as Informações para Cadastrar um Evento: \033[m ')
   
    id = int(input('ID do evento: ')) #Pega o id para cadastrar
    
    #Verifica se ja existe um id cadastrado
    if id in eventos:
        print(f'\033[1;31m O ID: {id} já está sendo usado - Tente outro \033[m ')
    else:
        #Entrada dos dados da entidade
        nome = input('Nome do Evento: ')
        data = input('Data do evento: ')
        local = input('Local: ')
        palestrante = input('Nome do Palestrante: ')
        organizador = input('Organizador do Evento: ')
       
        #Adicionar informações ao dicionário
        eventos[id] = {
            "id": id,
            "nome": nome,
            "data": data,
            "local": local,
            "palestrante": palestrante,
            "organizador": organizador
        }

        #Saída dos dados cadastrados
        print('\n-------------------------------\n')

        print('\033[1;32mEvento Adicionado \033[m ')
        print(f'\033[;1m{nome.upper()}\033[m')
        print(f'ID do evento: {id}')
        print(f'Data do Evento: {data}')
        print(f'Palestrante: {palestrante}')
        print(f'Local: {local}')
        print(f"Organizado por {organizador}")

    input('\033[1;35m \nPressione ENTER para continuar \033[m')
               
#Função que atualiza os dados de uma entidade
def atualizar():
    os.system('cls') #Limpa a tela

    print('\033[1;36m \n -- Atualizar as informações do Evento: \033[m ')
    
    #Pega o id da entidade que será atualizada
    id = int(input(f'Digite o ID do cadastro que você deseja alterar: '))
   
    #Verifica se o ID existe
    if id in eventos:
       
        #Resgatar valores desse cadastro
        id = eventos[id].get("id")
        nome = eventos[id].get("nome")
        data = eventos[id].get("data")
        local = eventos[id].get("local")
        palestrante = eventos[id].get("palestrante")
        organizador = eventos[id].get("organizador")
       
        #Exibe os dados antes de atualizar
        print(f'\033[1;36m \nDados do ID: {id}: \033[m ')
        print(f'\nNome do Evento: {nome}')
        print(f'Data: {data}')
        print(f'Local: {local}')
        print(f'Palestrante: {palestrante}')
        print(f'Organizado por {organizador}')
       
        #Perguntas do que deseja alterar
        resposta = input(f'\nDeseja alterar o nome do evento? sim ou não: ')
        if resposta == "sim" or resposta == "Sim":
            nome = input('Nome: ')
           
        resposta = input('\nDeseja alterar a data? sim ou não: ')
        if resposta == "sim" or resposta == "Sim":
            data = input('Data: ')
       
        resposta = input('\nDeseja alterar o local? sim ou não: ')
        if resposta == "sim" or resposta == "Sim":
            local = input('Local: ')
           
        resposta = input('\nDeseja alterar o nome do(a) palestrante? sim ou não: ')
        if resposta == "sim" or resposta == "Sim":
            palestrante = input('Palestrante: ')

        resposta = input('\nDeseja alterar o organizador? sim ou não: ')
        if resposta == "sim" or resposta == "Sim":
            organizador = input('Organizador: ')
        
        #Atualiza os dados
        eventos[id] = {
            "id": id,
            "nome": nome,
            "data": data,
            "local": local,
            "palestrante": palestrante,
            "organizador": organizador
        }

        #Confirmação de atualização
        print(f' \033[1;32m  \n -- Dados do evento alterados com sucesso ✔: \033[m  ')
        print(f' ID: {id} \n Evento: {nome} \n Data: {data} \n Local: {local} \n Palestrante: {palestrante} \n Organizador: {organizador}')
    else:
        print(f'\033[1;31m -- Não existe nenhum evento com o ID: {id} - Tente novamente: \033[m ')

    input('\033[1;35m \nPressione ENTER para continuar \033[m')
 

def exibirTodos(): #Função que exibe todas as entidades cadastradas no dicionário
    os.system('cls') #Limpa a tela

    print('\033[1;36m \n -- Todos os Eventos \033[m ')
   
    print('\n   ID   |   NOME   |   DATA   |   PALESTRANTE   |   LOCAL   |   ORGANIZADOR')
    for id in eventos: #Loop que roda por todo o dicionário
        print("-"*75)
        #Saída dos dados
        print(eventos[id].get("id"), "-", eventos[id].get("nome"), "-", eventos[id].get("data"), "-", eventos[id].get("palestrante"), '-', eventos[id].get("local"), '-', eventos[id].get("organizador"))

    input('\033[1;35m \nPressione ENTER para continuar \033[m')
   

def buscaEspecifica(): #Função que exibe uma entidade específica do dicionário
    os.system('cls') #Limpa a tela

    print('\033[1;36m \n -- Buscar por evento específico: \033[m ')
   
    #Pega o id da entidade que será buscada
    id = int(input('\n Digite o ID do Evento: '))
       
    #Verifica se o ID existe
    if id in eventos:
            #Saída dos dados
            print('\n   ID   |   NOME   |   DATA   |   PALESTRANTE   |   LOCAL   |   ORGANIZADOR')
            print("-"*75)
            print(eventos[id].get("id"), "-", eventos[id].get("nome"), "-", eventos[id].get("data"), "-", eventos[id].get("palestrante"), '-', eventos[id].get("local"), '-', eventos[id].get("organizador"))
 
    else:
        print(f'\033[31m Não foi encontrado nenhum evento com o ID: {id} \033[m')   

    input('\033[1;35m \nPressione ENTER para continuar \033[m')   
       
       
def presenca(): #Função que confirma presença em um evento (não é registrado, apenas simbólico)
    os.system('cls') #Limpa a tela

    print('\033[1;36m -- Veja os eventos disponíveis: \033[m ')
   
    #Imprime todos os eventos
    for todosEventos in eventos:
        print(f"ID: {eventos[todosEventos].get('id')} | Nome: {eventos[todosEventos].get('nome')} | Data: {eventos[todosEventos].get('data')} | Local: {eventos[todosEventos].get('local')} | Palestrante: {eventos[todosEventos].get('palestrante')} | Organizador: {eventos[todosEventos].get('organizador')}")
 
    print('\033[1;36m \nPreencha as informações para participar de um evento: \033[m ')
    
    #Entrada para o id do evento que o usuário quer reservar
    idEvento = int(input('ID do Evento: '))
    
    #Verifica se o Id digitado existe
    if idEvento in eventos:
        #Pega dados do usuário
        nomePessoa = input('Seu nome completo: ')
        idade = int(input('Idade: '))
        cpf = input('CPF: ')

        #Imprime os dados do evento e do usuário confirmando a reserva
        print(f' \033[1;32m  \n -- Presença confirmada ✔: \033[m  ')
        
        print(f'\n\033[;1m{eventos[idEvento].get("nome").upper()}\033[m')
        print(f'Palestrante: {eventos[idEvento].get("palestrante")}')
        print(f'Data do Evento: {eventos[idEvento].get("data")}')
        print(f'Local: {eventos[idEvento].get("local")}')
       
        print(f'\n\033[1;96mPara entrar na palestra apresente seus dados: \033[m')
        print(f'Nome Completo: {nomePessoa}')
        print(f'CPF: {cpf}')
        print(f'Idade: {idade} anos')

        print(f'\nOrganizado por {eventos[idEvento].get("organizador")}')
        print(f'ID do evento: {eventos[idEvento].get("id")}')
   
    else:
        print(f'\n\n \033[31m Esse ID não está em nenhum evento - Tente de novo \033[m ')

    input('\033[1;35m \nPressione ENTER para continuar \033[m')
   
#Função que apaga uma entidade do dicionário
def deletar():
    os.system('cls') #Limpa a tela

    print('\033[1;36m \n-- Deletar Eventos: \033[m ')
 
    id = int(input("\nDigite o ID que deseja deletar: ")) #Pega o id da entidade que será deletada
    
    #Confirma se o usuário quer realmente apagar o cadastro
    confirmacao = int(input(f'\nDeseja mesmo deletar o ID: {id} ? \n\033[1;92m 1- Sim \n\033[1;91m 2- Não \033[0;0m\n\nDigite sua escolha: '))
    
    #Verifica a escolha do usuário
    if(confirmacao== 1):
        #Consultar para excluir
        if id in eventos:
            del eventos[id] #Apaga o cadastro
            print(f'\033[1;32m\nInformações do evento com ID: {id} deletados com sucesso ✔ \n \033[m')
        else:
            print(f'\n\n\033[31mO ID: {id} não existe - Tente novamente \033[m ')
    else:
        print(f'Os dados do ID {id} não foram deletados')

    input('\033[1;35m \nPressione ENTER para continuar \033[m')