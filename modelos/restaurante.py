class Restaurante:#cria a classe restaurante

    restaurantes = []

    def __init__(self, nome, categoria): #vai construir para nós um método construtor, que é sempre chamado quando criamos uma instância de um objeto e espera alguma informação.passamos o self como primeiro parâmetro, para entendermos que se trata daquele objeto que estamos referenciando naquele momento. 
        self._nome = nome.title() #cria um dos objetos da classe restaurante
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self): #é um método especial que pega o objeto e define que, se precisarmos mostrar esse objeto em formato de texto, mostraremos determinada informação.
        return f'{self._nome} | {self._categoria}' #retorna um valor ao ser chamado esse metodo
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧'if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo



restaurante_praca = Restaurante('praça', 'Gourmet') #atribui a variavel uma classe, e dentro do (), informa o dado que sera inserido no respectivo objeto na classe
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza Express', 'Italiana') 

Restaurante.listar_restaurantes() #chama a respectiva função dentro da classe

