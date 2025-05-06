# La pregunta es si un padre puede asistir al juego de su hijo.
# Verificamos si tiene vacaciones
# Verificamos si tiene el día libre
# Usar estructura ‘if else’ con el operador or
# Imprimir

vacaciones = True;
diaLibre = True;

if not (vacaciones or diaLibre):
    print('Trabaja, no puede asistir al juego')
else: 
    print('Si puede asistir al juego')