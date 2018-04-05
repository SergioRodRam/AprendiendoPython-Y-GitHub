#! /usr/bin/env python

###############     ENTEROS
#Se coloca una variable de tipo "int"
entero = 23

#Se comprueba que sea un entero, devolveria int
print(type(entero))
print("El numero que tiene el entero es: "+ str(entero))

#Se fuerza a que una variable sea "long"
entero = 23L

#Se comprueba que sea un "long", devolveria long
print(type(entero))
print("El numero que tiene el entero es: "+ str(entero))

#En octal seria anteponer un "0"
#027 en octal = 23 en base 10
entero = 027

print("El numero que tiene el entero es: "+ str(entero))

#En hexadecimal se antepone un "0x"
#0x17 en hexadecimal = 23 en base 10
entero = 0x17

print("El numero que tiene el entero es: "+ str(entero))

###############     REALES
#Este es un numero real "float"
real = 0.2703

print("Mi numero real vale: "+ str(real))

#Se crea una variable que expresa un exponente en base 10
real = 0.1e-3

print("Mi numero en base 10 es: "+ str(real))

###############     COMPLEJOS
#Este es un numero complejo
complejo = 2.1 + 7.8j

print("Mi numero complejo es: "+ str(complejo))