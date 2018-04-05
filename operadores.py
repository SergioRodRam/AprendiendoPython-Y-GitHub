#! /usr/bin/env python

###############     OPERADORES ARITMETICOS     ###############
###############     ATRIBUTOS
numero1 = 10
numero2 = 12

###############     SUMA
suma = numero1 + numero2

print("La suma de "+ str(numero1)+ " + "+ str(numero2)+ " es: "+ str(suma))

###############     RESTA
resta = numero1 - numero2

print("La resta de "+ str(numero1)+ " - "+ str(numero2)+ " es: "+ str(resta))

###############     NEGACION
nNumero1 = -numero1

print("La negacion de "+ str(numero1)+ " es: "+ str(nNumero1))

###############     MULTIPLICACION
multiplicacion = numero1 * numero2

print("La multiplicacion de "+ str(numero1)+ " * "+ str(numero2)+ " es: "+ str(multiplicacion))

###############     EXPONENTE
exponente = numero1 ** numero2

print(str(numero1)+ " a la "+ str(numero2)+ " es: "+ str(exponente))

###############     DIVISION
#### NOTA
#### Para este caso al menos uno de los numeros debe de ser "float"
division = float(numero1) / numero2

print("La division de "+ str(numero1)+ " / "+ str(numero2)+ " es: "+ str(division))

###############     DIVISION ENTERA
dEntera = numero1 // numero2

print("La division entera de "+ str(numero1)+ " / "+ str(numero2)+ " es: "+ str(dEntera))

###############     MODULO
#### NOTA
#### El modulo solo regresa el residuo
modulo = numero2 % numero1

print(str(numero2)+ " % "+ str(numero1)+ " es: "+ str(modulo))