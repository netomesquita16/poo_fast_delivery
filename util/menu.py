#Funções visuais para o terminal.

import os

class Menu:
    @staticmethod
    def limpar_tela():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def exibir_menu_principal():
        print("\n--- FASTDELIVERY EXPRESS ---")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Criar Pedido")
        print("4. Listar Pedidos")
        print("5. Atualizar Status do Pedido")
        print("0. Sair")
        return input("Escolha uma opção: ")