class carrito:

    def __init__(self) -> None:
        self.seleccion = []
        pass


    def agregarProd(self,prod):
        self.seleccion.append(prod)
        pass


    def finCompra(self):
        total = 0.00
        for prod in (self.seleccion):
            total = total + (int(prod.cantidad) * float(prod.precio))
        return total
