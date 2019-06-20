class Carro(object):
    def _init_(self, kml):
        self.kml = kml
        self.combustivel = 0

    def adicionarGasolina(self, acrecimoDecombustivel):
        self.combustivel = self.combustivel + acrecimoDecombustivel

    def andar(self, km):

        if (km / self.kml) <= self.combustivel:
            self.combustivel = self.combustivel - (km / self.kml)
        else:
            kmFinal = self.kml * self.combustivel
            self.combustivel = 0

            print(f'GAsolina esgotada, você andou: {kmfinal}km e lhe resta: {km - kmFinal}km')

    def obterGasolina(self):
        print(f'Seu tanque ainda tem: {self.combustivel}L de Gasolina')