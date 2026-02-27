# Crie um arquivo chamado main.py, importe a classe Livro 
# e, no arquivo main.py, instancie dois objetos da classe Livro 
# e exiba a mensagem formatada utilizando o método str.

from atividades import Livro

def main():
    livro1 = Livro("O Hobbit", "J.R.R. Tolkien", 1937)
    livro2 = Livro("O Sol é Para Todos", "Harper Lee", 1960)

    print(f'{livro1}\n{livro2}')
    
    
if __name__ == '__main__':
    main()
