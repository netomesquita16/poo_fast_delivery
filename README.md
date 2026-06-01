# poo_fast_delivery

# FastDelivery Express - Sistema de Gerenciamento de Entregas

## 1. Descrição do Projeto
O FastDelivery Express é um sistema em console para gerenciamento de entregas urbanas. Ele permite cadastrar clientes, gerenciar pedidos, atualizar status de rastreio e calcular automaticamente o frete com base na distância e no tipo de serviço escolhido (Comum, Expressa ou Premium).

## 2. Tecnologias Utilizadas
* Python 3
* Git
* GitHub

## 3. Estrutura de Pastas
O projeto está organizado segundo o padrão de camadas para garantir separação de responsabilidades:
* `interfaces/`: Contém as classes abstratas (contratos) do sistema.
* `modelos/`: Contém as classes de entidade (Cliente, Entregador, Pedido, Entrega).
* `services/`: Contém as regras de negócio e armazenamento em memória.
* `util/`: Contém scripts auxiliares (menus, formatações).
* `main.py`: Ponto de entrada do console.

## 4. Conceitos de POO Utilizados
* **Herança:** As classes `Cliente` e `Entregador` herdam da superclasse `Pessoa`.
* **Interface:** Criada a interface `CalculoFreteInterface` usando a biblioteca `abc` para definir a assinatura do cálculo de frete.
* **Polimorfismo:** O método `calcular_frete()` atua de formas diferentes dependendo da classe que o implementa (`EntregaComum`, `EntregaExpressa`, `EntregaPremium`).
* **Encapsulamento:** Utilização de atributos privados (`__nome`, `__cpf`) e acesso através de decorators (`@property`, `@setter`).

## 5. Como executar o projeto
Certifique-se de ter o Python 3 instalado em sua máquina. Clone este repositório e rode no terminal: python main.py