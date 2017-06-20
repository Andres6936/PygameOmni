#!/usr/bin/env python
# coding=utf-8

class Punto:
    """
    Clase Punto.
    Inicializa y crea un punto en el plano XY.
    """

    def __init__(self, x: int, y: int):
        """
        Constructor de la clase.
        @param x: Coordenada en el eje B{X}.
        @type x: int
        @param y: Coordenada en el eje B{Y}.
        @type y: int
        """

        Punto.verificarInvariante(x, y)

        self.x: int = x
        self.y: int = y

    def __getitem__(self, item: int) -> int:
        """
        Soporte para el indexado.
        @param item: Indice al que se quiere acceder.
        @type item: int
        @return: Elemento del indice.
        @rtype: int
        """

        Punto.verificarInvarianteGetter(item)

        coordenadaXY: tuple = self.getCoordenadaXY()

        return coordenadaXY[item]

    def getCoordenadaX(self) -> int:
        """
        Devuelve la coordenada en el eje B{X}.
        @return: Coordenada en el eje B{X}.
        @rtype: int
        """
        return self.x

    def setCoordenadaX(self, x: int) -> None:
        """
        Cambia la coordenda actual en el eje X a una nueva.
        @param x: Nueva coordenada en el eje X.
        @type x: int
        """
        self.x = x

    def getCoordenadaY(self) -> int:
        """
        Devuelve la coordenada en el eje B{Y}.
        @return: Coordenada en el eje B{Y}.
        @rtype: int
        """
        return self.y

    def setCoordenadaY(self, y: int) -> None:
        """
        Cambia la coordenda actual en el eje Y a una nueva.
        @param y: Nueva coordenada en el eje Y.
        @type y: int
        """
        self.y = y

    def getCoordenadaXY(self) -> tuple:
        """
        Devulve la coordenada en el eje B{X} y eje B{Y}.
        @return: Coordenada en el eje B{X} y eje B{Y} en forma de tupla de dos valores enteros.
        @rtype: tuple
        """
        return (self.getCoordenadaX(), self.getCoordenadaY())

    def equals(self, puntoDiferente) -> bool:
        """
        Compara si dos Puntos son iguales.
        @param puntoDiferente: El Punto con el que se quiere comparar.
        @type puntoDiferente: Punto
        @return: True si los Puntos son iguales (es decir, sus coordenadas en B{(x, y)} son iguales),
        False en caso contrario.
        @rtype: bool
        """
        if self.getCoordenadaX() is puntoDiferente.getCoordenadaX() and self.getCoordenadaY() is puntoDiferente.getCoordenadaY():
            return True
        else:
            return False

    @staticmethod
    def verificarInvariante(x: int, y: int):
        """
        Verifica las invariantes que puedan presentarse.
        @param x: Coordenada en el eje B{X}.
        @type x: int
        @param y: Coordenada en el eje B{Y}.
        @type y: int
        """

        assert x is not None, "{0} debe de ser diferente de null".format(x)
        assert y is not None, "{0} debe de ser difenrete de null".format(y)

    @staticmethod
    def verificarInvarianteGetter(indice: int):
        """
        Verifica las invariantes que puedan presentarse en el método Getter.
        @param indice: Indice al cual se quiere accerder.
        @type indice: int
        """
        assert indice < 2, "El punto se encuentra en el plano XY, el indice {0} no puede ser mayor a dos.".format(indice)
