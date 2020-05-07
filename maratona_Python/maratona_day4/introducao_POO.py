# class
#sintaxe
# self serve para voce acessar as propriedades e metodos da instancia

# polimorfismo,herança e encapsulamento
#ESTUDEM DICIONARIOS, CONJUNTOS, TUPLAS E LISTAS// ARQUIVOS EM PYTHON

'''
class Computador:
    def __init__(self, marca,memoria_ram,placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video= placa_de_video
    pass 
 
computador1 = Computador('Asus', '8gb', ' Nvidia ')
computador2 = Computador('Hp', '4gb', ' atm ')
computador3 = Computador('dell', '10gb', ' geforce ')

print(computador1.marca,computador1.memoria_ram,computador1.placa_de_video)

print(computador2.marca,computador2.memoria_ram,computador2.placa_de_video)

print(computador3.marca,comSputador3.memoria_ram,computador3.placa_de_video)

'''

class Carro(object):
    def __init__(self, estado):
        self.estado = estado

        bmw = Carro('Semi-novo')
        print(bmw.estado)

class Veiculo():
    estado = 'novo'  
class Carro(Veiculo):
 pass

bmw = Carro()
print(bmw.estado)



