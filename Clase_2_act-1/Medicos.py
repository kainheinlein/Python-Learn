class medico:

    nombre = ''
    contrasenha = ''
    cuit = 0
    area = ''
    pacientes = []

    def __init__(self,nom,contra,cuit,area) -> None:
        self.nombre = nom
        self.contrasenha = contra
        self.cuit = cuit
        self.area = area
        self.pacientes = []
        pass


    def __str__(self) -> str:
        pass


    def buscarPaciente(self,nom):
        for paciente in (self.pacientes):
            if paciente.nombre == nom:
                print("Paciente encontrado")
                print("Nombre: " + paciente.nombre + "  Edad: " + str(paciente.edad) + " anhos")
                print("Motivo de consulta: " + paciente.motivo)
            else:
                print("Paciente no encontrado")


    def mostrarLista(self):
            print("Nombre|Edad")
            for pac in (self.pacientes):
                print(pac.nombre + " " + str(pac.edad) + "\n") 
            pass


    def agregarPaciente(self,pac):
        self.pacientes.append(pac)

    
    def eliminarPaciente(self,nom):
        cont = 0
        for paciente in (self.pacientes):
            if paciente.nombre == nom:
                self.pacientes.pop(cont)
                print("Paciente eliminado correctamente")
                return
            cont = cont + 1
        print("Paciente no encontrado, no se elimino ningun registro...")
