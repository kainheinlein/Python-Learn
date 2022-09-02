'''1) Un centro de distribución requiere de un sistema para administrar su personal del área de entregas, de cada empleado 
se tendrá el nombre y apellido, la edad, el DNI y una lista de los vehículos que utiliza para realizar las entregas, todos 
los vehículos tienen un numero de patente y un modelo, si el vehículo es un camión también tendrá un peso de carga máximo 
y si es un auto tendrá como dato la cantidad de asientos y el tipo de motor (diésel, gas, nafta). Cuando se abra el programa 
el usuario podrá cargar un nuevo empleado o ingresar a la cuenta de un empleado ya creado (Buscar por nombre, no tendrán contraseña), 
si el usuario ingresa como empleado podrá cargar vehículos a su lista y podrá verlos listados, además podrá filtrar la 
búsqueda de vehículos ya sea por tipo o por patente.'''

import copy
from os import system
from turtle import clear
import Camiones
import Autos
import Empleados

listaEmp = []
nom = ''
opc = ''
opcEmp = ''
usu = ''
empleActual = None
indiceEmp = 0
vehiculo = None


def menuPrinc():
    print("***Bienvenido***\n")
    print("Seleccione una opcion:")
    print(" 1-Ingresar")
    print(" 2-Carga nuevo empleado")
    print(" 3-Salir")
    aux = input("Opcion elegida --> ")
    return aux

def menuEmp():
    print("\nSeleccione una opcion:")
    print(" 1-Mostrar lista de vehiculos")
    print(" 2-Mostrar lista de autos")
    print(" 3-Mostrar lista de camiones")
    print(" 4-Buscar por patente")
    print(" 5-Cargar vehiculo")
    print(" 6-Volver al menu anterior")
    aux = input("Opcion elegida --> ")
    return aux


def clearEmp():
    system('cls')
    print("***Bienvenido " + empleActual.nombre + "***\n")


def ingreso():
    usu = input("Ingrese su nombre --> ")
    cont = 0
    for emp in listaEmp:
        if  emp.nombre == usu:
            global empleActual
            global indiceEmp
            empleActual = copy.deepcopy(listaEmp[cont])
            indiceEmp = cont
            return True
        cont = cont + 1
    return False


def creaVehi():
    print("Introduzca los datos a continuacion")
    pat = input("Patente -> ")
    mod = input("Modelo -> ")
    tipo = ''
    carga = 0
    vehi = None
    asientos = 0
    motor = ''
    while True:
        auxTipo = input("1-Camion  |  2-Auto   ==> ")
        if auxTipo == '1':
            tipo = 'Camion'
            carga = input("Indique la capacidad maxima de carga -> ")
            vehi = Camiones.camion(pat,mod,int(carga))
            break
        elif auxTipo == '2':
            tipo = 'Auto'
            asientos = input("Indique la cantidad de asientos -> ")
            while True:
                auxMotor = input("1-Nafta | 2-Diesel | 3-Gas   ==> ")
                if auxMotor == '1':
                    motor = 'Nafta'
                    break
                elif auxMotor == '2':
                    motor = 'Diesel'
                    break
                elif auxMotor == '3':
                    motor = 'Gas'
                    break
                else:
                    print("Opcion no valida")
            vehi = Autos.auto(pat,mod,int(asientos),motor)
            break
        else:
            print("Opcion no valida")
    return vehi


def crearEmp():
    nombre = input("Ingrese el nombre --> ")
    ape = input("Ingrese el apellido --> ")
    edad = input("Ingrese la edad --> ")
    dni = input("Ingrese el DNI --> ")
    auxemp = Empleados.empleado(nombre,ape,edad,dni)
    return auxemp

opc = menuPrinc()
system('cls')
while opc != '3': #Menu Principal
    if opc == '1':
        cont = 3
        while cont != 0: #Inicio de Sesion
            ini = ingreso()
            if ini == True:
                clearEmp()
                opcEmp = menuEmp()
                while True: #Menu Empleados
                    clearEmp()
                    if opcEmp == '1': #Mostrar Lista
                        print("Lista de vehiculos:")
                        #listaEmp[cont]
                        empleActual.mostrarLista()
                    elif opcEmp == '2': #Mostrar Autos
                        print("Lista de autos")
                        empleActual.buscaTipo("auto")  
                    elif opcEmp == '3': #Mostrar Camiones
                        print("Lista de camiones")
                        empleActual.buscaTipo("camion") 
                    elif opcEmp == '4': #Buscar por Patente
                        pat = input("Ingrese la patente que desea buscar --> ")
                        empleActual.buscaPatente(pat)
                    elif opcEmp == '5': #Agregar vehiculo a lista
                        while True:
                            vehiculo = empleActual.agregarVehi(creaVehi())
                            print("*Vehiculo agregado a su lista Exitosamente*")
                            salir = input("Si desea agregar mas vehiculos presione '1', de lo contrario cualquier tecla para finalizar la carga --> ")
                            if salir != '1':
                                break
                            else:
                                clearEmp()
                    elif opcEmp == '6': #Salir
                        listaEmp[indiceEmp] = copy.deepcopy(empleActual)
                        empleActual = None
                        break
                    else:
                         print("Opcion no valida")
                    opcEmp = menuEmp()                  
                break
            else:
                cont = cont - 1
                print("Usuario no encontrado, restan " + str(cont) +" intentos")
    elif opc == '2':
        while True:
            listaEmp.append(crearEmp())
            print("Empleado cargado de manera Exitosa")
            salir = input("Si desea agregar mas empleados presione '1', de lo contrario cualquier tecla para finalizar la carga --> ")
            if salir != '1':
                break
            system('cls')
    elif opc == '3':
        print("***Saliendo del sistema, que tenga un buen dia***")
        exit
    else:
        print("Opcion invalida")
    system('cls')
    opc = menuPrinc()