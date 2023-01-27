if __name__ == "__main__":
    texto = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen."

# split
palabras = texto.split()
print ("el texto usando split es: \n")
print(palabras)
print("\n")

# join
texto_join = " ".join(palabras)
print ("el texto usando join es: \n")
print(texto_join)
print("\n")

# count
texto_count = texto.count("texto")
print ("las veces que se encontraron la palabra texto son de: \n")
print(texto_count)
print("\n")

# find
texto_find = texto.find("imprenta")
print ("la posicion en la que se encuentra la palabra 'imprenta' es: \n")
print(texto_find)
print("\n")

# upper case
texto_mayuscula = texto.upper()
print ("el texto en mayuscula es: \n")
print(texto_mayuscula)
print("\n")

# lower case
texto_minuscula = texto.lower()
print ("el texto en minuscula es: \n")
print(texto_minuscula)
print("\n")
