class Veiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._estado = False

    def __str__(self):
        return f'Marca: {self.marca} | Modelo: {self.modelo} | Estado: {self._estado}'