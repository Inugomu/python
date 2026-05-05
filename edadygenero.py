cantidad = int(input("¿Cuantas personas va a contabilizar?"))

menores = 0
mayores = 0
masculino = 0
femenino = 0


for i in range(cantidad):
    print(f"personas {i+1}")

    edad =int(input("Edad: "))
    genero =input("Género (M/F): ").upper()

    if edad < 18:
        menores +=1
    elif edad >= 18 :
        mayores +=1
    if genero == "M":
        masculino +=1
    elif genero == "F":
        femenino +=1

print()
print("***RESULTADOS***")
print("Menores de edad: ", menores)
print("Mayores de edad: ", mayores)
print("Masculinos: ", masculino)
print("Femeninos: ", femenino)
