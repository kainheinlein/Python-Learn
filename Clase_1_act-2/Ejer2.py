'''Crear un programa que permita al usuario cargar productos que compro, cada producto tendrá un nombre, una cantidad y un precio unitario, 
crear un método que permita calcular el precio total de los productos multiplicando la cantidad cargada por el precio.
El usuario podrá ver la lista de los productos que compro, la cantidad que compro de cada uno y el precio final de la compra.'''

from math import prod
import Productos
import Carrito

nombre = ''
precio = 0.00
cantidad = 0
salir = ''
total = 0.00
compra = Carrito.carrito()

while salir != '1':
    nombre = input("Ingrese el nombre del producto -> ")
    cantidad = input("Ingrese la cantidad -> ")
    precio = input("Ingrese el precio por unidad -> $")

    nuevoProducto = Productos.producto(nombre,cantidad,precio)
    compra.agregarProd(nuevoProducto)

    salir = input("Presione cualquier tecla para agregar mas productos, 1 para finalizar la compra: ")

total = compra.finCompra()

for producto in (compra.seleccion):
    print('Producto -> ' + producto.nombre + ' | Cantidad -> ' + str(producto.cantidad))

print("Total de la compra -> $" + str(total))