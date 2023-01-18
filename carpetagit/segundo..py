''''
2.Calcule el área de un círculo, triángulo y cuadrado
con radio ingresado desde el teclado.
'''
base = float(input("ingrese el valor de la base\n "))
altura = float(input("ingrese el valor de la altura\n "))
radio = float(input("ingrese el valor del radio\n "))

areaCuadrado = base*altura
areaTriangulo = (base*altura)/2
areaCirculo = (3.14*radio**2)

print("el area del cuadrado con los datos es {}".format(areaCuadrado))
print("el area del triangulo con los datos es {}".format(areaTriangulo))
print("el area del circulo con los datos es {}".format(areaCirculo))