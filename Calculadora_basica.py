'''Contruir un programa que simule el funcionamiento de una calculadora que
pueda realizar las 4 operaciones aritmeticas basicas (+, -, *, /). El usuario
debe especificar la operacion con el primer caracter del nombre de la
operacion'''

print('CALCULADORA\n')

num1 = float(input('Digite el primer numero: '))
num2 = float(input('Digite el segundo numero: '))

print('\n-Por favor elige la operacion que deseas realizar-\n')
operacion = input('Digita "S" para suma, "R" para resta, "P" o "M" para multiplicacion, o "D" para division: ').upper()

if operacion=='S':
       result_suma = num1+num2
       print(f'\nEl resultado de la suma es: {result_suma}')

elif operacion=='R':
       result_rest = num1-num2
       print(f'\nEl resultado de la resta es: {result_rest}')  

elif operacion=='P' or operacion=='M':
       result_multi = num1*num2
       print(f'\nEl resultado de la multiplicacion es: {result_multi}')       

elif operacion=='D':
       result_div = num1/num2
       print(f'\nEl resultado de la division es: {result_div}') 

else:
       print('\nInformacion invalida')

#La funcion ".upper()" ayuda a que el sistema reconozca letras que en el
#statement se pusieron mayuscula pero el usuario las digita minuscula.
#Asi se evita programar todas las exceptiones de mayuscula/minuscula.

