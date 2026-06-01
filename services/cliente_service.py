#Aqui implementamos as regras de negócio: cadastrar, buscar, listar, etc.

from modelos.cliente import Cliente

class ClienteService:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, nome, cpf, telefone, endereco):
        novo_cliente = Cliente(nome, cpf, telefone, endereco)
        self.clientes.append(novo_cliente)
        return novo_cliente

    def listar_clientes(self):
        return self.clientes

    def buscar_cliente_por_cpf(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None