from moto import Moto
from carro import Carro

carro_toyota = Carro('Toyota', 'Corolla', 4)
carro_jeep = Carro('Jeep', 'Compass', 4)
carro_fiat = Carro('Fiat', 'Uno', 2)

moto_honda = Moto('Honda', 'CG 160', 'casual')
moto_yamaha = Moto('Yamaha', 'Lander 250', 'casual')
moto_harley_davidson = Moto('Harley-Davidson', 'Iron 883', 'esportiva')


print(carro_toyota)
print(carro_jeep)
print(carro_fiat)
print(moto_honda)
print(moto_yamaha)
print(moto_harley_davidson)

