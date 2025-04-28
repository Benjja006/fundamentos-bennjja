estudiante = True  # Aunque estas variables se definen, luego se reasignan con la entrada del usuario
frecuente = True
ctarut = True
descuentoest_valor = 15  # Es mejor tener los valores de descuento en variables separadas
descuentoclf_valor = 10
descuentoctarut_valor = 20

print("Ingrese el precio del producto")
preciooriginal = float(input())

es_estudiante = input("¿Es estudiante? S/N ")  # Usamos una variable más descriptiva
desc_aplicado = 0  # Inicializamos el descuento aplicado

if es_estudiante.lower() == "s":  # Convertimos la entrada a minúscula para comparar fácilmente
    desc_aplicado = (preciooriginal * descuentoest_valor / 100)
    print(f"Se aplicó un descuento de estudiante del {descuentoest_valor}%.")
preciofinal = preciooriginal - desc_aplicado
print(f"El precio original era: ${preciooriginal:.2f}")
print(f"El descuento aplicado es: ${desc_aplicado:.2f}")
print(f"El precio final es: ${preciofinal:.2f}")