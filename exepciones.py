# excepciones.py
# Aquí se definen excepciones personalizadas.
# Estas clases permiten manejar errores específicos del sistema.
# Ejemplos:
# - ErrorCliente
# - ErrorServicio
# - ErrorReserva
# Todas deben heredar de Exception.
class ErrorSistemaFJ(Exception):
    def __init__(self, mensaje: str, codigo: str = "ERR-000"):
        super().__init__(f"[{codigo}] {mensaje}")


class ErrorCliente(ErrorSistemaFJ):
    """Errores relacionados con la gestión de clientes."""
    def __init__(self, mensaje: str):
        super().__init__(mensaje, "ERR-CLI")


class ErrorClienteDuplicado(ErrorCliente):
    """Cliente ya registrado en el sistema."""
    def __init__(self, identificacion: str):
        super().__init__(f"El cliente con identificación '{identificacion}' ya existe en el sistema.")
        self.identificacion = identificacion


class ErrorClienteNoEncontrado(ErrorCliente):
    """Cliente no existe en el sistema."""
    def __init__(self, identificacion: str):
        super().__init__(f"No se encontró ningún cliente con identificación '{identificacion}'.")
        self.identificacion = identificacion


class ErrorDatosInvalidos(ErrorSistemaFJ):
    """Datos ingresados no cumplen con el formato o restricciones requeridas."""
    def __init__(self, campo: str, motivo: str):
        super().__init__(f"Dato inválido en campo '{campo}': {motivo}", "ERR-DAT")
        self.campo = campo
        self.motivo = motivo


class ErrorServicio(ErrorSistemaFJ):
    """Errores relacionados con los servicios."""
    def __init__(self, mensaje: str):
        super().__init__(mensaje, "ERR-SRV")


class ErrorServicioNoDisponible(ErrorServicio):
    """Servicio no está disponible para reserva."""
    def __init__(self, nombre_servicio: str):
        super().__init__(f"El servicio '{nombre_servicio}' no está disponible en este momento.")
        self.nombre_servicio = nombre_servicio


class ErrorServicioNoEncontrado(ErrorServicio):
    """Servicio no existe en el catálogo."""
    def __init__(self, id_servicio: str):
        super().__init__(f"No se encontró el servicio con ID '{id_servicio}'.")
        self.id_servicio = id_servicio


class ErrorCapacidadExcedida(ErrorServicio):
    """La capacidad del servicio ha sido superada."""
    def __init__(self, nombre_servicio: str, capacidad_max: int):
        super().__init__(
            f"La capacidad máxima del servicio '{nombre_servicio}' es {capacidad_max} personas."
        )


class ErrorReserva(ErrorSistemaFJ):
    """Errores relacionados con las reservas."""
    def __init__(self, mensaje: str):
        super().__init__(mensaje, "ERR-RES")


class ErrorReservaNoEncontrada(ErrorReserva):
    """Reserva no existe en el sistema."""
    def __init__(self, id_reserva: str):
        super().__init__(f"No se encontró la reserva con ID '{id_reserva}'.")
        self.id_reserva = id_reserva


class ErrorEstadoInvalido(ErrorReserva):
    """Operación no permitida dado el estado actual de la reserva."""
    def __init__(self, operacion: str, estado_actual: str):
        super().__init__(
            f"No se puede ejecutar '{operacion}' sobre una reserva en estado '{estado_actual}'."
        )


class ErrorDuracionInvalida(ErrorReserva):
    """Duración fuera del rango permitido para el servicio."""
    def __init__(self, min_h: float, max_h: float, solicitado: float):
        super().__init__(
            f"Duración {solicitado}h fuera del rango permitido ({min_h}h – {max_h}h)."
        )


class ErrorCalculo(ErrorSistemaFJ):
    """Error durante el cálculo de costos u otros valores numéricos."""
    def __init__(self, mensaje: str):
        super().__init__(mensaje, "ERR-CALC")
