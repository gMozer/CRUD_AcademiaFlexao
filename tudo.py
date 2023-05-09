import os
import csv

def menu():
    print('-'*60)
    print('Bem-vindo ao gerenciamento da Academia Flexão!')
    print('-'*60)
    print('Pressione 1 para o Cadastro de clientes.')
    print('Pressione 2 para o Relatório de clientes.')
    print('Pressione 3 para a Atualização de clientes.')
    print('Pressione 4 para a Exclusão de clientes.')
    print('Pressione 5 para Sair.')
    print('-'*60)

def cadastro():
    print('-'*60)
    nome=input('digite nome ')
    cpf=input('Insira o cpf: ')                                                       #colocar código para checar se esse CPF já existe                                #Cpf PRECISA ter 11 numeros
    while True:  
      cpf=input('Confirme o cpf: ')   
      if cpf.isdigit() and len(cpf) == 11:
          break
      else:
        print('insira apenas 11 números: ')
    telefone=input('telefone ')
    with open("database.csv", "a") as arquivo:          #a = attach      #colocar código de conflito de cpf
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, cpf, telefone])
        print("Cliente cadastrado com sucesso!")
        return
    voltar_menu()

def relatorio():
    cpff = input("Digite o CPF do cliente que deseja visualizar: ")
    with open("database.csv", "r") as arquivo:         #r = read 
        leitor = csv.reader(arquivo)
        linhas = list(leitor)
        if cpff in linhas:
            print('Cliente encontrado: ', linhas)
        for i, linha in enumerate(linhas):
            if cpff in linha:
                encontrado = True
                print(f"Cliente encontrado: {linha}")
    voltar_menu()

def atualizar():                                                  #colocar código de ser possível apenas procurar pelo CPF
    cpf = input("Digite o CPF do cliente que deseja atualizar: ")
    with open("database.csv", "r") as arquivo:
        leitor = csv.reader(arquivo)
        linhas = list(leitor)
        encontrado = False
        for i, linha in enumerate(linhas):
            if cpf in linha:
                encontrado = True
                print(f"Cliente encontrado: {linha}")
                print("Digite as novas informações:")
                nome = input("Digite o novo nome do cliente: ")
                cpf = input('Digite o novo CPF do cliente: ')
                telefone = input("Digite a novo telefone do cliente: ")
                linhas[i] = [nome, cpf, telefone]
                with open("database.csv", "w", newline="") as arquivo:         #w= write
                    escritor = csv.writer(arquivo)
                    escritor.writerows(linhas)
                print("Cliente atualizado com sucesso!")
                
        if not encontrado:
            print("Cliente não encontrado.")
    voltar_menu()


def excluir():
    cpf = input("Digite o CPF do cliente que deseja excluir: ")
    with open("database.csv", "r") as arquivo:
        leitor = csv.reader(arquivo)
        linhas = list(leitor)
        encontrado = False
        for i, linha in enumerate(linhas):
            if cpf in linha:
                encontrado = True
                print(f"Cliente encontrado: {linha}")
                confirmacao = input("Tem certeza que deseja excluir esse cliente? (S/N) ")
                if confirmacao.lower() == "s":
                    del linhas[i]
                    with open("database.csv", "w", newline="") as arquivo:
                        escritor = csv.writer(arquivo)
                        escritor.writerows(linhas)
                    print("Cliente excluído com sucesso!")
                
        if not encontrado:
            print("Cliente não encontrado.")

    voltar_menu()

def voltar_menu():
    return input('Pressione ENTER para retornar ao menu principal.')

limpar = lambda: os.system('cls')   #limpar o console

selecao=0
while not selecao==5: 
   menu()
   selecao == 0
   selecao = int(input('Insira a opção:'))
    
   if selecao == 1:
      limpar()
      cadastro()

   elif selecao==2:
      limpar()
      relatorio()

   elif selecao==3:
      limpar()
      atualizar()

   elif selecao==4:
      limpar()
      excluir()

   elif selecao==5:  #precisa definir para não mostrar a tela do else
      exit()         #função do próprio python que fecha o console

   else:
      limpar()
      print('Insira uma das opções listadas.')
      voltar_menu()
   limpar()
