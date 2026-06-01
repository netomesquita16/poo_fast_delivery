#A superclasse abstrata que contém o encapsulamento básico exigido.

from abc import ABC

class Pessoa(ABC):
    def __init__(self, nome: str):
        self.__nome = nome  # Atributo privado

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        self.__nome = novo_nome