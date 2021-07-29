class Produto():
    def __init__(self, titulo, valor):
        self.titulo = titulo
        self.valor = valor
        self.desconto = None
    
    def getTitulo(self):
        return self.titulo
    
    def setTitulo(self, novoTitulo):
        self.titulo = novoTitulo

    def getValor(self):
        return self.valor
    
    def setValor(self, novoValor):
        self.valor = novoValor

    def getDesconto(self):
        if self.desconto != None:
            desconto = self.desconto * self.valor
            return desconto
        else:
            return 0

    def setDesconto(self, novoDesconto):
        self.desconto = novoDesconto
    
    def getValorComDesconto(self):
        valorComDesconto = self.valor - self.getDesconto()
        return valorComDesconto

    def descreverProduto(self):
        print("  Categoria:",self.__class__.__name__)
        print("     Título:",self.getTitulo())
        print(f"      Valor: R$ {self.getValor():.2f}")
        print(f"   Desconto: R${self.getDesconto():.2f}")
        print(f"Valor final: R${self.getValorComDesconto():.2f}")

class Livro(Produto):
    def __init__(self, titulo, valor, autor):
        super().__init__(titulo, valor)
        super().setDesconto(0.10)
        self.autor = autor
    
    def getAutor(self):
        return self.autor

    def setAutor(self, novoAutor):
        self.autor = novoAutor

    def descreverProduto(self):
        super().descreverProduto()
        print("      Autor:", self.getAutor())

class CD(Produto):
    def __init__(self, titulo, valor, artista):
        super().__init__(titulo, valor)
        super().setDesconto(0.15)
        self.artista = artista
    
    def getArtista(self):
        return self.artista

    def setArtista(self, novoArtista):
        self.artista = novoArtista

    def descreverProduto(self):
        super().descreverProduto()
        print("    Artista:",self.getArtista())

class DVD(Produto):
    def __init__(self, titulo, valor, duracao):
        super().__init__(titulo, valor)
        super().setDesconto(0.20)
        self.duracao = duracao

    def getDuracao(self):
        return self.duracao

    def setDuracao(self, novaDuracao):
        self.duracao = novaDuracao

    def descreverProduto(self):
        super().descreverProduto()
        print("    Duração:", self.getDuracao())

class Compra():
    def __init__(self):
        self.carrinho = []
        self.valorCompra = 0
    
    def getCarrinho(self):
        return self.carrinho
    
    def setCarrinho(self, novoCarrinho):
        self.carrinho = novoCarrinho

    def getValorCompra(self):
        return self.valorCompra
    
    def setValorCompra(self, novoValorCompra):
        self.valorCompra = novoValorCompra
    
    def descreverCompra(self):
        for produto in self.getCarrinho():
            produto.descreverProduto()
            print("························")
    
    def pedido(self):
        print("········Produtos········")
        self.descreverCompra()
        print(f"Total: R${self.getValorCompra():.2f}")
        print("························\n")
            
class main():
    def __init__(self):
        self.opcao = None
        self.listaProdutos = []

    def getOpcao(self):
        return self.opcao
    
    def setOpcao(self, novaOpcao):
        self.opcao = novaOpcao
    
    def getListaProdutos(self):
        return self.listaProdutos
    
    def setListaProdutos(self, novaListaProdutos):
        self.listaProdutos = novaListaProdutos

    def comprar(self):
        valorCompra = 0

        compra = Compra()

        id = None

        while id != 0:
            id = int(input("Digite o ID do produto que eu devo adicionar ao carrinho: "))
            if id <= len(self.getListaProdutos()):
                valorProduto = self.getListaProdutos()[id].getValorComDesconto()
                valorCompra += valorProduto
                compra.getCarrinho().append(self.getListaProdutos()[id])
                print("Pronto, adicionado!\n")
            else:
                print("Acho que não tem ou falta cadastrar esse :/")
                print("Não adicionei por precaução, tudo bem?\n")

            compra.setValorCompra(valorCompra)  
        compra.pedido()

    def menu(self):
        dvd1 = DVD("Click", 20, "1:47:00")
        dvd2 = DVD("Interestellar", 30, "2:55:00")
        dvd3 = DVD("Clube da Luta", 25, "2:31:00")
        livro1 = Livro("The final six", 39.90, "Alexandra Monir")
        livro2 = Livro("A divina comédia", 32.68, "Dante Alighieri")
        livro3 = Livro("1984", 14.89, "George Orwell")
        cd1 = CD("A Raposa e as Uvas", 20, "Reginaldo Rossi")
        cd2 = CD("True", 20, "Avicii")
        cd3 = CD("Go back", 20, "Titãs")
        produto1 = Produto("Marca-texto", 2)
        produto2 = Produto("Régua", 6)
        produto3 = Produto("Post-it (400f)", 19.20)
        
        self.setListaProdutos([0, dvd1, dvd2, dvd3, livro1, livro2, livro3, cd1, cd2, cd3, produto1,produto2, produto3])

        print("Oi, chefe! Vamos vender?")
        print("Me indique o que fazer:")

        while self.getOpcao() != "0":
            print("1 - Nova venda")
            print("0 - Sair")

            self.setOpcao(input("Opção desejada: "))

            if self.getOpcao() == "1":
                self.comprar()

            elif self.getOpcao() == "0":
                print("Desligando, chefe... Até a próxima :)")

            else:
                print("Vish, acho que não sei fazer isso. Que tal tentar algum destes? ↓")

menuInicial = main()
menuInicial.menu()