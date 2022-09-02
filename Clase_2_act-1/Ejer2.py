'''Crear un sistema de gestión para un hospital, el sistema permitirá crear cuentas de médicos, al iniciar el programa nos preguntará si queremos crear una cuenta o ingresar a una ya 
creada, cada médico tendrá como datos: nombre, contraseña, cuit, área (adultos, pediátrico). Los médicos podrán cargar pacientes en el sistema, cada médico tendrá su propia lista de 
pacientes, además de esto los médicos podrán eliminar pacientes de la lista y buscar pacientes por nombre además de esto podrán leer su motivo de consulta y visualizar la lista completa
de pacientes. Cada paciente tendrá como datos: Nombre, Edad, Motivo de consulta.Si un medico es pediátrico no permitir el ingreso de pacientes mayores a 18 años, si el medico es de 
adultos no permitir el ingreso de pacientes menores a 18 años.'''

from os import system
import Pacientes
import Medicos

nombre = ''
contra = ''
edad = 0
cuit = 0
opc = ''
area = ''
medicoActual = None
listaMedicos = []


def menuMedico():
    print("Seleccione una opcion")
    print("1- Cargar paciente")
    print("2- Mostrar listado de pacientes")
    print("3- Buscar paciente")
    print("4- Eliminar paciente")
    print("5- Menu anterior")
    opc = input("Opcion --> ")
    system('cls')
    return opc


def mostrarMenu():
    print("Seleccione una opcion")
    print("1- Crear nueva cuenta")
    print("2- Ingresar al sistema")
    print("3- Finalizar programa")
    opc = input("Opcion --> ")
    system('cls')
    return opc


def crearCuenta():
    nombre = input("Ingrese el nombre -> ")
    contra = input("Ingrese una contraseña -> ")
    cuit = int(input("Ingrese el CUIT ->"))
    while True:
        aux = input("Area: 1- Adultos | 2- Pediatria --> ")
        if aux == '1':
            area = 'Adultos'
            break
        elif aux == '2':
            area = 'Pediatria'
            break
        else:
            print("Opcion incorrecta")
            return
    medico = Medicos.medico(nombre,contra,cuit,area)
    listaMedicos.append(medico)
    return


def cargaPaciente():
    salir = '1' 
    while salir == '1':
        nombre = input("Ingrese el nombre del paciente -> ")
        edad = int(input("Ingrese la edad del paciente -> "))
        mot = input("Ingrese el motivo de la consulta -> ")
        newPaciente = Pacientes.paciente(nombre,edad,mot)
        if (medicoActual.area == 'Pediatria' and edad < 18) or (medicoActual.area == 'Adultos' and edad >= 18):
            medicoActual.agregarPaciente(newPaciente)
            print("\n**Paciente cargado correctamente**")
        else: 
            print("La edad del paciente no corresponde a la designada para su area...")
        salir = input("Si desea cargar otro paciente presione '1', de lo contrario presione cualquier tecla --> ")
    


def ingreSist():
    cont = 3
    while cont != 0:
        user = input("Por favor ingrese su nombre -> ")
        contra = input("Por favor ingrese su contrasenha -> ")
        for med in (listaMedicos):
            if (user == med.nombre) and (contra == med.contrasenha):
                global medicoActual 
                medicoActual = med
                return True
        cont = cont - 1
        print("Contrasenha incorrecta, quedan " + str(cont) + " intentos")
    return False


opc = mostrarMenu()
while opc != '3':
    if opc == '1':
        crearCuenta()
    elif opc =='2':
        while True:
            salir = ''
            log = ingreSist()
            if log == True:
                while True:
                    system('cls')
                    opcMed = menuMedico()
                    if opcMed == '1':
                        cargaPaciente()
                    elif opcMed == '2':
                        medicoActual.mostrarLista()
                        input("\nPresione cualquier tecla para continuar...")
                    elif opcMed == '3':
                        buscar = input("Introduzca el nombre del paciente que desea buscar -> ")
                        medicoActual.buscarPaciente(buscar)
                        input("\nPresione cualquier tecla para continuar...")
                    elif opcMed == '4':
                        elim = input("Introduzca el nombre del paciente que desea eliminar -> ")
                        medicoActual.eliminarPaciente(elim)
                        input("\nPresione cualquier tecla para continuar...")
                    elif opcMed == '5':
                        salir = 'ok'
                        break
                    else:
                        input("Opcion incorrecta, presione cualquier tecla para continuar...")
            else:
                input("Login incorrecto, presione cualquier tecla para continuar...")
                break
            if salir == 'ok':
                break          
    elif opc == '3':
        input("Programa finalizado...")
        exit
    else:
        input("Opcion incorrecta, presione cualquier tecla para continuar...")
    print("")
    opc = mostrarMenu()
    
                           

