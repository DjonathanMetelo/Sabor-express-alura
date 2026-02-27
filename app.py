import os #importa uma biblioteca. nesse caso a biblioteca 'os'

def exibir_nome_do_programa():#cria uma função que contem um codigo que pode ser chamado futuramente
        print("""Sabor Express
                """)#Imprime oque estiver escrito entre () para o usuario. a string inserida entre '' será exibida ao usuario. podemos usar aspas triplas (""" """) e um "Enter" para pular a linha

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurantes')
    print('4. Sair\n')#\n em uma string pula uma linha

def finalizar_app():
    os.system('cls')#limpa a tela
    print('Finalizando o app')


def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))#cria a variavel e atribu um valor a ela depois do '='. solicita ao usuario que digite algo. oque está escrito entre ('') sera exibido ao usuario. neste caso atribuimos a variavel 'opcao_escolhida' o dado inserido pelo usuario no input. o int serve para converter em inteiro o valor contido entre (), nesse caso o dado recebido no comando input
    ##antes de uma strng usamos o 'f' para dentro da string podermos chamar uma variavel e exibr oque está contida dentro dela para o usuario

    if opcao_escolhida == 1: #cria uma condicional e se ela for verdadeira executa o codigo abaxo
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2: #caso a condicional não seja verdadeira, ele compara a variavel com outra condconal e se for verdadera executa o codigo abaixo
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurantes')
    else: #caso nenhuma das outras condiconais seja verdadeira, se executa o codigo abaixo
        finalizar_app() #chama a função criada anteriormente

def main(): #função principal que contem o programa principal
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__': # This code only runs when you execute this file directly executa esse codigo apenas se este arquivo não estiver sendo exportado, ou seja, apenas executando ele diretamente
    main()


