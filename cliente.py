# cliente.py

class Cliente:

    def __init__(self, nombre, documento):

        if nombre == "":
            raise ValueError("El nombre no puede estar vacío")

        if documento == "":
            raise ValueError("El documento no puede estar vacío")

        self.__nombre = nombre
        self.__documento = documento

    def mostrar_info(self):

        return f"Cliente: {self.__nombre} - Documento: {self.__documento}"

    def get_nombre(self):

        return self.__nombre

    def get_documento(self):

        return self.__documento