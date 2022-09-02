import Vehiculos

class camion(Vehiculos.vehiculo):
    carga = 0


    def __init__(self,pat,mod,carga) -> None:
        self.carga = carga
        super().__init__(pat,mod)

    
    def __str__(self) -> str:
        return super().__str__() + ' ' + str(self.carga)