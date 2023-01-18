'''
3.Ingrese 3 valores y realice las operaciones de suma ,resta ,multiplicación, división
y división entera.
'''

valor1=float(input("ingrese el primer valor\n"))
valor2=float(input("ingrese el segundo valor\n"))
valor3=float(input("ingrese el tercer valor\n"))

operacion1= valor1 + valor2 + valor3
operacion2= valor1 - valor2 - valor3
operacion3= valor1 * valor2 * valor3
operacion4= valor1 / valor2 / valor3
operacion5= valor1 // valor2 // valor3

print("la suma de valores es {} y la resta es {} y la multiplicacion es {}".format(operacion1,operacion2,operacion3))
print("la division es {} y la division real es {}".format(operacion4,operacion5))
