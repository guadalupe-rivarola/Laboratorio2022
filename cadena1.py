archi1=open("cadena1.txt","w+")
nombre=input("Ingrese el nombre: ")
archi1.write("Nombre: ")
archi1.write(nombre)
archi1.write(" \n")
dni=input("Ingrese DNI: ")
archi1.write("DNI: ")
archi1.write(dni)
archi1.write(" \n")
usuario= nombre[:3] + dni[5:]
archi1.write("Usuario: ")
archi1.write(usuario)
archi1.write(" \n")
archi1.close()
