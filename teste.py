
class Programador:
    def _init_(self, Nome):
        self.Nome = Nome
        self.Equip = None

    def getName(self):
        return self.Nome

    def setName(self, x):
        self.Nome = x

    def getEquip(self):
        return self.Equip

    def setEquip(self, x):
        self.Equip = x

class Equipamento:
    def _init_(self, Marca, Modelo):
        self.Marca = Marca
        self.Modelo = Modelo

    def getMarca(self):
        return self.Marca

    def setMarca(self, x):
        self.Marca = x

    def getModelo(self):
        return self.Modelo

    def setModelo(self, x):
        self.Modelo = x

Marcos = Programador("Marcos")
Marcos.getEquip

Macbook = Equipamento("Apple", "Air")

Marcos.setEquip(Macbook)
Marcos.getEquip()

Marcos.getEquip().getMarca()

Marcos.getEquip().getModelo()