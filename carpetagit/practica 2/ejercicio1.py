while True:
    print("""
    1. Dibujar un cuadrado en consola con *
    2. Identificar números múltiplos de 2
    3. Imprimir mayores de edad
    4. Salir
    """)

    opcion = int(input("Seleccione una opción (1-4): "))

    if opcion == 1:
        tamaño = int(input("Ingrese el tamaño del cuadrado: "))
        for i in range(tamaño):
            print("*" * tamaño)

    elif opcion == 2:
        numeros = [int(num) for num in input("Ingrese una lista de números separados por comas: ").split(",")]
        for num in numeros:
            if num % 2 == 0:
                print(f"{num} es múltiplo de 2")

    elif opcion == 3:
        print("necesito un poco de ayuda en esta no lo veo tan clara la logica")

    elif opcion == 4:
        print("Hasta pronto!")
        break

    else:
        print("Opción inválida")
