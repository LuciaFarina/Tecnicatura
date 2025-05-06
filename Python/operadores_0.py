# calcular el área y el perímetro de un rectángulo. Para ello debemos de crear las siguientes variables:
# alto (int)
# ancho (int)
# El usuario debe de proporcionar los valores de alto y ancho, después se debe de imprimir el resultado en el siguiente formato:
# Proporciona el alto del rectángulo: 5
# Proporciona el ancho del rectángulo: 3
# Área: 15
# Perímetro: 16

# Las fórmulas para calcular el área y el perímetro de un rectángulo son: 
# Área: alto * ancho
# Perímetro: (alto + ancho) * 2

alto = int(input('Proporciona el alto del rectángulo en cm: '));
ancho = int(input('Proporciona el ancho del rectángulo en cm: '));

area = alto * ancho
perimetro = (alto + ancho) * 2

print('El área de tu rectángulo es:', area);
print('El perímetro de tu rectángulo es:', perimetro)

