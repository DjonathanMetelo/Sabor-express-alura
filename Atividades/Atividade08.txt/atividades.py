# Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro 
# e retorna uma lista dos livros disponíveis publicados nesse ano.


class Livro:

    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponibilidade = True
        Livro.livros.append(self)

    def __str__(self):
        return f'Titulo {self._titulo} | Autor: {self._autor} | Ano: {self._ano_publicacao} | Disponibilidade: {self._disponibilidade}'

    def emprestar(self):
        self._disponibilidade = not self._disponibilidade

    def verificar_disponibilidade(ano):
        for livro in Livro.livros:
            if livro._ano_publicacao == ano and livro._disponibilidade == True:
                print(f'{livro._titulo} | {livro._autor} | {livro._ano_publicacao}')

    @property
    def disponibilidade(self):
        return 'Disponivel'if self._disponibilidade else 'Indisponivel'
