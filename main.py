from servicio import ReservaSala
from servicio import AlquilerEquipo
from servicio import AsesoriaEspecializada


sala = ReservaSala(2)

equipo = AlquilerEquipo(3)

asesoria = AsesoriaEspecializada(1)


print(sala.descripcion())
print(sala.calcular_costo())

print(equipo.descripcion())
print(equipo.calcular_costo())

print(asesoria.descripcion())
print(asesoria.calcular_costo())
