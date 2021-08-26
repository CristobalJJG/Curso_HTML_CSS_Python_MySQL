#print("Hola mundo")

#Es lo mismo#
x1 = "y=1"
x2 = "y=2"
x3 = "y=3"

y1, y2, y3 = "z=1", "z=2", "z=3"

#print(x1, x2, x3)
#print(y1, y2, y3)

#Concatenación#
inicio = "HOLA "
final = "MUNDO!"
#print(inicio + final)


#<-----Listas----->#
l1 = [3, 5, 2]
#print("Print:", l1)

l1.append(4)
#print("Append 4:", l1)

l2 = l1.copy()
#l1.clear()
#print("Clear:", l1)
#print("Copy l2:", l2)

i = 0
while i<10:
    l2.append(3)
    i+=1
#print(l2)
#print("¿Cuántos 3's tiene l2? Respuesta:",l2.count(3))
#print("¿Cuántos elementos tiene l2? Respuesta:", len(l2))

l1.append(13)
#print(l1)
#print("Eliminar el último elemento de la lista (pop): \n", l1)
l1.remove(2)
#print("Eliminar un número concreto (remove): \n", l1)
l1.reverse()
#print("Print reverse:\n", l1)
#print("Se pueden ordenar listas únicamente de String o únicamente de Enteros")
l1.sort()
#print("Lista ordenada: \n", l1)
#<-----Fin Listas----->#

#<-----Tuplas----->#
tupla = ("Hola", 13)
tup_a_list = list(tupla)
tup_a_list.append("Adiós")
#print(tupla, tup_a_list)
#<-----Fin Tuplas----->#

#<----Rangos---->#
rango = range(6)
#print(rango)
#<----Fin Rangos---->#

#<----Diccionarios Hashes---->#
dic = {
    "nombre":"Orion",
    "raza": "Naranjita",
    "gordo": True
}
#print(dic)

#print(dic["nombre"])
#print(dic.get("nombre"))
dic["nombre"] = "Orión"
#print(dic["nombre"])

dic["Hermana"] = True
#print(dic)

dic.pop("Hermana")
del dic["raza"]
#print(dic)

copiaDic = dic.copy()
copiaDic["raza"] = "Naranjita"
dic.clear()
#print(dic, copiaDic)


gatos = {
    "Orión":{
        "nombre":"Orión",
        "raza":"Gordo"
    },
    "Luna":{
        "nombre":"Luna",
        "raza":"Gorda"
    }
}
#print(gatos)

#Otra forma de hacerlo#
Orión = {
    "nombre":"Orión",
    "raza":"Gordo"
}
Luna = {
    "nombre":"Luna",
    "raza":"Gorda"
}
gatos2 = {
    "Orión": Orión,
    "Luna": Luna
}
#print(gatos2)

minina = dict(nombre="Minina", edad=5, raza="Gorda")
gordo = dict(nombre="Orion", edad=1, raza="Gordo")
gorda = dict(nombre="Luna", edad=0.7, raza="Gorda")
#print(minina)

gatos3 = dict(minina=minina, Orion=gordo, Luna=gorda)
#print(gatos3)
#<----Fin Diccionarios Hashes---->#

#booleanos raros (if cortos y ternarios, and y or)#
#if 2<5: print("if corto.")

    #Evalúa true y false en una sola línea(ternario)
#print("Cuando devuelte true") if 5<2 else print("Cuando devuelve false")

#No se muestra porque 1 es falsa
#if 2>5 and 5<6: print("Eh verdá 1")
#Se muestra porque 1 de las 2 es verdadera
#if 2>5 or 5<6: print("Eh verdá 2")

#FIN booleanos raros (if cortos y ternarios)#

#Prueba#
dato = input("Escribe un número: ")
try:
    d = int(dato)
except:
    print("Solo vale poner números...")
    exit(-13)

lista = [13, 1, 3, 10, 15, 5, 21]
print("Existe!", dato) if(lista.count(d))>0 else print("No existe", dato) 


#Funciones#
def diHola():
    print("Hola!")

diHola()