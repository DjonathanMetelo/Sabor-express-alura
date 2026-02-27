class Restaurante:#cria a classe restaurante

    restaurantes = []

    def __init__(self, nome, categoria): #vai construir para nós um método construtor, que é sempre chamado quando criamos uma instância de um objeto e espera alguma informação.passamos o self como primeiro parâmetro, para entendermos que se trata daquele objeto que estamos referenciando naquele momento. 
        self.nome = nome #cria um dos objetos da classe restaurante
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self): #é um método especial que pega o objeto e define que, se precisarmos mostrar esse objeto em formato de texto, mostraremos determinada informação.
        return f'{self.nome} | {self.categoria}' #retorna um valor ao ser chamado esse metodo
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


restaurante_praca = Restaurante('Praça', 'Gourmet') #atribui a variavel uma classe, e dentro do (), informa o dado que sera inserido no respectivo objeto na classe
restaurante_pizza = Restaurante('Pizza Express', 'Italiana') 

#restaurantes = [restaurante_praca, restaurante_pizza]

# print(restaurante_praca)
# print(restaurante_pizza)

Restaurante.listar_restaurantes() #chama a respectiva função dentro da classe
