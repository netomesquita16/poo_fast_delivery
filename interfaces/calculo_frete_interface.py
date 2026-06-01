#Define a obrigatoriedade do método calcular_frete.

from abc import ABC, abstractmethod

class CalculoFreteInterface(ABC):
    @abstractmethod
    def calcular_frete(self, distancia: float) -> float:
        pass