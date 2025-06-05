# Gerenciador de Eventos
# Módulo: Principal / Main
# Data: 26/05/2025
# Autor: Igor Bitencourt Laura Rodrigues, Lucas Alves, Wagner Silva
 
#Importação de bibliotecas e módulos
import eventos
import palestrantes
import locais
import organizadores
import os
 
#Variáveis
escolha = 0

os.system('cls') #Limpa a tela

#Entrada para Nome
nome = input('Digite seu Nome: ')
 
# Menu inicial
def menu():
    os.system('cls') #Limpa a tela

    print("\033[;1m\033[1;33mGerenciador de Eventos\033[0;0m")
    print(f'Olá, \033[1;35m{nome}\033[m! Seja Bem Vindo(a)\n ')

    print("\033[;1mQual serviço deseja acessar?\033[0;0m")
    print(" 1 - Eventos")
    print(" 2 - Palestrantes")
    print(" 3 - Locais")
    print(" 4 - Organizadores")
    print(" 5 - Ingressar em um evento")
    print("\033[1;31m 6 - Sair\033[m")

#Menu de eventos
def evento():
    opcao = 0
    while(opcao != 6): #Looping para não voltar ao menu inicial até o usuário decidir voltar
        os.system('cls') #Limpa a tela

        #Impressão de um menu
        print("\033[;1m\033[1;33mEventos\033[0;0m")

        print(' 1 - Adicionar Evento: ')
        print(' 2 - Atualizar Informações do Evento: ')
        print(' 3 - Ver todos os Eventos: ')
        print(' 4 - Buscar Evento Específico: ')
        print(' 5 - Deletar Evento: ')
        print('\033[1;31m 6 - Voltar \033[m ')
    
        opcao = int(input('Escolha uma opção: ')) #Entrada da escolha

        input('\033[1;35m \nPressione ENTER para continuar \033[m')

        #Validando a escolha
        if opcao == 1:
            eventos.adicionar()
        elif opcao == 2:
            eventos.atualizar()
        elif opcao == 3:
            eventos.exibirTodos()
        elif opcao == 4:
            eventos.buscaEspecifica()
        elif opcao == 5:
            eventos.deletar()
        else:
            (f'Voltando ao Menu Inicial')

#Menu de palestrantes
def palestrante():
    opcao = 0
    while(opcao != 6): #Looping para não voltar ao menu inicial até o usuário decidir voltar
        os.system('cls') #Limpa a tela

        #Impressão de um menu
        print("\033[;1m\033[1;33mPalestrantes\033[0;0m")

        print(' 1 - Cadastrar Palestrante: ')
        print(' 2 - Atualizar dados do Palestrante: ')
        print(' 3 - Ver todos os Palestrantes: ')
        print(' 4 - Buscar Palestrante Específico: ')
        print(' 5 - Descadastrar Palestrante: ')
        print('\033[1;31m 6 - Voltar \033[m ')

        opcao = int(input('Escolha uma opção: ')) #Entrada da escolha
    
        input('\033[1;35m \nPressione ENTER para continuar \033[m')

        #Validando a escolha
        if opcao == 1:
            palestrantes.cadastrar()
        elif opcao == 2:
            palestrantes.atualizar()
        elif opcao == 3:
            palestrantes.exibirTodos()
        elif opcao == 4:
            palestrantes.buscaEspecifica()
        elif opcao == 5:
            palestrantes.descadastrar()
        else:
            (f'Voltando ao Menu Inicial')

#Menu de locais
def local():
    opcao = 0
    while(opcao != 6): #Looping para não voltar ao menu inicial até o usuário decidir voltar
        os.system('cls') #Limpa a tela

        #Impressão de um menu
        print("\033[;1m\033[1;33mLocais\033[0;0m")

        print(' 1 - Adicionar Local: ')
        print(' 2 - Atualizar informações do Local: ')
        print(' 3 - Ver todos os Locais: ')
        print(' 4 - Buscar Local Específico: ')
        print(' 5 - Apagar Local: ')
        print('\033[1;31m 6 - Voltar \033[m ')

        opcao = int(input('Escolha uma opção: ')) #Entrada da escolha
    
        input('\033[1;35m \nPressione ENTER para continuar \033[m')

        #Validando a escolha
        if opcao == 1:
            locais.adicionar()
        elif opcao == 2:
            locais.atualizar()
        elif opcao == 3:
            locais.exibirTodos()
        elif opcao == 4:
            locais.buscaEspecifica()
        elif opcao == 5:
            locais.apagar()
        else:
            (f'Voltando ao Menu Inicial')

#Menu de organizadores
def organizador():
    opcao = 0
    while(opcao != 6): #Looping para não voltar ao menu inicial até o usuário decidir voltar
        os.system('cls') #Limpa a tela

        #Impressão de um menu
        print("\033[;1m\033[1;33mOrganizadores\033[0;0m")

        print(' 1 - Adicionar Organizador: ')
        print(' 2 - Atualizar dados do Organizador: ')
        print(' 3 - Ver todos os Organizadores: ')
        print(' 4 - Buscar Organizador Específico: ')
        print(' 5 - Apagar Organizador: ')
        print('\033[1;31m 6 - Voltar \033[m ')

        opcao = int(input('Escolha uma opção: ')) #Entrada da escolha
    
        input('\033[1;35m \nPressione ENTER para continuar \033[m')

        #Validando a escolha
        if opcao == 1:
            organizadores.cadastrar()
        elif opcao == 2:
            organizadores.atualizar()
        elif opcao == 3:
            organizadores.exibirTodos()
        elif opcao == 4:
            organizadores.buscaEspecifica()
        elif opcao == 5:
            organizadores.descadastrar()
        else:
            (f'Voltando ao Menu Inicial')

#Função de participar de um evento
def participar():
    eventos.presenca()
 
#Define qual entidade irá alterar a partir da escolha do usuário
def comandos(escolha):
    if escolha == 1:
        evento()
    elif escolha == 2:
        palestrante()
    elif escolha == 3:
        local()
    elif escolha == 4:
        organizador()
    elif escolha == 5:
        participar()
    else:
        (f'Encerrando')

while(escolha != 6): #Looping para não encerrar o programa e se manter no menu inicial
    os.system('cls') #Limpa a tela
   
    menu() #Imprime o menu principal a partir da função menu()
    
    #Envia e valida qual entidade o usuário quer alterar
    escolha = int(input('Escolha uma opção: '))
    comandos(escolha)