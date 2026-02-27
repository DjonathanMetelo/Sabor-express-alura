from veiculo import Veiculo

class Moto(Veiculo):

    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Estado: {self._estado} | Qte de Portas: {self.tipo}'