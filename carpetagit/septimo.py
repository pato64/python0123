'''
Realiza un programa que lea 2 números por teclado y determine
los siguientes aspectos:
● Si los dos números son iguales
● Si los dos números son diferentes
● Si el primero es mayor que el segundo
● Si el segundo es mayor o igual que el primero
'''

Num1 = int(input("introducir el primer valor\n"))
Num2 = int(input("introducir el segundo valor\n"))

if Num1==Num2:
    print("el numero {} es igual que {}".format(Num1,Num2))
elif Num2<Num1:
    print("el numero {} es mayor que {}".format(Num1,Num2))
    print("el numero {} es distinto que {}".format(Num1,Num2))
elif Num2>=Num1:
    print("el numero {} es mayor o igual que {} ".format(Num2,Num1))
    print("el numero {} es distinto que {}".format(Num1,Num2))
