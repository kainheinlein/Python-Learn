class medicamento:
    nombre = ''
    precio = ''
    cant = ''
    tipo = ''

    def __init__(self,nom,pre,cant,tipo) -> None:
        self.nombre = nom
        self.precio = pre
        self.cant = cant
        self.tipo = tipo
        pass
