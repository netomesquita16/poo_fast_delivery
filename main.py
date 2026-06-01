from services.cliente_service import ClienteService
from services.pedido_service import PedidoService
from services.entrega_service import EntregaService
from util.menu import Menu
from util.formatador import Formatador

def main():
    cliente_service = ClienteService()
    pedido_service = PedidoService()

    while True:
        Menu.limpar_tela()
        opcao = Menu.exibir_menu_principal()

        if opcao == '1':
            print("\n-- Cadastro de Cliente --")
            nome = input("Nome: ")
            cpf = input("CPF: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            cliente_service.cadastrar_cliente(nome, cpf, telefone, endereco)
            print("Cliente cadastrado com sucesso!")
            input("Pressione ENTER para continuar...")

        elif opcao == '2':
            print("\n-- Lista de Clientes --")
            clientes = cliente_service.listar_clientes()
            for c in clientes:
                print(f"Nome: {c.nome} | CPF: {c.cpf} | Endereço: {c.endereco}")
            input("\nPressione ENTER para continuar...")

        elif opcao == '3':
            print("\n-- Criar Pedido --")
            cpf_cliente = input("CPF do Cliente: ")
            cliente = cliente_service.buscar_cliente_por_cpf(cpf_cliente)
            
            if not cliente:
                print("Cliente não encontrado!")
            else:
                codigo = input("Código do Pedido: ")
                peso = float(input("Peso (kg): "))
                distancia = float(input("Distância (km): "))
                
                print("Tipos de Entrega: 1-Comum | 2-Expressa | 3-Premium")
                tipo_opcao = int(input("Escolha o tipo: "))
                tipo_entrega = EntregaService.instanciar_entrega(tipo_opcao)
                
                if tipo_entrega:
                    pedido = pedido_service.criar_pedido(codigo, cliente, peso, distancia, tipo_entrega)
                    print(f"Pedido criado! Valor do frete: {Formatador.formatar_moeda(pedido.valor_frete)}")
                else:
                    print("Tipo de entrega inválido.")
            input("\nPressione ENTER para continuar...")

        elif opcao == '4':
            print("\n-- Lista de Pedidos --")
            pedidos = pedido_service.listar_pedidos()
            for p in pedidos:
                print(p.exibir_resumo())
            input("\nPressione ENTER para continuar...")

        elif opcao == '5':
            print("\n-- Atualizar Status --")
            codigo = input("Código do Pedido: ")
            print("Status: 1-Em preparação | 2-Saiu para entrega | 3-Entregue | 4-Cancelado")
            op_status = input("Escolha: ")
            mapa_status = {"1": "Em preparação", "2": "Saiu para entrega", "3": "Entregue", "4": "Cancelado"}
            
            if op_status in mapa_status:
                sucesso = pedido_service.atualizar_status(codigo, mapa_status[op_status])
                if sucesso:
                    print("Status atualizado com sucesso!")
                else:
                    print("Pedido não encontrado.")
            else:
                print("Status inválido.")
            input("\nPressione ENTER para continuar...")

        elif opcao == '0':
            print("Saindo do sistema...")
            break

if __name__ == "__main__":
    main()