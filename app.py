import os #importa uma biblioteca. nesse caso a biblioteca 'os'

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                    {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]#cria um dicionario, cada unidade do dicionario esta contido dentro de '{}', cada campo esta entre '' e apos ':' está o valor contido dentro do campo. cada undade do dicionario está separado por ','

def exibir_nome_do_programa():#cria uma função que contem um codigo que pode ser chamado futuramente
        print("""Sabor Express
                """)#Imprime oque estiver entre () para o usuario. podemos usar aspas triplas (""" """) e um "Enter" para pular a linha

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair\n')#\n em uma string pula uma linha

def finalizar_app():
    os.system('cls')#limpa a tela
    exibir_subtitulo('Finalizar app')#chama uma função. envia um valor para a função que será atribuida a variavel correspondente dentro das '()'

def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu principal')#solicita ao usuario que digite algo. oque está escrito entre ('') sera exibido ao usuario.
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):#nesse caso, cria uma variavel dentro dos '()' que deverá receber um valor quando for chamada, e essa mesma varavel pode ser usada dentro da função
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')#cria a variavel e atribui um valor a ela depois do '='. neste caso atribuimos a variavel 'nome_do_restaurante' o dado inserido pelo usuario no input.
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}):')#antes de uma strng usamos o 'f' para dentro da string podermos chamar uma variavel e exibr oque está contida dentro dela para o usuario
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False} #cria-se um dicionario, usando '{}' apos o '=' e o atribui a uma variavel 
    restaurantes.append(dados_do_restaurante) #abre o dconario e insere oque esta contido entre ()
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes') 
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')#ljust vai dar um espaço apos exibir a variavel
    for restaurante in restaurantes: #cria um loop, que para cada variavel (nesse caso: 'restaurante'), na lista (nesse caso: 'restaurantes') ele vai executar o codigo abaixo até a lista estar vazia
        nome_restaurante = restaurante['nome'] #insere na variavel o valor contido dentro do campo na respectva unidade do diconario
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:#cria uma condicional e se ela for verdadeira executa o codigo abaxo
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado: #'not' neste caso vai executar a o codigo caso a variavel seja falso
        print('O restaurante não foi encontrado.')
        
        
    voltar_ao_menu_principal()

def escolher_opcao():
    try:#tenta executar o codigo abaixo
        opcao_escolhida = int(input('Escolha uma opção: ')) #o int serve para converter em inteiro o valor contido entre (), nesse caso o dado recebido no comando input
        
        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante() 
        elif opcao_escolhida == 2: #caso a condicional não seja verdadeira, ele compara a variavel com outra condconal e se for verdadera executa o codigo abaixo
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: #caso nenhuma das outras condiconais seja verdadeira, se executa o codigo abaixo. e nesse caso se a opção digitada não for uma das escolhidas ele encerrará o programa
            opcao_invalida()
    except:#caso não consiga executar o codigo acima ele executa o codigo abaixo
        opcao_invalida()

def main(): #função principal que contem o programa principal
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__': #executa esse codigo apenas se este arquivo não estiver sendo exportado, ou seja, apenas executando ele diretamente
    main()