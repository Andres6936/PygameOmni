import unittest

from Source.Core.Punto import Punto


class TestPunto (unittest.TestCase):

    # Atributos

    punto1: Punto = None
    punto2: Punto = None
    punto3: Punto = None


    # Test de Métodos

    def test_isIgualTrue( self ):
        """
        Test para método isIgual de la clase Punto.
        """

        self.configurarEscenario1()

        self.assertEqual(punto1.isIgual(punto2), True, "Error")

        self.resetConfiguracion()

    def test_isIgualFalse(self):
        """
        Test para método isIgual de la clase Punto.
        """

        self.configurarEscenario1()

        self.assertEqual(punto1.isIgual(punto3), False, "Error")

        self.resetConfiguracion()

    # Configuracion de Escenarios.

    def configurarEscenario1(self):
        """
        Configuramos el escenario 1.
        """

        global punto1
        global punto2
        global punto3

        punto1 = Punto(69, 69)
        punto2 = Punto(69, 69)
        punto3 = Punto(69, 36)

    # Resetear configuracion

    def resetConfiguracion(self):
        """
        Resetea la configuracion de las variables globales.
        """

        global punto1
        global punto2
        global punto3

        punto1 = None
        punto2 = None
        punto3 = None


if __name__ == '__main__':
    unittest.main()
