from cliente import Cliente
from servicio import ReservaSala
from reserva import Reserva


cliente1 = Cliente("Jose", "123")

servicio1 = ReservaSala(2)

reserva1 = Reserva(cliente1, servicio1)


print(reserva1.mostrar_reserva())

print("Costo total:", reserva1.calcular_total())


reserva1.confirmar()

print("Estado actual:", reserva1.estado)