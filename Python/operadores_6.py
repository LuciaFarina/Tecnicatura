# El mayor de dos números
# Solicitar al usuario dos valores, determinar cual es el mayor.
# Solicitar al usuario dos valores
# 	numero1 (int)
# 	numero2 (int)
# Se debe imprimir el mayor de los dos números (La salida debe ser identica a la siguiente):
# 	Digite el valor para el numero1:
# 	Digite el valor para el numero2:
# 	El número mayor es:   <numeroMayor>


num1 = int(input("Digite el valor para el numero1: "));
num2 = int(input("Digite el valor para el numero2: "));

if (num1 > num2):
    print('El número mayor es:', num1)
elif (num2> num1):
    print('El número mayor es:', num2)
else: 
    print('Los números son iguales')
