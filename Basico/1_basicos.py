# Imprime "Hola mundo" en consola
print('Hola mundo')

# Imprime tu nombre y edad
print("Piero Alvarado | 24 años")

# Imprimir el tipo de datos
print(type(5))

#Formateo de texto y variables
name = "Piero"
surname = "Alvarado"
age = 24

print("Mi nombre es {} {} y tengo {} años".format(name,surname, age))
print("Mi nombre es %s %s y tengo %d años" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y tengo {age} años")

#Desempaquetado de caracteres
lenguaje = "python"
a, b, c, d, e, f = lenguaje
print(a, c, e)

#Split de caracteres
lenguaje_slice = lenguaje[1:3]
print(lenguaje_slice)

lenguaje_slice = lenguaje[1:]
print(lenguaje_slice)

lenguaje_slice = lenguaje[-3]
print(lenguaje_slice)

lenguaje_slice = lenguaje[0:2:4]
print(lenguaje_slice)

#Reversa de caracteres 
lenguaje_reversed = lenguaje[::-1]
print(lenguaje_reversed)

#Listas
my_list = [2,3,4,5]
print(my_list)

#Tuplas
my_tuple = (2,3,4,5,6)
print(my_tuple)

#Sets
my_set = {2,"3",4,"5",6}
print(my_set)

#Diccionario
my_dicc = {"nombre":"Piero", "apellido":"Alvarado"}
print(my_dicc.items())
print(my_dicc.fromkeys("name",my_dicc))

#Condicional IF
valor = ""

if valor:
    print(valor)
else:
    print("else")

