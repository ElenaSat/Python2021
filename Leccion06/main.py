"""
mi_funcion_python
miFuncionPython camello altos y bajos

def miFuncion(nombre,apellido):
    print(f'Saludos desde mi funcion {nombre} y {apellido}')

miFuncion("Elena","apellidodsad")

"""

def mult(*numeros):
    result=1
    for i in numeros:
       result*=float(i)
    return result
print(f'Resultado de la suma: {mult(2,3,4)}')