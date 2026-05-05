frase = ""

while True:
    palabra = input("Ingrese una palabra:  ")
    if palabra == ".":
        break
    else:
        frase += palabra + " "
print(f"La frase es: {frase}")