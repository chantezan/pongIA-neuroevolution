import unittest
from playerAI import Player
from genetica import Genetico

class MyPlayer(unittest.TestCase):
    def testGenerarHijos(self):
        player1 = Player(cantidad=[6]
                            , activacion=["sigmoid"], dim_input=4, dim_output=1)
        player2 = Player(cantidad=[6]
                            , activacion=["sigmoid"], dim_input=4, dim_output=1)
        genetico = Genetico(16, number_children=10, iteraciones=100, cantidad=[6]
                            , activacion=["sigmoid"], dim_input=4, dim_output=1, label="")
        hijos = genetico.generarHijos(player1,player2)
        hijos2 = genetico.generarHijos(hijos[0], hijos[2])
        self.assertEqual(len(hijos), 10)
        self.assertEqual(len(hijos2), 10)

    def testTotalNeurona(self):
        player1 = Player(cantidad=[6]
                            , activacion=["sigmoid"], dim_input=4, dim_output=1)
        player2 = Player(cantidad=[6,3]
                            , activacion=["sigmoid","sigmoid"], dim_input=4, dim_output=1)

        self.assertEqual(player1.red.total_neuronas, 7)
        self.assertEqual(player2.red.total_neuronas, 10)

    def testGeneraHijo(self):
        player1 = Player(cantidad=[12]
                         , activacion=["sigmoid"], dim_input=4, dim_output=1)
        player2 = Player(cantidad=[12]
                         , activacion=["sigmoid"], dim_input=4, dim_output=1)
        hijo = player1.generarHijo(player2,100)
        self.assertEqual(hijo.red.total_neuronas, player1.red.total_neuronas)