archi1=open("cadena2.txt", "w+")
palabra=input("Ingrese una palabra: ")
archi1.write('**' + '*' * len(palabra))
archi1.write(" \n")
archi1.write("*"+ palabra +"*")
archi1.write(" \n")
archi1.write('**' + '*' * len(palabra))
archi1.write(" \n")
archi1.close()
