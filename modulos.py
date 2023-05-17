import csv
from funcoes import voltar_menu

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
    cabecalho=['NOME', 'CPF', 'TELEFONE', 'PLANO']
    # Cria um arquivo csv e acrescenta um cabeçalho. Caso o arquivo já exista é verificado se possui um cabeçalho.
    with open ('database.csv', 'a', newline='') as arquivoC:
        if arquivoC.tell() == 0:
              escritor = csv.writer(arquivoC)
              escritor.writerow(cabecalho)
              arquivoC.close()

    # Loop que continua até o usuário digitar o nome ou escolher vpltar ao menu principal. 
    while True:
       # A função strip faz com que o nome não possa ser um monte de espaços.
       nome = input("Digite o nome do cliente (ou digite 'sair' para voltar ao menu principal): ").strip()
       # Lower serve para formatar qualquer entrada de dados como minúscula
       if nome.lower() == "sair":
           return
       # Caso o usuário pressione Enter sem querer ele pode tentar novamente.
       elif nome == '':
           print('Insira o nome do cliente corretamente!')
       # Função que faz com que a variável "nome" só possa ter letras e espaços. 
       elif all(caractere.isalpha() or caractere.isspace() for caractere in nome):
           break
       else:
           print('Insira o nome do cliente corretamente!')   

    # Loop que continua até o CPF inserido possuir 11 caracteres numéricas.
    while True:                                      
       cpf=input('Insira o cpf do cliente: ')
       if cpf.isdigit() and len(cpf) == 11:
            break
       else:
            print('Insira o cpf com apenas 11 caracteres numéricas!')

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
            print('Insira o Telefone com o DDD!')

    # Loop que continua até o plano inserido possuir 1 caractere numérico.
    print('Qual plano o cliente escolheu?')
    print('1 - Amendobobo')
    print('2 - XANDÃO')
    print('3 - PLUTÃO EXPANDIDO')
    while True:
        plano= input('O plano escolhido foi: ')
        # Lista que só permite a saída do loop caso o número selecionado faça parte da mesma.
        if plano in ['1','2','3']:
            break
        else:
            print('Insira um plano válido!')

    # Acrescenta as informações do cliente ao banco de dados.
    with open("database.csv", "a", newline='') as arquivo:
        escritor = csv.writer(arquivo)     
        # Como os banco de dados utilizam os dados em maiúsculo decidi convertar o "nome" para capslock.     
        escritor.writerow([nome.upper(), cpf, telefone, plano])
        print("Cliente cadastrado com sucesso!")

    voltar_menu()

##############################################################################################################

def relatorio():
    try:
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
                  print('Insira o cpf com apenas 11 caracteres numéricas!')

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
                # Enumerate serve para adicionar IDs para a lista.
                for indice, linha in enumerate(leitor):
                    # f = Formata tudo como string.
                    print(f'{indice}: {linha}')

        elif opcao.lower() == 'sair':
            return

        else:
            print('Insira uma opção válida.')
            return relatorio()

        voltar_menu()
    
    # Caso o arquivo CSV não existe esta mensagem é imprimida.
    except FileNotFoundError:
        print('Cadastre um cliente primeiro!')
        voltar_menu()
 
##############################################################################################################

def atualizar():
    try:                                         
        chave = input('Digite o CPF do cliente que deseja atualizar (ou digite sair para voltar ao menu): ')

        if chave.isdigit() and len(chave) == 11:
            with open('database.csv', 'r') as arquivo:
                leitor = csv.reader(arquivo)
                encontrado = False
                # Define a variável como uma lista
                dados = []
                for linha in leitor:
                    if chave in linha[1]:
                        encontrado = True
                        print(f'Cliente encontrado: {linha}')
                        print('Digite as novas informações:')
                        # Loops iguais ao do cadastro que verificam se as informações digitadas estão corretas.
                        while True:
                            novo_nome = input('Digite o novo nome do cliente: ').strip()
                            if all(caractere.isalpha() or caractere.isspace() for caractere in novo_nome):
                                break
                            elif novo_nome == '':
                                print('Digite o nome corretamente!')
                            else:
                                print('Digite o nome corretamente!')

                        while True:                            
                            novo_telefone = input('Digite a novo telefone do cliente: ')
                            if novo_telefone.isdigit() and len(novo_telefone) == 11:
                                break
                            else:
                               print('Insira o Telefone com o DDD')
                        
                        while True:
                            novo_plano = input('Digite o novo plano do cliente\n(1 - Amendobobo\n2 - XANDÃO\n3 - PLUTÃO EXPANDIDO)\n: ')
                            if novo_plano in ['1','2','3']:
                                break
                            else:
                                print('Insira uma opção válida!')

                        # Grava cada informação no seu array respectivo
                        linha[0] = novo_nome.upper()
                        linha[2] = novo_telefone
                        linha[3] = novo_plano
                    # Coloca as informações gravadas em outra variável
                    dados.append(linha)

            # Modifica as informações no arquivo CSV                        
            if encontrado:
                with open('database.csv', 'w', newline='') as arquivo:
                            escritor = csv.writer(arquivo)
                            escritor.writerows(dados)
                            print('Cliente atualizado com sucesso!')
                            voltar_menu()
                        
            if not encontrado:
                print('Cliente não encontrado.')
                return atualizar()

        elif chave == 'sair':
            return

        else:
            print('Digite uma das opções válidas!')
            return atualizar()

    # Caso o arquivo CSV não existe esta mensagem é imprimida. 
    except FileNotFoundError:
        print('Cadastre um cliente primeiro!')

##############################################################################################################

def excluir():
    try:
        chave = input('Digite o CPF do cliente que deseja excluir (ou "sair" para retornar ao menu): ')

        # Se o usuário digitar "sair" ele volta ao menu.
        if chave.lower() == 'sair':
            return

        # Verificação se a chave digita possui as mesmas propriedades de um CPF.    
        elif chave.isdigit() and len(chave) == 11:
            with open("database.csv", "r") as arquivo:
                leitor = csv.reader(arquivo)
                # Armazena todo o conteúdo do arquivo CSV em uma variável.
                linhas = list(leitor)
                encontrado = False
                # Cria-se um índice com todas as linhas do arquivo CSV.
                for i, linha in enumerate(linhas):
                    # Se a chave coincidir com o CPF na coluna 2 é imprimido o cliente na tela.
                    if chave in linha[1]:
                        encontrado = True
                        while True:
                           print(f"Cliente encontrado: {linha}")
                           print('Tem certeza que deseja excluir esse cliente?')
                           confirmacao = input('Digite "sim" ou "nao": ')
                           if confirmacao.lower() == "sim":
                               # Excluí-se a linha do cliente baseado pelo seu índice.
                               del linhas[i]
                               with open("database.csv", "w", newline="") as arquivo:
                                   escritor = csv.writer(arquivo)
                                   escritor.writerows(linhas)
                               print('Cliente excluído com sucesso!')
                               break
                        
                           elif confirmacao.lower() == "nao":
                                print('O cliente não foi excluído.')
                                break

                           else:
                               print('Digite "sim" ou "nao".')

                # Se a chave não existe no banco de dados o usuário volta para o módulo excluir.        
                if not encontrado:
                    print('Cliente não encontrado.')
                    return excluir()

            # A função fica neste espaçamento para os IFs de confirmação.
            voltar_menu()

        else:
            print('Digite corretamente!')
            return excluir()

    # Caso o arquivo CSV não existe esta mensagem é imprimida.        
    except FileNotFoundError:
        print('Cadastre um cliente primeiro!')
        voltar_menu()

# FIM DO PROGRAMA! =^..^=
##############################################################################################################
