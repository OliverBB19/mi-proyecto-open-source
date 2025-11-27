#!/usr/bin/env python3
"""
Calculadora Científica Básica
Soporta: suma, resta, multiplicación, división, potencias,
raíz cuadrada, seno, coseno, tangente, logaritmo, etc.
"""

import math

def mostrar_menu():
    print("""
=== CALCULADORA CIENTÍFICA ===

Opciones disponibles:
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Potencia
6. Raíz cuadrada
7. Seno
8. Coseno
9. Tangente
10. Logaritmo (base 10)
11. Salir
""")

def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: introduce un número válido.")

def ejecutar_opcion(op):
    if op == "1":
        a = pedir_numero("Número 1: ")
        b = pedir_numero("Número 2: ")
        print("Resultado:", a + b)

    elif op == "2":
        a = pedir_numero("Número 1: ")
        b = pedir_numero("Número 2: ")
        print("Resultado:", a - b)

    elif op == "3":
        a = pedir_numero("Número 1: ")
        b = pedir_numero("Número 2: ")
        print("Resultado:", a * b)

    elif op == "4":
        a = pedir_numero("Número 1: ")
        b = pedir_numero("Número 2: ")
        if b == 0:
            print("Error: no se puede dividir entre 0.")
        else:
            print("Resultado:", a / b)

    elif op == "5":
        a = pedir_numero("Base: ")
        b = pedir_numero("Exponente: ")
        print("Resultado:", a ** b)

    elif op == "6":
        a = pedir_numero("Número: ")
        if a < 0:
            print("Error: no se puede obtener raíz de negativo.")
        else:
            print("Resultado:", math.sqrt(a))

    elif op == "7":
        a = pedir_numero("Ángulo en grados: ")
        print("Resultado:", math.sin(math.radians(a)))

    elif op == "8":
        a = pedir_numero("Ángulo en grados: ")
        print("Resultado:", math.cos(math.radians(a)))

    elif op == "9":
        a = pedir_numero("Ángulo en grados: ")
        print("Resultado:", math.tan(math.radians(a)))

    elif op == "10":
        a = pedir_numero("Número: ")
        if a <= 0:
            print("Error: el logaritmo solo aplica a números positivos.")
        else:
            print("Resultado:", math.log10(a))

    elif op == "11":
        print("Saliendo…")
        exit()

    else:
        print("Opción no válida.")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        ejecutar_opcion(opcion)
        input("\nPresiona ENTER para continuar...")


if __name__ == "__main__":
    main()
