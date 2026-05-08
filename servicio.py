# servicio.py

from abc import ABC, abstractmethod


# Clase abstracta
class Servicio(ABC):

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# Servicio 1
class ReservaSala(Servicio):

    def __init__(self, horas):

        self.horas = horas

    def calcular_costo(self):

        return self.horas * 50000

    def descripcion(self):

        return "Reserva de sala"


# Servicio 2
class AlquilerEquipo(Servicio):

    def __init__(self, dias):

        self.dias = dias

    def calcular_costo(self):

        return self.dias * 30000

    def descripcion(self):

        return "Alquiler de equipo"


# Servicio 3
class AsesoriaEspecializada(Servicio):

    def __init__(self, sesiones):

        self.sesiones = sesiones

    def calcular_costo(self):

        return self.sesiones * 80000

    def descripcion(self):

        return "Asesoría especializada"