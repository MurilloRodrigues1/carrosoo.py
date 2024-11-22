# Classe dos Motores
class Motor:
    def __init__(self, potencia: float, marca: str):
        self.__potencia = potencia
        self.__marca = marca

    # Getters
    def get_potencia(self):
        return self.__potencia

    def get_marca(self):
        return self.__marca


# Classe das Roda
class Roda:
    def __init__(self, tamanho: int, marca: str):
        self.__tamanho = tamanho
        self.__marca = marca

    # Getters
    def get_tamanho(self):
        return self.__tamanho

    def get_marca(self):
        return self.__marca


# Classe dos Carro
class Carro:
    def __init__(self):
        self.__motor = None
        self.__roda = None

    # Setters
    def set_motor(self, motor: Motor):
        self.__motor = motor

    def set_roda(self, roda: Roda):
        self.__roda = roda

    # Getters
    def get_motor(self):
        return self.__motor

    def get_roda(self):
        return self.__roda

    def exibir_detalhes(self):
        if self.__motor and self.__roda:
            print(f"Carro com Motor marca: {self.__motor.get_marca()}, "
                  f"Potência: {self.__motor.get_potencia()} HP, "
                  f"Roda marca: {self.__roda.get_marca()}, "
                  f"Tamanho: {self.__roda.get_tamanho()}")
        else:
            print("Carro não está completamente montado.")


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
motor1 = Motor(150.0, "Honda")
motor2 = Motor(200.0, "Toyota")
motor3 = Motor(250.0, "Ford")

# Instanciando rodas
roda1 = Roda(17, "Pirelli")
roda2 = Roda(18, "Michelin")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
carro1 = Carro()
carro1.set_motor(motor1)
carro1.set_roda(roda1)

carro2 = Carro()
carro2.set_motor(motor2)
carro2.set_roda(roda1)

carro3 = Carro()
carro3.set_motor(motor3)
carro3.set_roda(roda1)

carro4 = Carro()
carro4.set_motor(motor1)
carro4.set_roda(roda2)

carro5 = Carro()
carro5.set_motor(motor2)
carro5.set_roda(roda2)

carro6 = Carro()
carro6.set_motor(motor3)
carro6.set_roda(roda2)

# - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
carros = [carro1, carro2, carro3, carro4, carro5, carro6]

for i, carro in enumerate(carros, start=1):
    print(f"Carro {i}:")
    carro.exibir_detalhes()
    print("-" * 30)
