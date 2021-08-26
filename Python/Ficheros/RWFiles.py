import time
import os

#Lee un archivo el cual podemos usar como String

def leer(nombre):
    f = open(nombre, "r", encoding="utf8")
    texto = f.read()
    imp_log("leer el fichero '" + nombre + "'.", "")
    texto2 = texto.split("\n")
    print(texto, "\n")
    print(texto2)
    f.close()

#Añade una línea al final del archivo
def append(nombre):
    f = open(nombre, "a", encoding="utf8")
    msg = input("Introduce una frase para apuntar en 'texto.txt': ")
    f.write("\n" + msg)
    imp_log("escribir en el fichero '" + nombre + "'.", msg.strip())
    f.close()

#Escribir sobreescribe el contenido (A no ser que la funcion que yo cree lo impida)
def escr(nombre):
    f = open(nombre, "w", encoding="utf8")
    f.write()
    f.close()

#<---- Imprime en "log.txt" lo ocurrido ---->#
def imp_log(msg, esc):
    log = open("Python/Ficheros/log.txt", "a", encoding="utf8")
    log.write("\n" + time.strftime('%H:%M:%S   %A - %d/%b/%Y') + " [ACTION]-> Se intentó " + msg)
    if esc != "": log.write("\n\t [MSG]Mensaje que se intentó escribir -> '" + esc + "'\n")
    log.close()

def crear_archivo(nombre):
    f = open("temp", "w", encoding="utf8")
    if os.path.exists(nombre):
        imp_log("Ya existe un archivo con este nombre...", "")
    else:
        f = open(nombre, "w", encoding="utf8")
    imp_log("Se intentó crear una archivo con el nombre " + nombre, "")
    borrar_archivo("temp")
    f.close()

def borrar_archivo(nombre):
    os.remove(nombre) if os.path.exists(nombre) else imp_log("No existe este archivo...", "")
    imp_log("Se intentó eliminar la archivo con el nombre " + nombre, "")

append('Python/Ficheros/texto.txt')
leer('Python/Ficheros/texto.txt')
crear_archivo("Python/Ficheros/Hola mundo1.txt")
crear_archivo("Python/Ficheros/Hola mundo2.txt")
borrar_archivo("Python/Ficheros/Hola mundo2.txt")