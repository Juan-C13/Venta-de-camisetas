nombre=input("Digite su nombre:")
a=0
while a==0:
    edad=int(input("Digite su edad:"))
    if edad>0 and edad<18:
        valorC=30000
        tipo="Juvenil"
        a+=1
    elif edad>=18 and edad<=100:
        valorC=45000
        tipo="Adulto"
        a+=1
    else:
        print("Esa edad no es válida")
        print("")
cantidad=int(input("Digite la cantidad de camisetas a comprar:"))
total=valorC*cantidad
print("")
print("NOMBRE:",nombre)
print("TIPO CAMISETA:",tipo)
print("TOTAL A PAGAR:",total)
