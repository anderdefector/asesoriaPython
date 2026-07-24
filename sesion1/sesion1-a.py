# =====================================================================
# CLASE: VARIABLES Y TIPOS DE DATOS EN PYTHON
# =====================================================================

# 1. ¿Qué es una variable? 
# Imagínala como una caja con una etiqueta donde guardamos información.
print("--- 1. VARIABLES ---")

nombre_alumno = "Carlos"  # Creamos la variable y le asignamos un valor
edad = 20

print("El alumno se llama:", nombre_alumno)
print("Su edad es:", edad)

# Las variables pueden cambiar de valor a lo largo del programa
edad = 21 
print("Un año después, su edad es:", edad)
print("\n" + "-"*40 + "\n")


# 2. Tipos de Datos Primitivos
print("--- 2. TIPOS DE DATOS ---")

# Texto (String / Str) - Siempre van entre comillas
ciudad = "Ciudad de México"

# Números Enteros (Integer / Int) - Sin decimales
articulos_comprados = 5

# Números Decimales (Float) - Usan punto, no coma
precio_total = 299.99

# Booleans (Bool) - Solo pueden ser True (Verdadero) o False (Falso)
tiene_descuento = True

# Mostramos los valores en pantalla
print("Ciudad:", ciudad)
print("Artículos:", articulos_comprados)
print("Precio:", precio_total)
print("¿Tiene descuento?:", tiene_descuento)
print("\n" + "-"*40 + "\n")


# 3. ¿Cómo saber qué tipo de dato tiene una variable?
# Usamos la función nativa type()
print("--- 3. FUNCIÓN TYPE() ---")

print("El tipo de 'ciudad' es:", type(ciudad))
print("El tipo de 'articulos_comprados' es:", type(articulos_comprados))
print("El tipo de 'precio_total' es:", type(precio_total))
print("El tipo de 'tiene_descuento' es:", type(tiene_descuento))
print("\n" + "-"*40 + "\n")
    

# 4. Dinamismo en Python (Tipado Dinámico)
# A diferencia de otros lenguajes, en Python una variable puede cambiar de tipo libremente.
print("--- 4. TIPADO DINÁMICO ---")

caja_sorpresa = "Ahora soy un texto"
print("Valor:", caja_sorpresa, "| Tipo:", type(caja_sorpresa))

caja_sorpresa = 42
print("Valor:", caja_sorpresa, "      | Tipo:", type(caja_sorpresa))
print("\n" + "-"*40 + "\n")


# 5. Pequeño Reto / Ejercicio para los alumnos
# Regla de oro: No se pueden sumar textos con números directamente sin convertir.
print("--- 5. EJERCICIO PRÁCTICO: CONVERSIÓN ---")

edad_texto = "25"  # Es un String porque tiene comillas
# edad_futura = edad_texto + 5  <-- ¡Esto daría un error (TypeError)!

# Solución: Convertir el texto a entero usando int()
edad_entero = int(edad_texto)
edad_futura = edad_entero + 5

print("Edad original (texto):", edad_texto)
print("Edad sumada en 5 años (entero):", edad_futura)
