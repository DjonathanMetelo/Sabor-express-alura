import os #importa uma biblioteca. nesse caso a biblioteca 'os'

restaurantes = ['Pizza', 'Sushi']#cria uma lista, separando os valores por ','

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
    print(texto)

def cadastrar_novo_restaurante():
    os.system('cls')
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')#cria a variavel e atribui um valor a ela depois do '='. neste caso atribuimos a variavel 'nome_do_restaurante' o dado inserido pelo usuario no input.
    restaurantes.append(nome_do_restaurante)#abre a lista e insere o valor contido entre() dentro da lista. nesse oque estiver contido na  variavel 'nome_do_restaurante'
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')#antes de uma strng usamos o 'f' para dentro da string podermos chamar uma variavel e exibr oque está contida dentro dela para o usuario
    voltar_ao_menu_principal()

def listar_restaurantes():
    os.system('cls')
    exibir_subtitulo('Listando restaurantes') 
    for restaurante in restaurantes: #cria um loop, que para cada variavel (nesse caso: 'restaurante'), na lista (nesse caso: 'restaurantes') ele vai executar o codigo abaixo até a lista estar vazia
        print(f'.{restaurante}')
    voltar_ao_menu_principal()


def escolher_opcao():
    try:#tenta executar o codigo abaixo
        opcao_escolhida = int(input('Escolha uma opção: ')) #o int serve para converter em inteiro o valor contido entre (), nesse caso o dado recebido no comando input
        
        if opcao_escolhida == 1: #cria uma condicional e se ela for verdadeira executa o codigo abaxo
            cadastrar_novo_restaurante() 
        elif opcao_escolhida == 2: #caso a condicional não seja verdadeira, ele compara a variavel com outra condconal e se for verdadera executa o codigo abaixo
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
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


