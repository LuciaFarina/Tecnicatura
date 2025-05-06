# Valor dentro de un rango

# Pedimos al usuario un valor numérico
# Verificar si el valor ingresado se encuentra entre el rango de 0 a 5
# La formula es: <num> >= 0  and  <num> <= 5

num = int(input("Ingrese un número: "));

rangoMin = 0;
rangoMax = 5;

if (num >=0 and num <=5):
    print(f'El número {num} esta dentro del rango')
else:
    print(f'El número {num} esta fuera del rango')
