from typing import TypedDict

Ingredientes = TypedDict("Ingredientes",{"nome": str, "custo": float , "quantidade": int})
Pizza = TypedDict(
    "Pizza",{"ingredientes": list[Ingredientes], "tamanho": int, "custo": float}
)
Pedido = TypedDict(
    "Pedido",{
    
    "id": int,
    "nomeDoCliente": str,
    "pizzas": Pizza,
    "dataEHora": int,
    "tempoDePreparo": int,
    "status": str,
    "custo": float,
    },

)
FilaDePedidos = TypedDict("FiladePedidos", {"pedidos": Pedido})
HistoricoDePedidos = TypedDict("HistoricoDePedidos" , {"pedidos": FilaDePedidos})

Cancelamento = TypedDict("Cancelamento", {"status": Pedido})

def calcular_custo_ingredientes(ingrediente: Ingredientes):
    return ingrediente["custo"] * ingrediente["quantidade"]


def calcular_custo_pizza(pizza:Pizza):
    total = 0 
    for ingredientes in pizza ["ingredientes"]:
        total += calcular_custo_ingredientes(ingredientes)

    pizza["custo"] = total 

def calcularPrecoFinal(pedido:Pizza):
    custoFinal = pedido["ingredientes"]
    return pedido ["custo"]

def criar_ingrediente(nome:str , custo: float, quantidade: float) -> Ingredientes:
    ingrediente: Ingredientes = {"nome": nome, "custo": custo, "quantidade": quantidade}
    return ingrediente


def criar_pizza(nome: str ,ingredientes: list[Ingredientes], tamanho: str) ->Pizza:
    pizza:Pizza = {"nome": nome, "ingrediente": ingredientes, "tamanho": tamanho}
    calcular_custo_pizza(pizza)
    return pizza

print("Olá seja bem vindo a nossa Pizzaria , fazemos a melhor pizza da região")