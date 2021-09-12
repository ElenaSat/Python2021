from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    #print(objeto)
    print(type(objeto))
    print(objeto.mostar_detalles())
    if isinstance(objeto,Gerente): #valida el tipo de objeto con la clase indicada para acceder al metodo correspondiente
        print(objeto.departamento)

empleado= Empleado('Juan', 5000)
imprimir_detalles(empleado)

gerente= Gerente('Karla', 6000, 'Sistemas')
imprimir_detalles(gerente)