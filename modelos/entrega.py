#Implementa a interface e o Polimorfismo, com as fórmulas exatas de cálculo.

from interfaces.calculo_frete_interface import CalculoFreteInterface

class EntregaComum(CalculoFreteInterface):
    def calcular_frete(self, distancia: float) -> float:
        return distancia * 1.5

class EntregaExpressa(CalculoFreteInterface):
    def calcular_frete(self, distancia: float) -> float:
        return distancia * 3.0

class EntregaPremium(CalculoFreteInterface):
    def calcular_frete(self, distancia: float) -> float:
        return (distancia * 5.0) + 20.0