frase = input("Ingrese una frase : ")
caracter = input("Ingrese un caracter : ")

cantidad = frase.count(caracter)

if len(caracter) == 1:
    print("En la frase", frase, " aparece", cantidad, "veces el caracter", caracter)
else:
    print("Ingrese solo un caracter.")