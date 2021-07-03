from data import data_string, salutation_message, banner, options, menu_message, error, size_message, final_question, final_message
import random

# Função do Menu
def menu():
  print(salutation_message)
  print(banner)
  print(options)
  return input(str(menu_message))

# Função referente ao tamanho da senha 
def get_password_length():
  return input(str(size_message))

# Função para a geração da senha 
def generate_password(size, characters_bag):
  password = ''
  for character in range(size):
    password += random.choice(characters_bag)
  print(f'\nAqui está sua senha : >>>  {password}  <<<\n')

# Função para o encerramento do programa
def finality():
  print(final_question)
  return input(str(menu_message))
