
while True:
    y = float(input("Ingrese un valor para Y : "))

    if y == 0:
        print("Programa terminado")
        break
    resultado = y ** 3 + 7
    print(f"para y = {y}, f(X) = {resultado}")