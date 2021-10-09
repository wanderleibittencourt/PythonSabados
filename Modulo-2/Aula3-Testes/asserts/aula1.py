# Para garantir o comportamento de uma denominada aplicação é muito importante que tenhamos testes sobre a nossa aplicação

# Nessa secção veremos sobre o uso de asserts com unittest para verificar
# a veracidade do comportamento da função

# para gerar um teste devemos utilizar a palavra reservada assert

# Exemplo:

import unittest

class Test(unittest.TestCase):

    def test_aprendendo_testar(self):
        assert 1 == 1

    def test_string(self):
        assert "1" == "1"

    def test_booleano_dois(self):
        a = "teste"
        assert bool(a)

    def test_bolenaos(self):
        assert True == True


    def test_varios_testes(self):
        a = "Teste"
        b = "Teste"
        c = ""
        assert a == b or a == c
        #or == palavra 'ou'
        # a é igual a b ou a é igual a c

    def test_com_and(self):
        a = "Teste"
        b = "Teste"
        c = ""
        assert a == b and a != c
        #poderia por ! no lugarde == "a != c"

    def test_valor_inteiro(self):
        assert isinstance(1, int)
        assert isinstance("Sou uma string", str)
        assert isinstance(12.25, float)

    def test_com_not (self):
        a = "teste"
        b = "teste"
        c = ""
        assert a == b and not c



if __name__=="__main__":
    unittest.main()








# assert 1 == 1
# assert 1 == "1"
# assert 1 == 0

# podemos utilizar as condicionais para validar os testes.
# Exemplos:

# lista_frutas = ["laranja", "uva", "abacaxi", "melancia"]

# assert "laranja" in lista_frutas
# assert "laranja" not in lista_frutas
# assert not True
# assert not False

# assert "laranja" in lista_frutas and len(lista_frutas) > 3
