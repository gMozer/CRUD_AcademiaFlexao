from modulos import menu, cadastro, relatorio, atualizar, excluir
from funcoes import limpar, voltar_menu

selecao = 0
while not selecao==5: 
   menu()

   try:
       selecao == 0
       selecao = int(input('Insira a opção: '))
       # Redirecionamento para cada módulo 
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
       # É necessário definir para não mostrar a tela do else
       elif selecao==5:
          # Função do Python que fecha o programa  
          exit()

       else:
          limpar()
          print('Insira uma das opções listadas.')
          voltar_menu()
       limpar()

   # Caso o usuário use algo que não seja um número inteiro.
   except ValueError:
       limpar()
       print('Use um número inteiro!')
       voltar_menu()
   limpar()
