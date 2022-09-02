from select import select


class producto:
    nombre = ''
    __precio = 0.0
    codigo = ''

    def __init__(self,nom,cod,pre) -> None:
        self.nombre = nom
        self.codigo = cod
        self.__precio = pre
        pass

    
    def __str__(self) -> str:
        return self.codigo + ' ' + self.nombre + ' ' + str(self.__precio)
        pass


    def GetPrecio(self):
        return self.__precio

    
    def SetPrecio(self,pre):
        self.__precio = pre