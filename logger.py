# logger.py

import os
import traceback
from datetime import datetime
from enum import Enum


class NivelLog(Enum):
    INFO = "INFO"
    ADVERTENCIA = "ADVERTENCIA"
    ERROR = "ERROR"
    CRITICO = "CRITICO"


class Logger:
    """
    Gestor centralizado de logs.
    Registra eventos en consola y en archivo de texto plano.
    """

    _instancia = None  

    def __new__(cls, ruta_archivo: str = "logs_sistema_fj.txt"):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializar(ruta_archivo)
        return cls._instancia

    def _inicializar(self, ruta_archivo: str):
        self.ruta_archivo = ruta_archivo
        self._escribir_separador("SISTEMA SOFTWARE FJ - INICIO DE SESIÓN")

    def _timestamp(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _escribir_separador(self, titulo: str = ""):
        linea = "=" * 70
        with open(self.ruta_archivo, "a", encoding="utf-8") as f:
            f.write(f"\n{linea}\n")
            if titulo:
                f.write(f"  {titulo} — {self._timestamp()}\n")
                f.write(f"{linea}\n")

    def _registrar(self, nivel: NivelLog, mensaje: str, detalle: str = ""):
        timestamp = self._timestamp()
        entrada = f"[{timestamp}] [{nivel.value:12}] {mensaje}"
        if detalle:
            entrada += f"\n{'':>35}DETALLE: {detalle}"
        entrada += "\n"

        # Escribir en archivo
        with open(self.ruta_archivo, "a", encoding="utf-8") as f:
            f.write(entrada)

        # Mostrar en consola con colores ANSI
        colores = {
            NivelLog.INFO: "\033[96m",       # Cyan
            NivelLog.ADVERTENCIA: "\033[93m", # Amarillo
            NivelLog.ERROR: "\033[91m",       # Rojo
            NivelLog.CRITICO: "\033[95m",     # Magenta
        }
        reset = "\033[0m"
        print(f"{colores[nivel]}{entrada.strip()}{reset}")

    def info(self, mensaje: str, detalle: str = ""):
        self._registrar(NivelLog.INFO, mensaje, detalle)

    def advertencia(self, mensaje: str, detalle: str = ""):
        self._registrar(NivelLog.ADVERTENCIA, mensaje, detalle)

    def error(self, mensaje: str, excepcion: Exception = None):
        detalle = ""
        if excepcion:
            detalle = f"{type(excepcion).__name__}: {excepcion}"
        self._registrar(NivelLog.ERROR, mensaje, detalle)

    def critico(self, mensaje: str, excepcion: Exception = None):
        detalle = ""
        if excepcion:
            detalle = traceback.format_exc()
        self._registrar(NivelLog.CRITICO, mensaje, detalle)

    def operacion(self, numero: int, descripcion: str):
        """Registra el inicio de una operación numerada."""
        with open(self.ruta_archivo, "a", encoding="utf-8") as f:
            f.write(f"\n{'─'*70}\n")
            f.write(f"  OPERACIÓN #{numero:02d}: {descripcion}\n")
            f.write(f"{'─'*70}\n")
        print(f"\n\033[1m\033[94m{'─'*70}\033[0m")
        print(f"\033[1m\033[94m  OPERACIÓN #{numero:02d}: {descripcion}\033[0m")
        print(f"\033[1m\033[94m{'─'*70}\033[0m")
