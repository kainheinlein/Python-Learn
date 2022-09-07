from glob import glob
from select import select
import sqlite3
from os import system


db = sqlite3.connect('farmacia.db') #Conecta a la db, caso contrario la crea
db.execute("PRAGMA foreign_keys = 1") #Habilita el uso de foreing keys
db.commit() #Guarda cambios en db
cursor = db.cursor()
usuActual = " "
salir = ''


def iniDB(): #Inicializacion de la Base de Datos
    
    try: #Inicializacion de tabla Usuarios
        cursor.execute(
        """CREATE TABLE usuarios(
            idUsuario integer NOT NULL PRIMARY KEY,
            usuario text,
            contrasenha text)
        """
        )
        #Carga de datos a la tabla Usuarios
        cursor.execute(
            """INSERT INTO usuarios(usuario,contrasenha)
            VALUES('empleado1','1234'),
            ('empleado2','5678')
            """
        )
    except: #Si la tabla ya esta creada se ejecuta el mensaje
        print("Usuarios cargados")
    else: #Se ejecuta si no ocurrio ningun error en el try
        print("Tabla usuarios creada")
    db.commit()

    try: #Inicializacion de tabla Tipos   
        cursor.execute(
         """CREATE TABLE tipos(
            idTipo integer NOT NULL PRIMARY KEY,
            tipo text NOT NULL
            )
        """
        )
        cursor.execute(
            """INSERT INTO tipos(tipo)
            VALUES('con receta'),
            ('sin receta'),
            ('especializado')
            """
        )
    except:
        print('Tipos cargados')
    else:
        print("Tabla tipos creada")
    db.commit()

    try: #Inicializacion de tabla Medicamentos    
        cursor.execute(
         """CREATE TABLE medicamentos(
            idMedicamento integer NOT NULL PRIMARY KEY,
            nombre text NOT NULL,
            precio real NOT NULL,
            stock integer NOT NULL DEFAULT 0,
            idTipo integer NOT NULL,
            FOREIGN KEY (idTipo)
            REFERENCES tipos (idTipo)
            )
        """
        )
        # idTipo integer NOT NULL --> Columna idTipo como entero, no puede ser vacio
        #FOREIGN KEY (idTipo) --> Se indica idTipo como Clave Foranea
        #REFERENCES tipos (idTipo) --> Se indica a que tabla se hace referencia
    except:
        print("Medicamentos cargados")
    else:
        print("Tabla medicamentos creada")
    db.commit()

    try: #Inicializacion de tabla Ventas   
        cursor.execute(
         """CREATE TABLE ventas(
            idVenta integer NOT NULL PRIMARY KEY,
            comprador text NOT NULL,
            monto real NOT NULL,
            idUsuario integer NOT NULL,
            FOREIGN KEY (idUsuario)
            REFERENCES usuarios (idUsuario)
            )
        """
        )
    except:
        print("Ventas cargadas")
    else:
        print("Tabla Ventas creada")
    finally:
        input("Presione Enter para comenzar el programa...")
    db.commit()


def clearSCR():
    system('cls')
    print("***BIENVENIDO***")


def menuLog(): #Menu de seleccion de usuario
    print("\nSELECCIONE SU NUMERO DE USUARIO")
    print("1 - empleado1")
    print("2 - empleado2")
    print("3 - Salir del programa")
    usu = input("Opcion elegida --> ")
    return usu


def menuPrincipal():
    print("\nSELECCIONE UNA OPCION")
    print("1- Cargar/Actualizar medicamentos")
    print("2- Realizar venta")
    print("3- Mostrar stock")
    print("4- Salir")
    opc = input("Opcion seleccionada --> ")
    print("\n")
    return opc


def ingreso(us): #Ingreso y Verificacion de contraseña
    global usuActual
    #Busco que la opcion elegida se encuentre dentro de la tabla
    cursor.execute(
        f"""SELECT idUsuario FROM usuarios WHERE idUsuario = {us}"""
    )
    datos = cursor.fetchall()
    if len(datos) == 0: #len = 0 indicaria q no se encuentro datos en la tabla
        print("USUARIO NO ENCONTRADO")
        input("Presione cualquier tecla para volver al menu anterior...")
        clearSCR()
    else:
        contra = input("\nINGRESE LA CONTRASEÑA --> ")
        #Selecciono la fila donde el usuario seleccionado coincida con algun idUsuario en la tabla Usuarios
        cursor.execute(
            f"""SELECT contrasenha FROM usuarios WHERE idUsuario = {us}"""
        )
        dbContra = cursor.fetchall() #Copio lo seleccionado y asigno el contenido a la variable
        if (dbContra[0][0]) == contra:
            usuActual = us
            return True
        else:
            return False


def cargaDB(nom,pre,cant,tipo): #Carga del medicamento a la DB
    cursor.execute(
    f"""SELECT nombre FROM medicamentos"""
    )
    aux = cursor.fetchall()
    existe = False
    for nombre in aux: #Busco coincidencia entre nombre ingresado y tabla
        if (nombre[0]) == nom:
            existe = True
            try:
                cursor.execute(
                    f"""UPDATE medicamentos
                    SET precio = '{pre}',
                    stock = '{cant}',
                    idTipo = '{tipo}'
                    WHERE nombre = '{nom}'
                    """
                )
                db.commit()
            except Exception as e:
                print(e)
            else:
                print("\nMedicamento actualizado correctamente")
    if existe == False:
        try:
            cursor.execute(
                f"""INSERT INTO medicamentos(nombre,precio,stock,idTipo)
                VALUES('{nom}','{pre}','{cant}','{tipo}')
                """
            )
            db.commit()
        except Exception as e:
            print(e)
        else:
            print("\nMedicamento cargado correctamente")


def creaMedi(): #Carga de valores del medicamento
    clearSCR()
    print("**SECCION DE CARGA**\n")
    print("Si el medicamento a cargar ya existe se actualizaran sus datos")
    try:
        nom = input("Ingrese el nombre del medicamento --> ")
        pre = float(input("Ingrese el precio --> "))
        cant = int(input("Ingrese el stock disponible --> "))
    except:
        print("Datos Incorrectos\n")
    else:
        while True:
            auxTipo = input("1-con receta| 2-sin receta | 3-especializado --> ")
            if auxTipo == '1':
                tipo = 1
                break
            elif auxTipo == '2':
                tipo = 2
                break
            elif auxTipo == '3':
                tipo = 3
                break
            else:
                print("Opcion no valida")
        cargaDB(nom,pre,cant,tipo)


def mostrar(): #Mostrar Stock
    print("******STOCK DISPONIBLE******\n")
    cursor.execute(
        """SELECT * FROM medicamentos WHERE stock > 0
        """
    )
    datos = cursor.fetchall()
    for med in datos:
        print(f'Nombre: {med[1]}        Precio: ${med[2]}     Stock: {med[3]}     Tipo: {med[4]}')


def vender(prod,cant): #Carga de ventas en DB y actualizacion de stock
    #Buscamos coincidencia del medicamento ingresado con la Base de Datos
    cursor.execute(
        f"""SELECT precio FROM medicamentos WHERE nombre = '{prod}'"""
    )
    datos = cursor.fetchall()
    if len(datos) != 0:
        total = int(cant) * float((datos[0][0])) #Calculo del total a pagar
        venta = input("Presione 1 para confirmar la venta, cualquier otra para cancelar --> ")
        if venta == '1':
            doc = input("\nIntroduzca el DNI del cliente --> ")
            print("**RESUMEN DE VENTA**")
            input(f'Producto: {prod}   Cantidad vendida: {cant}\nTotal de compra: ${str(total)}\nEnter para finalizar...')
            try: #Crea registro en Tabla de ventas
                cursor.execute(
                    f"""INSERT INTO ventas(comprador,monto,idUsuario)
                    VALUES('{doc}','{total}','{usuActual}')
                    """
                )
            except Exception as e:
                print(e)
                input("error")
            else:
                db.commit()
            
            try: #Actualizacion de stock en la Tabla medicamentos
                cursor.execute(
                    f"""UPDATE medicamentos
                    SET stock = stock - '{cant}'
                    WHERE nombre = '{prod}'
                    """
                )
            except Exception as e:
                print(e)
            else:
                db.commit()
    else:
        print("**PRODUCTO NO ENCONTRADO")
        input("Presione cualquier tecla para continuar")


iniDB()
clearSCR()
while salir != '1':
    usu = menuLog()
    cont = 3
    if usu != '3':
        while cont != 0:
            ini = ingreso(usu)
            if ini == True:
                while True:
                    clearSCR()
                    opcPrin = menuPrincipal()
                    if opcPrin == '1':#Carga/Actualiza Medicamentos
                        while True:
                            creaMedi()
                            continuar = input("Presione cualquier tecla para continuar la carga, presione 1 para salir --> ")
                            clearSCR()
                            if continuar == '1':
                                break
                    elif opcPrin == '2':#Realizar Venta
                        clearSCR()
                        print("*****SECCION DE VENTAS*****\n")
                        prod = input("Introduzca el nombre del producto a vender --> ")
                        cant = input("Introduzca la cantidad a vender --> ")
                        vender(prod,cant)
                    elif opcPrin == '3':#Mostrar Stock
                        clearSCR()
                        mostrar()
                        input("\nPresione cualquier tecla para volver al menu anterior...")
                    elif opcPrin == '4':#Salir
                        cont = 0
                        break
                    else:
                        print("**OPCION INCORRECTA**")        
            elif ini == False:
                print("\n**Contraseña incorrecta")
                opc = input("Presione cualquier tecla para reintentar || 1 - Menu anterior --> ")
                clearSCR()
                if opc != '1':
                    cont = cont - 1
                else:
                    break
            else:
                break
    else:
        salir = '1'
db.close()
input("\n***PROGRAMA FINALIZADO***")

            
        


