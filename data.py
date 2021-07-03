# Caracteres usados para gerar as senhas
data_string = { 
'letters':'abcdefghijklmnopqrstuvwxyz',
'capital_letters':'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
'numbers':'0123456789',
'symbols':'!@#$%&*()[]{}_-+=|\<>:;?/'
}

# Mensagem de Boas-Vindas
salutation_message = '\nOlá, Bem-vindo ao Gerador de Senhas 1.0 !!\n'

banner = '░██████╗░███████╗██████╗░░█████╗░██████╗░░█████╗░██████╗░  ██████╗░███████╗\n██╔════╝░██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔════╝\n██║░░██╗░█████╗░░██████╔╝███████║██║░░██║██║░░██║██████╔╝  ██║░░██║█████╗░░\n██║░░╚██╗██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔══██╗  ██║░░██║██╔══╝░░\n╚██████╔╝███████╗██║░░██║██║░░██║██████╔╝╚█████╔╝██║░░██║  ██████╔╝███████╗\n░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝\n\n░██████╗███████╗███╗░░██╗██╗░░██╗░█████╗░░██████╗  ░░███╗░░░░░░█████╗░\n██╔════╝██╔════╝████╗░██║██║░░██║██╔══██╗██╔════╝  ░████║░░░░░██╔══██╗\n╚█████╗░█████╗░░██╔██╗██║███████║███████║╚█████╗░  ██╔██║░░░░░██║░░██║\n░╚═══██╗██╔══╝░░██║╚████║██╔══██║██╔══██║░╚═══██╗  ╚═╝██║░░░░░██║░░██║\n██████╔╝███████╗██║░╚███║██║░░██║██║░░██║██████╔╝  ███████╗██╗╚█████╔╝\n╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ╚══════╝╚═╝░╚════╝░'

# Opções do menu do programa
options = ('\nConforme sua necessidade, escolha um número referente a força de sua senha.\n\n1) Muito fraca: Formada apenas de caracteres aleatórios minúsculos.\n2) Fraca: Uma mistura de caracteres minúsculos e maiúsculos.\n3) Média: Composta aleatoriamente por caracteres minúsculos, maiúsculos e números.\n4) Forte: Combo aleatório de caracteres minúsculos, maiúsculos, números e símbolos.\n')

# Mensagem referente a escolha do menu
menu_message = 'Digite aqui o número da opção desejada >> '

# Mensagem de erro caso o usuário coloque um número não presente nas opções ou uma string como resposta 
error = '\n🚫  Por favor, digite apenas números correspondentes as opções passadas.\n🚫  Tente novamente\n'

# Mensagem referente ao tamanho da senha do usuário
size_message = '\nDigite o tamanho de sua senha (Quantidade de caracteres)\nPara uma senha forte, recomendamos de 18 caracteres pra cima >> '

# Opções para o usuário depois da geração da senha
final_question = 'O que deseja fazer?\n\n1) Voltar para o menu\n2) Encerrar Gerador de Senhas 1.0\n'

# Mensagem de agradecimento 
final_message = '\nObrigada por usar o Gerador de Senhas 1.0 !!\nVolte sempre que quiser ! S2\n'
