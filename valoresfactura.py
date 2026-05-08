valorconocido = input("¿Cual valor de su factura conoce?(neto, iva o total):  ").upper()

if valorconocido == "NETO":
    valorneto = float(input("Ingrese el valor neto de su factura: "))
    print(f"""
    El valor neto es: {valorneto}
    El valor iva es: {valorneto * 0.19}
    El valor total es: {valorneto * 1.19}

    """)
elif valorconocido == "IVA":
    iva = float(input("Ingrese el valor iva de su factura:  "))
    print(f"""
    El valor neto es: {iva / 0.19}
    El valor iva es: {iva}
    El valor total es: {(iva / 0.19) + iva}
    """)
elif valorconocido == "TOTAL":
    total = float(input("Ingrese el valor total de su factura: "))
    print(f""" 
    El valor neto es : {total / 1.19}
    EL valor iva es: {(total / 1.19) * 0.19}
    El valor total es: {total}
    """)
else:
    print("Por favor ingrese \"NETO\", \"IVA\" O \"TOTAL\"")
    