#Aqui centralizamos a criação dos tipos de entrega para facilitar.

from modelos.entrega import EntregaComum, EntregaExpressa, EntregaPremium

class EntregaService:
    @staticmethod
    def instanciar_entrega(tipo: int):
        if tipo == 1:
            return EntregaComum()
        elif tipo == 2:
            return EntregaExpressa()
        elif tipo == 3:
            return EntregaPremium()
        return None