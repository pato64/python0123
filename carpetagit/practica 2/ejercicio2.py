biblioteca = {
    'Ciencia ficción': [
        {'titulo': 'patatas sobre nubes', 'autor': 'portirio humber', 'estado': 'disponible'},
        {'titulo': 'la luna sabe a queso', 'autor': 'ramirio festini', 'estado': 'disponible'}
    ],
    'Terror': [
        {'titulo': 'Dumverso', 'autor': 'dum', 'estado': 'disponible'},
        {'titulo': 'las sombrias aventuras de pedrito', 'autor': 'carly mars', 'estado': 'disponible'}
    ],
    'Aventura': [
        {'titulo': 'dabi el perro feliz', 'autor': 'ernesto silva', 'estado': 'prestado'},
        {'titulo': 'adventure never ends', 'autor': 'pkm-150', 'estado': 'disponible'}
    ]
}

usuarios = []

def obtener_categorias():
    print("Lista de categorías de libros:")
    for categoria in biblioteca.keys():
        print(categoria)

def obtener_libros():
    print("Lista de libros y autores:")
    for categoria, libros in biblioteca.items():
        print('Categoría: {}'.format(categoria))
        for libro in libros:
            print('Titulo: {}, Autor: {}'.format(libro['titulo'],libro['autor']))

def cambiar_estado(titulo, estado_nuevo):
    for categoria, libros in biblioteca.items():
        for libro in libros:
            if libro['titulo'] == titulo:
                libro['estado'] = estado_nuevo
                print("El estado del libro '{}' ha sido cambiado a '{}'.".format(titulo,estado_nuevo))
                return
    print("No se encontró el libro con título '{}'.".format(titulo))

def listar_usuarios():
    print("Lista de usuarios de la biblioteca:")
    for usuario in usuarios:
        print(usuario)

def agregar_usuario(nombre):
    usuarios.append(nombre)
    print("El usuario '{}' ha sido agregado a la lista de usuarios.".format(nombre))

# Uso de las funciones
obtener_categorias()
print("///////////////////")
obtener_libros()
print("///////////////////")
cambiar_estado('patatas sobre nubes', 'prestado')
cambiar_estado('adventure never ends', 'descontinuado')
print("///////////////////")
listar_usuarios()
print("///////////////////")
agregar_usuario('Juan')
agregar_usuario('mauricio')

