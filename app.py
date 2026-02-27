print("""Sabor Express
        """)#Imprime oque estiver escrito entre () para o usuario. a string inserida entre '' será exibida ao usuario. podemos usar aspas triplas (""" """) e um "Enter" para pular a linha

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n')#\n em uma string pula uma linha

opcao_escolhida = input('Escolha uma opção: ')#cria a variavel e atribu um valor a ela depois do '='. solicita ao usuario que digite algo. oque está escrito entre ('') sera exibido ao usuario. neste caso atribuimos a variavel 'opcao_escolhida' o dado inserido pelo usuario no input
print(f'Você escolheu a opção {opcao_escolhida}')#antes de uma strng usamos o 'f' para dentro da string podermos chamar uma variavel e exibr oque está contida dentro dela para o usuario