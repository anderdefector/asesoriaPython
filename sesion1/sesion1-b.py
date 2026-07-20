# =====================================================================
# CONTINUACIÓN: OPERADORES Y VARIABLES BOOLEANAS
# =====================================================================

print("--- 6. OPERADORES ARITMÉTICOS ---")
# Sirven para realizar operaciones matemáticas básicas
a = 15
b = 4

suma = a + b          # 19
resta = a - b         # 11
multiplicacion = a * b # 60
division = a / b       # 3.75 (Siempre devuelve un Float)
division_entera = a // b # 3 (Descarta los decimales)
residuo = a % b        # 3 (El sobrante de la división, útil para saber si un número es par)
potencia = a ** 2      # 225 (15 elevado al cuadrado)

print(f"Suma: {a} + {b} = {suma}")
print(f"División exacta: {a} / {b} = {division}")
print(f"División entera: {a} // {b} = {division_entera}")
print(f"Residuo (Módulo): {a} % {b} = {residuo}")
print("\n" + "-"*40 + "\n")


print("--- 7. OPERADORES DE COMPARACIÓN -> RESULTAN EN BOOLEANOS ---")
# Estos operadores comparan dos valores y SIEMPRE devuelven True o False (un tipo bool)
mi_edad = 20
edad_minima = 18

# Guardamos el resultado directo de la comparación en variables booleanas
es_mayor_de_edad = mi_edad >= edad_minima  # Mayor o igual
puede_votar = mi_edad == 18                # Igualdad exacta (Ojo: doble signo ==)
es_diferente = mi_edad != 30               # Diferente de

print("¿Es mayor de edad?:", es_mayor_de_edad)  # True
print("¿Tiene exactamente 18?:", puede_votar)  # False
print("¿Su edad es diferente de 30?:", es_diferente)  # True
print("El tipo de dato de estas respuestas es:", type(es_mayor_de_edad))
print("\n" + "-"*40 + "\n")


print("--- 8. OPERADORES LÓGICOS (AND, OR, NOT) ---")
# Sirven para combinar múltiples condiciones booleanas

tiene_boleto = True
tiene_identificacion = False
es_invitado_vip = True

# AND: Da True SÓLO si AMBAS condiciones son verdaderas
entra_por_puerta_general = tiene_boleto and tiene_identificacion
print("¿Entra por puerta general? (boleto Y id):", entra_por_puerta_general) # False

# OR: Da True si AL MENOS UNA de las condiciones es verdadera
entra_al_evento = entra_por_puerta_general or es_invitado_vip
print("¿Entra al evento? (general O vip):", entra_al_evento) # True

# NOT: Invierte el valor booleano
esta_lloviendo = False
print("¿El clima está despejado? (not lloviendo):", not esta_lloviendo) # True
