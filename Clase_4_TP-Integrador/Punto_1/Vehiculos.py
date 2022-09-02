class vehiculo:
    patente = ''
    modelo = ''

    def __init__(self,pat,mod) -> None:
        self.patente = pat
        self.modelo = mod
        pass

    
    def __str__(self) -> str:
        return self.modelo + ' ' + self.patente
        pass