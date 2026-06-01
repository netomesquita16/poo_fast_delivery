from modelos.pedido import Pedido

class PedidoService:
    def __init__(self):
        self.pedidos = []

    def criar_pedido(self, codigo, cliente, peso, distancia, tipo_entrega):
        novo_pedido = Pedido(codigo, cliente, peso, distancia, tipo_entrega)
        self.pedidos.append(novo_pedido)
        return novo_pedido

    def listar_pedidos(self):
        return self.pedidos

    def atualizar_status(self, codigo, novo_status):
        status_validos = ["Em preparação", "Saiu para entrega", "Entregue", "Cancelado"]
        if novo_status not in status_validos:
            return False
        
        for pedido in self.pedidos:
            if pedido.codigo == codigo:
                pedido.status = novo_status
                return True
        return False