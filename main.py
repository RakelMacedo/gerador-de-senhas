from data import data_string, salutation_message, banner, error, final_message
from functions import menu, get_password_length, generate_password, finality

while True:
  choice = menu()

  # Se a escolha do usuário for a 1ª
  if choice == '1':
    # Gere uma senha do tamanho escolhido apenas de caracteres minúsculos 
    size = int(get_password_length())
    generate_password(size, data_string['letters'])

  # Se a escolha do usuário for a 2ª
  elif choice == '2':
    # Gere uma senha do tamanho escolhido apenas de caracteres minúsculos e maiúsculos
    size = int(get_password_length())
    generate_password(size, data_string['letters'] + data_string['capital_letters'])

  # Se a escolha do usuário for a 3ª
  elif choice == '3':
    # Gere uma senha do tamanho escolhido composta de caracteres minúsculos, maiúsculos e números
    size = int(get_password_length())
    generate_password(size, data_string['letters'] + data_string['capital_letters'] + data_string['numbers'])

  # Se a escolha do usuário for a 4ª
  elif choice == '4':
    # Gere uma senha do tamanho escolhido composta de caracteres minúsculos, maiúsculos, números e símbolos
    size = int(get_password_length())
    generate_password(size, data_string['letters'] + data_string['capital_letters'] + data_string['numbers'] + data_string['symbols'])
  
  # Se o usuário escolher uma opção inexistente ou digitar uma string
  elif choice != '1,2,3,4':
    # Printe o erro e volte ao menu do programa
    print(error)
    continue
  
  # Encerramento do programa
  choice_finish = finality()
  
  # Se o usuário escolher a 1ª opção, volte ao menu
  if choice_finish == '1':
    continue
  
  # Se o usuário escolher a 2ª opção, encerramos o programa
  elif choice_finish == '2':
    print(final_message)
    break
  
  # Se o usuário escolher uma opção inexistente ou digitar uma string voltamos ao menu principal
  elif choice_finish != '1,2':
    print(error)
    continue
  else:
    pass
