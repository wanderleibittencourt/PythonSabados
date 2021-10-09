# Crie teste para usando as seguintes condiçoes
# Not - and - or - == - !=
# Not Verificar se o valor não e verdadeiro
# And - Verificar se as duas condições são verdadeiras
# Or - Verificar se uma das duas condições são verdadeiras
# == - Verificar igualdade entre dois valores
# != - Verificar se os valores são diferentes
#

from unittest import TestCase
import unittest

class Test(TestCase):

    def test_usando_not(self):
        a = " "
        a = a.strip()
        assert not a

    def test_usando_and(self):
        pessoa1 = "Ana"
        pessoa2 = "Junior"
        pessoa3 = "Ana"
        pessoa4 = "Junior"
        assert pessoa1 == pessoa3 and pessoa2 == pessoa4

    def test_usando_or(self):
        numero1 = 1
        numero2 = 2
        numero3 = "3"
        assert numero1 or numero2 != numero3

    def test_startwitch(self):
        nome = "Marley"

        assert nome.startswith("M") #inicio do nome
        assert nome.endswith("y") # fim do nome


    def test_usando_condicao_diferente(self):
        n1 = 5
        n2 = 10
        assert n1 != n2

    def test_usando_condicao_igualdade(self):

        ano1 = 2021
        ano2 = 2021
        assert ano1 == ano2

if __name__ == "__main__":
    unittest.main()
