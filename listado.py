lista={}
stop=0
archi1 = open("listado.txt", "w+")
fecha=input("Ingrese fecha: ")
curso=input("Ingrese el curso: ")

while stop == 0:
    alumno=input("Ingrese apellido y nombre del alumno: ")
    pre=input("Si el alumno se encuntra en el establecimiento ingrese sí sino ingrese no: ")
    if pre== "no":
        lista[alumno]="A"
    else:
        hora= float(input("Ingrese horario de entrada: "))
        if hora > 07.00 and hora < 08.15:
            lista[alumno]="P"
        else:
            lista[alumno]="T"
    seguir = input("Ingrese s para agregar otro alumno sino ingrese n: ")
    if seguir == "n":
        stop = 1
            
archi1.write(fecha)
archi1.write("\n")
archi1.write(curso)
archi1.write("\n")
archi1.write(str(lista))
archi1.write("\n")









    
archi1.close()
