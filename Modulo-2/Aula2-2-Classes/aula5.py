from time import sleep

class Escritor:
     #METODO CONSTRUTOR
    def __init__(self,nome,livros) -> None:
        self.__nome = nome
        self.__titulos = livros
    #Getter
    def get_nome(self):
        return self.__nome
    #Getter
    def get_titulos(self):
        for livros in self.__titulos: #["livro1","livro2","livro3"]
            sleep(1) # quantidade de segunto a imprimir
            print(livros)
    #Setter
    def set_nome(self,valor):
        self.__nome = valor
#Variavel Instancia da classe Escritor - valores que estou passando para dentro da classe
escritor = Escritor("shakspeare", ["livro1","livro2","livro3"])
print(escritor.get_nome())
escritor.set_nome("Machado de assis")
print(escritor.get_nome())

escritor.get_titulos()

class Escritor:
     #METODO CONSTRUTOR
    def __init__(self,nome,livros) -> None:
        self.__nome = nome
        self.__titulos = livros

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def titulos(self):
        return self.__titulos

    @titulos.setter
    def titulos(self, abacaxi):
        self.__titulos = abacaxi


escritor = Escritor("shakspeare", ["livro1","livro2","livro3"])
print(escritor.nome)
escritor.nome = "Machado de Assis"
print(escritor.nome)