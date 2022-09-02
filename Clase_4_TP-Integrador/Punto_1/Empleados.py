from opcode import hasconst

class empleado:

    nombre = ''
    apellido = ''
    dni = 0
    edad = 0
    listaVehi = []

    def __init__(self,nom,ape,edad,dni) -> None:
        self.nombre = nom
        self.apellido = ape
        self.edad = edad
        self.dni = dni
        self.listaVehi = []
        pass


    def agregarVehi(self,vehi):
        self.listaVehi.append(vehi)
        pass


    def mostrarLista(self):
        print("Modelo|Patente|Asiento/Carga|Motor")
        for vehiculo in (self.listaVehi):
            print(vehiculo)
        pass


    def buscaPatente(self,pat):
        encontrado = 0
        for vehi in (self.listaVehi):
            if vehi.patente == pat:
                print("Vehiculo encontrado! --> ")
                print(vehi)
                encontrado = 1     
        if encontrado == 0:
            print("Vehiculo no encontrado")    
        pass


    def buscaTipo(self,tipo):
        encontrado = 0
        for vehi in (self.listaVehi):
            if tipo == 'camion':
                if hasattr(vehi,"carga") == True:
                    print (vehi)
                    encontrado = 1
            if tipo == 'auto':
                if hasattr(vehi,"asientos") == True:
                    print (vehi)
                    encontrado = 1
        if encontrado == 0:
            print("No se encontro ningun vehiculo del tipo seleccionado")
        pass



