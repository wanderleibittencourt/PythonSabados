# Crie uma classe de produtos
# Que tenha seus atributos privados __
# Utilizando o getter e setter para poder alterar seus valores
# Sem property

# Crie uma classe de Categorias
# Que tenha seus atributos privados __
# Utilizando o getter e setter para poder alterar seus valores
# Com property

class Produtos:

    def __init__(self,nome, valor) -> None:
        self.__nome = nome
        self.__valor = valor

    def get_nome(self):
        return self.__nome

    def get_valor(self):
        return self.__valor

    def alterar_nome(self, nome):
        self.__nome = nome
    
    def alterar_valor(self, valor):
        self.__valor = valor

produto = Produtos("Skol", 2.00)
print(produto.get_nome())
print(produto.get_valor())
produto.alterar_nome("Coca-cola")
produto.alterar_valor(4.00)
print(produto.get_nome(), produto.get_valor())


class Categoria:

    def __init__(self,nome,quantidade) -> None:
        self.__nome = nome
        self.__quantidade = quantidade

    def mostrar_nome(self):
        return self.__nome

    def mostrar_quantidade(self):
        return self.__quantidade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, cat):
        self.__nome = cat

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def valor(self, valores_reais):
        self.__quantidade = valores_reais
            

categoria = Categoria("cerveja", 10)
print(categoria.mostrar_nome(), categoria.mostrar_quantidade())
categoria.__nome = "Refrigerante"
categoria.__quantidade = 50
print(categoria.__nome, categoria.__quantidade)
