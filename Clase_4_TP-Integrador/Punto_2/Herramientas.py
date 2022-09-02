import Productos

class herramienta(Productos.producto):
    medida = ''


    def __init__(self,nom,cod,pre,med) -> None:
        self.medida = med
        super().__init__(nom,cod,pre)

    
    def __str__(self) -> str:
        return super().__str__() + ' ' + self.medida