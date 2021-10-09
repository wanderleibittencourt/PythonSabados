

class ClasseDeTreino:

    def retornando_uma_lista(self):
        return []

    def retornando_uma_tupla(self):
        return ()

    def retornando_um_dicionario(self):
        return {}

    def retornando_uma_string(self):
        return "String"

    def retornando_um_interger(self):
        return 1

    def retornando_um_float(self):
        return 12.5

    def retornando_um_boolean(self):
        return True

#Exemplo:
#self.assertIsInstance(ClasseDeTreino.retornando_um_boolean, bool)
#self.assertEqual(ClasseDeTreino.retornando_um boolean, True)
import unittest
from unittest import TestCase


class TestClasseDeTreino(TestCase):

    def test_retorno_metodo_de_lista(self):
        minha_classe = ClasseDeTreino()

        self.assertIsInstance(minha_classe, ClasseDeTreino)
        self.assertEqual(minha_classe.retornando_uma_lista(),[])

    def test_retorno_metodo_tupla(self):
        minha_classe = ClasseDeTreino()

        self.assertIsInstance(minha_classe,ClasseDeTreino)
        self.assertEqual(minha_classe.retornando_uma_tupla(),())

    def test_retorno_metodo_dicionario(self):
        minha_classe = ClasseDeTreino()

        self.assertIsInstance(minha_classe,ClasseDeTreino)
        self.assertEqual(minha_classe.retornando_um_dicionario(),{})

    def test_retorno_metodo_string(self):
        minha_classe = ClasseDeTreino()

        self.assertIsInstance(minha_classe,ClasseDeTreino)
        self.assertEqual(minha_classe.retornando_uma_string(),("String"))

    def test_retorno_metodo_interger(self):
        minha_classe = ClasseDeTreino()

        self.assertIsInstance(minha_classe,ClasseDeTreino)
        self.assertEqual(minha_classe.retornando_um_interger(), 1)

    def test_retorno_metodo_float(self):
        minha_classe = ClasseDeTreino()

        self.assertIsInstance(minha_classe,ClasseDeTreino)
        self.assertEqual(minha_classe.retornando_um_float(),12.5)

    def test_retorno_metodo_boolean(self):
        minha_classe = ClasseDeTreino()

        self.assertIsInstance(minha_classe,ClasseDeTreino)
        self.assertEqual(minha_classe.retornando_um_boolean(), True )



    



if __name__ == "__main__":
    unittest.main()


