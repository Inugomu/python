num1 = int(input("Ingrese un número entero y positivo: "))
num2 = int(input("Ingrese un número entero, positivo y menor que el anterior: "))

if num1 > num2 and num1 > 0 and num2 > 0:
    for i in range (num1, num2 -1, -1):
        print(i)
else:
    print("Los números ingresados no son validos.")