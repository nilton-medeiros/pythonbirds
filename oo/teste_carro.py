from unittest import TestCase
from oo.carro import Motor

"""
Nome do arquivo de teste deve começar com a palavra "test" em inglês.
A classe deve começar com o primeiro método com a palavra "test". Como a palavra em português começa com test
pode-se utilizar "teste_alguma_coisa"
"""


class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)