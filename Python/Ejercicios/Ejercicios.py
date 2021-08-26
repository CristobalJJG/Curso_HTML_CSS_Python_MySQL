#Multiplicar dos numeros sin usar el simbolo de multiplicacion
def mult():
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))
    res = 0
    if n2<n1:
        for x in range(n2): res += n1
    else:
        for x in range(n2): res += n1
    print(res)

#Ingresar el nombre y apellido e imprimirlo al reves
def nombre_reves():
    nombre = input("Nombre y apellidos: ")
    print("".join(reversed(nombre)))
    print(nombre[::-1])

#Escribir la funcion que encuentre el elemento menor de una lista
def menor_de_lista():
    lista = [5, 13, 8, 50, 23, 13, 15, 6, -5, 13, 9, 8, 51, 60, 165, 13]
    res = lista[0]
    for i in lista:
        if i<=res: res = i
    print(res)

#Escribir una funcion que devuela el volumen de una esfera por su radio (4/3 * pi * r^2 *3)
def calcular_volumen(r):
    res = (4 / 3 * 3.14 * r ** 3)
    print(res)

#Escribir una funcion que indique si el usuario es mayor de edad
def mayor_de_edad():
    print("Es mayor de edad.") if int(input("Escribe tu edad: "))>18 else print("Es menor de edad.")

#Escribir una funcion que indique si un numero es par o impar
def par_impar():
    print("Es par.") if int(input("Pon un número: "))%2 == 0 else print("Es impar.")

#Escribir una funcion que indique cuantas vocables tiene una palabra
def vocales():
    res = 0
    for x in input("Escribe una palabra: "):
        if ['a', 'e', 'i', 'o', 'u'].__contains__(x.lower()): res+=1
    print(res)

def vocales2():
    res = 0
    for y in input("Escribe una palabra: "):
        x = y.lower()
        res +=1 if x=='a'or x=='e'or x=='i'or x=='o' or x=='u' else 0
    print(res)

#Escribir una aplicacion que reciba una cantidad infinita de numeros hasta decir basta, luego que devuelva la suma de los numeros ingresados
def suma_de_lista_dinamica():
    entry, lista, res = ".", [], 0
    while entry!="":
        str = input("Escribe un número. Para salir aprieta enter: ")
        if str=="": break
        num = int(str)
        lista.append(num)
        res += num
    print(res, lista)

#Escribir una funcion que reciba el nombre y el apellido y lños vaya agregando a un archivo
def name_in_file():
    nombre = input("Escribe tu nombre: ")
    apellido = input("Escribe tu apellido: ")
    f = open("Python/Ejercicios/file.txt", "a", encoding="utf8")
    f.write(str(apellido) + "; " + str(nombre) + "\n")
    f.close()

suma_de_lista_dinamica()