'''2) Una tienda de construcción busca un sistema que le permita clasificar y llevar cuenta de los productos que tiene a la 
venta, la tienda necesita clasificar sus productos en 2 tipos, materiales y herramientas, cada producto tendrá un nombre, un 
precio y un código, los materiales tendrán además una cantidad por bolsa o peso por unidad, en cambio las herramientas 
tendrán una medida. El usuario podrá cargar productos en el programa, luego podrá listar los productos en stock, el usuario 
tendrá la posibilidad de buscar productos específicos filtrando por nombre o código, además podrá eliminar productos de la 
lista y modificar el precio de los mismos, el precio será un atributo protegido que el usuario solo podrá modificar si tiene 
la clave de administrador (no hace falta que la ingrese el usuario, puede estar declarada al inicio del programa)'''


from pprint import pprint
import Herramientas
import Materiales
from os import system

listaProd = []
adminPass = 'admin1234'
nom = ''
opc = ''


def menuPrinc():
    print("\n***Bienvenido***\n")
    print("Seleccione una opcion:")
    print(" 1-Cargar Producto")
    print(" 2-Mostrar Stock")
    print(" 3-Buscar/Eliminar/Modificar Producto")
    print(" 4-Salir")
    aux = input("Opcion elegida --> ")
    return aux


def menuBuscar():
    print("\nSeleccione una opcion de busqueda:")
    print(" 1-Buscar por nombre")
    print(" 2-Buscar por codigo de producto")
    print(" 3-Volver al menu anterior")
    aux = input("Opcion elegida --> ")
    return aux


def menuProducto():
    print("\nSeleccione una opcion")
    print("1-Eliminar producto")
    print("2-Modificar precio")
    print("3-Salir")
    aux = input("Opcion elegida --> ")
    return aux


def buscarProd(valor,opc):
    encontrado = 0
    cont = 0
    for prod in (listaProd):
        if opc == '1' and prod.nombre == valor: #Busqueda por nombre de producto
            print("Producto encontrado!")
            print(prod)
            return cont
        if opc == '2' and prod.codigo == valor: #Busqueda por codigo de producto
            print("Producto encontrado!")
            print(prod)
            return cont
        cont = cont + 1 
    if encontrado == 0:
        print("No se encontraron productos ")


def clearScr():
    system('cls')
    print("\n***Bienvenido***\n")


def ingresoAdmin():
    contra = input("Ingrese la contrasenha de administrador --> ")
    if contra == adminPass:
        return True
    else:
        return False


def creaProd():
    print("Introduzca los datos del producto a continuacion")
    nom = input("Nombre de producto -> ")
    cod = input("Codigo de producto -> ")
    pre = input("Precio de producto -> ")
    prod = None
    while True:
        auxTipo = input("1-Herramienta  |  2-Material   ==> ")
        if auxTipo == '1': #Crea Herramienta
            med = input("Indique la medida de la herramienta -> ")
            prod = Herramientas.herramienta(nom,cod,pre,med)
            break
        elif auxTipo == '2': #Crea Material
            cant = input("Indique la cantidad por bolsa (Ej: 10u) o peso por unidad (Ej: 25Kg)-> ")
            prod = Materiales.material(nom,cod,pre,cant)
            break
        else:
            print("Opcion no valida")
    return prod


def mostrarProd():
    print("Nombre|Codigo|Medida|Precio($)")
    for prod in (listaProd):
        if listaProd.__len__ != 0:
            print(prod)
        else:
            print("No hay productos cargados en el sistema")


opc = menuPrinc()
system('cls')
while True: #Menu Principal
    if opc == '1': #Cargar Productos
        clearScr()
        while True:
            listaProd.append(creaProd())
            print("\nProducto cargado correctamente")
            salir = input("Si desea agregar mas productos presione '1', de lo contrario cualquier tecla para finalizar la carga --> ")
            if salir != '1':
                break
            clearScr()

    elif opc == '2': #Mostrar Lista
        clearScr()
        print("Lista de productos:\n")
        mostrarProd()
        input("\nPresione una tecla para continuar...")

    elif opc == '3': #Buscar Productos
        while True:
            clearScr()
            buscar = menuBuscar()
            if buscar == '1' or buscar == '2':
                valor = input("\nIngrese el nombre o codigo del producto a buscar -> ")
                encontrado = buscarProd(valor,buscar)
                if encontrado != None:
                    opcProducto = menuProducto()
                    while True:
                        if opcProducto == '1': #Eliminar producto
                            listaProd.pop(encontrado)
                            print("\nProducto eliminado correctamente")
                            break
                        elif opcProducto == '2': #Modificar precio
                            cont = 3
                            while cont != 0:
                                ini = ingresoAdmin()
                                if ini == True:
                                    auxProd = listaProd[encontrado]
                                    nuevoPre = input("\nIngrese el nuevo precio del producto -> ")
                                    print("Precio anterior -> " + str(auxProd.GetPrecio()))
                                    auxProd.SetPrecio(int(nuevoPre))
                                    print("Precio nuevo -> " + str(auxProd.GetPrecio()))
                                    print("\nSe modifico el precio correctamente")
                                    break
                                else:
                                    cont = cont -1
                                    input("Contrasenha incorrecta, restan " + str(cont) + " intentos")
                                    clearScr()
                        elif opcProducto == '3':
                            break
                        else:
                            print("Opcion Incorrecta")
                        break
                salir = input("Si desea buscar otro producto presione '1', de lo contrario cualquier tecla para finalizar --> ")
                if salir != '1':
                    break
            elif buscar == '3':
                break
            else:
                input("Opcion incorrecta...")

    elif opc == '4': #Mostrar Camiones
        input("***Presione cualquier tecla para finalizar, que tenga un buen dia***")
        break
    else:
        print("Opcion invalida")
    system('cls')
    opc = menuPrinc()
exit