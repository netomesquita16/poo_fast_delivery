#Representa o pedido com seus status possíveis.

from modelos.cliente import Cliente
from interfaces.calculo_frete_interface import CalculoFreteInterface

class Pedido:
    def __init__(self, codigo: str, cliente: Cliente, peso: float, distancia: float, tipo_entrega: CalculoFreteInterface):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__peso = peso
        self.__distancia = distancia
        self.__tipo_entrega = tipo_entrega
        self.__status = "Em preparação" # Status inicial
        self.__valor_frete = self.__tipo_entrega.calcular_frete(distancia)

    @property
    def codigo(self): return self.__codigo
    
    @property
    def cliente(self): return self.__cliente
    
    @property
    def status(self): return self.__status
    
    @status.setter
    def status(self, novo_status: str):
        self.__status = novo_status
        
    @property
    def valor_frete(self): return self.__valor_frete
    
    @property
    def distancia(self): return self.__distancia
    
    def exibir_resumo(self):
        return f"Pedido {self.__codigo} | Cliente: {self.__cliente.nome} | Status: {self.__status} | Frete: R$ {self.__valor_frete:.2f}"