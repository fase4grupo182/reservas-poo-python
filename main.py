#main.py 

from cliente import Cliente
from servicio import ReservaSala
from servicio import AlquilerEquipo
from servicio import AsesoriaEspecializada
from reserva import Reserva

from logger import Logger

from excepciones import ErrorReserva
from excepciones import ErrorCliente
from excepciones import ErrorServicio


logger = Logger()

print('\n --- SISTEMA SOFTWARE FJ ---\n')


# OPERACION 1
logger.operacion(1, 'Creación de cliente')

try:

    cliente1 = Cliente('Jose', '123')

    print(cliente1.mostrar_info())

    logger.info('Cliente creado correctamente')

except Exception as error:

    logger.error('Error al crear cliente', error)


# OPERACION 2
logger.operacion(2, 'Reserva de sala')

try:

    servicio1 = ReservaSala(2)

    print(servicio1.descripcion())

    print("Costo:", servicio1.calcular_costo())

    logger.info('Servicio ReservaSala creado')

except Exception as error:

    logger.error('Error en ReservaSala', error)


# OPERACION 3
logger.operacion(3, 'Alquiler de equipo')

try:

    servicio2 = AlquilerEquipo(3)

    print(servicio2.descripcion())

    print("Costo:", servicio2.calcular_costo())

    logger.info('Servicio AlquilerEquipo creado')

except Exception as error:

    logger.error('Error en AlquilerEquipo', error)


# OPERACION 4
logger.operacion(4, 'Asesoría especializada')

try:

    servicio3 = AsesoriaEspecializada(1)

    print(servicio3.descripcion())

    print("Costo:", servicio3.calcular_costo())

    logger.info('Servicio AsesoriaEspecializada creado')

except Exception as error:

    logger.error('Error en asesoría', error)


# OPERACION 5
logger.operacion(5, 'Creación de reserva')

try:

    reserva1 = Reserva(cliente1, servicio1)

    print(reserva1.mostrar_reserva())

    logger.info('Reserva creada correctamente')

except Exception as error:

    logger.error('Error al crear reserva', error)


# OPERACION 6
logger.operacion(6, 'Confirmar reserva')

try:

    reserva1.confirmar()

    print("Estado actual:", reserva1.estado)

    logger.info('Reserva confirmada')

except Exception as error:

    logger.error('Error al confirmar reserva', error)


# OPERACION 7
logger.operacion(7, 'Calcular costo total')

try:

    print("Costo total:", reserva1.calcular_total())

    logger.info('Costo calculado correctamente')

except Exception as error:

    logger.error('Error al calcular costo', error)


# OPERACION 8
logger.operacion(8, 'Cancelar reserva')

try:

    reserva1.cancelar()

    print("Nuevo estado:", reserva1.estado)

    logger.info('Reserva cancelada')

except Exception as error:

    logger.error('Error al cancelar reserva', error)


# OPERACION 9
logger.operacion(9, 'Crear segundo cliente')

try:

    cliente2 = Cliente('Carlos', '345')

    print(cliente2.mostrar_info())

    logger.info('Segundo cliente creado')

except Exception as error:

    logger.error('Error al crear segundo cliente', error)


# OPERACION 10
logger.operacion(10, 'Segunda reserva')

try:

    reserva2 = Reserva(cliente2, servicio2)

    print(reserva2.mostrar_reserva())

    logger.info('Segunda reserva creada')

except Exception as error:

    logger.error('Error en segunda reserva', error)


# OPERACION 11
logger.operacion(11, 'Cliente con datos invalidos')
try : 
    cliente_error = Cliente('','')
    print(cliente_error.mostrar_info())

except Exception as error:
    logger.error('Error al crear cliente con datos invalidos', error)
    print('Se detecto un error controlado')

# OPERACION 12
logger.operacion(12, 'Reserva con datos invalidos')
try:
    reserva_error = Reserva(None, servicio1)
    print(reserva_error.mostrar_reserva())
except Exception as error:
    logger.error('Error al crear reserva con datos invalidos', error)
    print('Reserva invalida detectada')