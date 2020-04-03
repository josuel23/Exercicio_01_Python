class Produto:
    def __init__(self, nome , preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Pedido:
    def __init__(self):
        self.produtos = []

    def adicionar_produtos(self, prod):
        self.produtos.append(prod)

    def calcular_valor(self):
        soma = 0
        for prod in self.produtos:
            soma += prod.preco * prod.quantidade
        return soma

café = Produto('Café', 5.50, 2)
arroz = Produto('Arroz Camil', 12.90, 1)
feijão = Produto('Feijão carioca', 5.40, 2)
açúcar = Produto('Açucar União', 2.65, 3)

meu_pedido = Pedido()
meu_pedido.adicionar_produtos(café)
meu_pedido.adicionar_produtos(arroz)
meu_pedido.adicionar_produtos(feijão)
meu_pedido.adicionar_produtos(açúcar)

print(f'O valor total é:, {meu_pedido.calcular_valor():.2f}')