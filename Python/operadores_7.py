# Tienda de libros
# Mostrar: Ingrese los siguientes datos del libro
# Digite el nombre del libro
# Digite el ID del libro
# Digite el precio del libro
# Indicar si el envío es gratuito (True/False)
# Mostrar:
# 	Nombre:
# 	ID: 
# 	Precio:
# 	Envío Gratuito?:

print('Ingrese los siguientes datos del libro')

nombre = input("Digite el nombre del libro: ");
id = input("Digite el ID del libro: ");
precio = input("Digite el precio del libro: ");
envioGratis = input("Indicar si el envío es gratuito (True/False): ");

if (envioGratis == 'True'):
    envioGratis = 'Si'
elif(envioGratis == 'False'):
    envioGratis = 'No'
envioGratis = 'El formato es inválido, ingrese True/False'

print(f'''
Nombre: {nombre} 
ID: {id} 
Precio: {precio} 
Envio Gratuito?: {envioGratis}
''')