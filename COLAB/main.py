# ESTE CÓDIGO NÃO VAI RODAR NO WINDOWS, APENAS NO GOOGLE COLAB

from google.colab import output
from modulos import menu, cadastro, relatorio, atualizar, excluir
from funcoes import voltar_menu

selecao = 0
while not selecao==5: 
   menu()

   try:
       selecao == 0
       selecao = int(input('Insira a opção: '))
       # Redirecionamento para cada módulo 
       if selecao == 1:
          output.clear()
          cadastro()

       elif selecao==2:
          output.clear()
          relatorio()

       elif selecao==3:
          output.clear()
          atualizar()
  
       elif selecao==4:
          output.clear()
          excluir()
       # É necessário definir para não mostrar a tela do else
       elif selecao==5:
          # Função do Python que fecha o programa  
          exit()

       else:
          output.clear()
          print('Insira uma das opções listadas.')
          voltar_menu()
       output.clear()

   # Caso o usuário use algo que não seja um número inteiro.
   except ValueError:
       output.clear()
       print('Use um número inteiro!')
       voltar_menu()
   output.clear()
