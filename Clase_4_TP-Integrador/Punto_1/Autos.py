import Vehiculos

class auto(Vehiculos.vehiculo):
    asientos = 0
    motor = ''


    def __init__(self,pat,mod,asie,mot) -> None:
        self.asientos = asie
        self.motor = mot
        super().__init__(pat,mod)
    

    def __str__(self) -> str:
        return super().__str__() + ' ' + str(self.asientos) + ' ' + self.motor