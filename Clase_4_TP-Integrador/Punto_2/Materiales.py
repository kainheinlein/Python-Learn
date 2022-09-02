import Productos

class material(Productos.producto):
    cantidad = ''


    def __init__(self,nom,cod,pre,cant) -> None:
        self.cantidad = cant
        super().__init__(nom,cod,pre)
    

    def __str__(self) -> str:
        return super().__str__() + ' ' + self.cantidad