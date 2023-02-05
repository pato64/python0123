a = int(input("ingrese el valor de a: "))
b = int(input("ingrese el valor de b: "))

def obtener_mayor(a, b):
    if a > b:
        print("el numero {} es mayor ".format(a))
    else:
        print("el numero {} es mayor ".format(b))
obtener_mayor(a,b)
