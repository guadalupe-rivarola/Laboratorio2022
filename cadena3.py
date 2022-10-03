telePrecioPalabra=500
teleTotal=0
cd_p=900
cd_ph=50
cd_total=0
telegrama=0
cc_precio=0
print("   ESCOJA UNO DE LOS PRODUCTOS DEL MENÚ")
print(" ")
print("   1 - CARTA CERTIFICADA")
print("   2 - TELEGRAMA")
print("   3 - CARTA DOCUMENTO")
print("   4 - TELEGRAMA DE RENUNCIA")
print(" ")
x=int(input("INGRESE LA ID DE UNO DE LOS PRODUCTOS OFRECIDOS: "))

if x == 1:
    cc_peso=int(input("Ingrese peso de la carta certificada en gramoS (recuerde que debe ser menor a los dos kilos): "))
    if cc_peso <= 20:
        cc_precio=1170
        print("El precio de la carta certificada es de $1170")
    elif cc_peso <= 150:
        cc_precio=1600
        print("El precio de la carta certificada es de $1600")
    elif cc_peso <= 250:
        cc_precio=1820
        print("El precio de la carta certificada es de $1820")
    elif cc_peso <= 500:
        cc_precio=2430
        print("El precio de la carta certificada es de $2430")
    elif cc_peso <= 1000:
        cc_precio=3710
        print("El precio de la carta certificada es de $3710")
    elif cc_peso <= 1500:
        cc_precio=4880
        print("El precio de la carta certificada es de $4880")
    elif cc_peso <= 2000:
        cc_precio=6010
        print("El precio de la carta certificada es de $6010")
    else:
        while 1 == 1:
            print("El peso de la carta certificada ha sido traspasado")

elif x == 2:
    telegrama=input("Ingrese el telegrama:")
    telegrama=telegrama.strip()
    print("El telegrama tiene", telegrama.count(" ")+1, "palabras, el precio es de:", (telegrama.count(" ")+1)*telePrecioPalabra)

elif x == 3:
    cd_ch=int(input("ingresar la cantidad de hojas de su carta documento: "))
    cd_total = cd_ch * cd_ph + cd_p
    print("El valor total de la carta documento es", cd_total)

elif x == 4:
    print("El telegrama de renuncia es gratis")
    telegramarenuncia=input("Ingrese el telegrama de renuncia: ")

else:
    while 1 == 1:
            print("ID no valido")
