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
