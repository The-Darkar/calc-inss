#  Você foi contratado para fazer um serviço para o INSS. O trabalho consiste em criar um programa que diga a pessoa o ano que ela poderá se aposentar. Você deve perguntar a pessoa, o nome, a idade e criar uma mensagem dizendo em qual ano ela irá aposentar. Considere que todas as pessoas podem se aposentar aos 65 anos de idade.


# criar um programa que diga a pessoa o ano que ela poderá se aposentar.

# 1. Pergunte ao usuário seu nome e idade
# 2. ao receber a idade, exibir mensagem dizendo o ano de aposantadoria
  # 2-1. se a idade for igual ou maior que 65, exibir mensagem confirmando a aposentadoria e o ano de início.
  # 2-2. se a idade for menor que 65, exibir mensagem dizendo quanto tempo falta para se aposentar.

try:
  nome = str(input('Bem vindo a Calculadora de aposentadoria! \n\n Qual o seu nome? ').capitalize())

  nasc = int(input('\n\n Insíra sua idade utilizando *apenas números inteiros*: '))

  if nasc == 65:
    print(f'\n \n INSS informa: {nome}, você já está aposentado!  \n \n Seu benefício teve início este ano')

  elif nasc > 65:
    tempo = nasc - 65
    print(f'\n \n INSS INFORMA: {nome}, você já está aposentado! \n \n seu benefício foi iniciado há {tempo} ano(s) atrás.')

  else:
    tempo2 = 65 - nasc
    print(f'\n \n INSS INFORMA: {nome} você ainda não está aposentado! \n \n Seu benefício estará disponível em {tempo2} ano(s).')

except ValueError:
  print('\n \n ATENÇÃO: Informação inválida! por favor, tente novamente')
 
