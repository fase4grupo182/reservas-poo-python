# reserva.py

class Reserva:

    def __init__(self, cliente, servicio):

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "pendiente"

    def confirmar(self):

        self.estado = "confirmada"

    def cancelar(self):

        self.estado = "cancelada"

    def calcular_total(self):

        return self.servicio.calcular_costo()

    def mostrar_reserva(self):

        return (
            f"Cliente: {self.cliente.get_nombre()} | "
            f"Servicio: {self.servicio.descripcion()} | "
            f"Estado: {self.estado}"
        )