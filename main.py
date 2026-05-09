from cliente import Cliente
from servicio import ReservaSala
from servicio import AlquilerEquipo
from servicio import AsesoriaEspecializada
from reserva import Reserva

print('\n ---Sistema SOFTWARE FJ ---\n')

#Operacion1
cliente1 = Cliente("Jose", "123")
print(cliente1.mostrar_info())

#Operacion 2
servicio1 = ReservaSala(2)
print(servicio1.descripcion())
print("Costo:", servicio1.calcular_costo())

#Operacion 3
Servicio2 = AlquilerEquipo(3)
print(Servicio2.descripcion())
print("Costo:", Servicio2.calcular_costo())

#Operacion 4
Servicio3 = AsesoriaEspecializada(1)
print(Servicio3.descripcion())
print("Costo:", Servicio3.calcular_costo())

#Operacion 5
reserva1 = Reserva(cliente1, servicio1)
print(reserva1.mostrar_reserva())

#Operacion 6
reserva1.confirmar()
print('Estado actual:', reserva1.estado)

#Operacion 7
print('Costo total:', reserva1.calcular_total())

#Operacion8
reserva1.cancelar()
print('Nuevo estado:', reserva1.estado)

#Operacion 9
cliente2 = Cliente('Carlos', '345')
print(cliente2.mostrar_info())

#Operacion 10
reserva2 = Reserva(cliente2, Servicio2)
print(reserva2.mostrar_reserva())
