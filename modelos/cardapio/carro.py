from atividades.veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__(self):
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Estado: {self._estado} | Qte de Portas: {self.portas}'