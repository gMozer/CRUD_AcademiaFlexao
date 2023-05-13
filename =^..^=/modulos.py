import csv
from funcoes import voltar_menu, limpar

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
    cabecalho=['Nome', 'CPF', 'Telefone', 'Plano']
    # Cria um arquivo csv e acrescenta um cabeçalho. Caso o arquivo já exista é verificado se possui um cabeçalho.
    with open ('database.csv', 'a', newline='') as arquivoC:
        if arquivoC.tell() == 0:
              escritor = csv.writer(arquivoC)
              escritor.writerow(cabecalho)
              arquivoC.close()

    # Loop que continua até o usuário digitar o nome ou escolher vpltar ao menu principal. 
    while True:
       nome = input("Digite o nome do cliente (ou digite 'sair' para voltar ao menu principal): ")
       # Lower serve para formatar qualquer entrada de dados como minúscula
       if nome.lower() == "sair":
           return
       # Caso o usuário pressione Enter sem querer ele pode tentar novamente.
       elif nome == '':
           print('Insira o nome do cliente corretamente.')
       else:
           break   

    # Loop que continua até o CPF inserido possuir 11 caracteres numéricas.
    while True:                                      
       cpf=input('Insira o cpf do cliente: ')
       if cpf.isdigit() and len(cpf) == 11:
            break
       else:
            print('Insira o cpf com apenas 11 caracteres numéricas')

    # Verifica se o CPF já existe no banco de dados. Caso já exista o usuário é mandado de volta para o módulo de cadastro.
    with open('database.csv', 'r') as arquivo:
        csv_reader = csv.reader(arquivo, delimiter=',')
        # Pula a linha do cabeçalho
        next(csv_reader)
        for row in csv_reader:
          # Se o CPF estiver na coluna 2
          if cpf in row[1]:
              print('CPF já cadastrado ', cpf)
              return cadastro()
          else:
              break

    # Loop que continua até o telefone inserido possuir 11 caracteres numéricas.
    while True:                                              
       telefone=input('Insira o Telefone do cliente: ')
       if telefone.isdigit() and len(telefone) == 11:
            break
       else:
            print('Insira o Telefone com o DDD')

    # Loop que continua até o plano inserido possuir 1 caractere numérico.
    print('Qual plano o cliente escolheu?')
    print('1 - Básico')
    print('2 - Intermediário')
    print('3 - XANDÃO')
    while True:
        plano= input('O plano escolhido foi: ')
        if plano.isdigit() and len(plano) == 1:
            break
        else:
            print('Insira corretamente o plano.')

    # Acrescenta as informações do cliente ao banco de dados.
    with open("database.csv", "a", newline='') as arquivo:
        escritor = csv.writer(arquivo)          
        escritor.writerow([nome, cpf, telefone, plano])
        print("Cliente cadastrado com sucesso!")
    voltar_menu()

##############################################################################################################

def relatorio():
    opcao = 0
    print('Você deseja visualizar um cliente específico ou todos cadastrados no banco de dados? (digite "sair" para voltar ao menu)')
    opcao = input('"um" ou "todos": ')

    if opcao.lower() == 'um':
       # Loop para verificar se o CPF possui 11 caracteres numéricos.
       while True:
            chave = input("Digite o CPF do cliente que deseja visualizar: ")
            if chave.isdigit() and len(chave) == 11:
                break
            else:
              print('Insira o cpf com apenas 11 caracteres numéricas')

       # Variável que define se o cliente existe ou não no banco de dados.
       encontrado = False
       with open("database.csv", "r") as arquivo:         
            leitor = csv.reader(arquivo)
            for linha in leitor:
               if chave in linha:
                    # Se pela chave achar no banco de dados a variável "encontrado" vira verdadeira, após isso é imprimido a linha que a chave está e para o loop. 
                    encontrado = True               
                    print('Cliente encontrado: ', linha)
                    break
       # Se a chave não for encontrada no banco de dados a variável continua negativa, assim retornando ao módulo de relatório.
       if not encontrado:
            print('Cliente não encontrado.')
            return relatorio()

    elif opcao.lower() == 'todos':
        with open('database.csv', 'r') as arquivo:
            leitor = csv.reader(arquivo)
            # Enumerate serve para adicionar um ID para a lista.
            for indice, linha in enumerate(leitor):
                # f = Formata tudo como string.
                print(f'{indice}: {linha}')

    elif opcao.lower() == 'sair':
        return

    else:
        print('Insira uma opção válida.')
        return relatorio()
    voltar_menu()

##############################################################################################################

def atualizar():                                         
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


##############################################################################################################

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
