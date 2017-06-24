# -*- coding: utf-8 -*-

import random

from pygame import Surface
from pygame.sprite import Sprite
from Source.Core.Punto import Punto
from Source.Enum.Constantes import Constantes


class GameObject( Sprite ):
    """
    Un clase generica que contiene los metodos de los diferentes objectos del juego.
    """

    # CONSTANTES DE CLASE
    PIXELES: int = Constantes.PIXELES.value
    """
    Ancho y alto de un Tile.
    """

    DIRECTION: list = ['L', 'R', 'D', 'U']  # Left, right, down, up

    # ATRIBUTOS DE CLASE



    # CONSTRUCTOR DE LA CLASE
    def __init__(self, screen: Surface, coordenada: Punto, imagen: object, mapa: object, *groups):
        """ 
        Constructor de la clase.
        @param screen: the screen to draw on
        @type screen: SurfaceType
        @param coordenada: La posicion del objecto representado por una tupla de dos valores (x, y).
        @type coordenada: Punto
        @param imagen: La imagen del objecto.
        @type imagen: object
        @param mapa: El mapa.
        @type mapa: object
        """
        super().__init__(*groups)

        self.screen: Surface = screen
        self.imagen: object = imagen
        self.mapa: object = mapa
        self.coordenada: Punto = self.legalStartPosition(coordenada[0], coordenada[1])

    # MÉTODOS

    def update(self, mapa: object, coordenada: Punto) -> None:
        """
        Actualiza el Objecto de juego.
        @param mapa: El mapa.
        @type mapa: object
        @param coordenada: Una tupla de dos valores (x, y) que contiene la nueva posicion del Objecto.
        @type coordenada: tuple(int, int)
        """
        self.mapa = mapa
        self.coordenada: Punto = self.legalStartPosition(coordenada[0], coordenada[1])

    def getCoordenadaX(self) -> int:
        """
        Devuelve la coordenada en el eje X.
        @return: Coordenada en el eje X.
        @rtype: int
        """
        return self.coordenada.getCoordenadaX()

    def setCoordenadaX(self, x: int) -> None:
        """
        Establecemos una nueva coordenada en el eje X.
        @param x: Nueva coordenada en el eje X.
        @type x: int
        """
        self.coordenada.setCoordenadaX(x)

    def getCoordenadaY(self) -> int:
        """
        Devuelve la coordenada en el eje Y.
        @return: Coordenada en el eje Y.
        @rtype: int
        """
        return self.coordenada.getCoordenadaY()

    def setCoordenadaY(self, y: int) -> None:
        """
        Establecemos una nueva coordenada en el eje Y.
        @param y: Nueva coordenada en el eje Y.
        @type y: int
        """
        self.coordenada.setCoordenadaY(y)

    def mover(self, x: int, y: int) -> None:
        """
        Metodo que cambia la posicion de los Enemigos para moverlos alrededor.
        @param x: Coordenada en el eje x.
        @type x: int
        @param y: Coordenada en el eje y.
        @type y: int
        """
        self.setCoordenadaX(self.getCoordenadaX() + x )
        self.setCoordenadaY(self.getCoordenadaY() + y )

    def dibujar(self) -> None:
        """
        Metodo para dibujar el objecto en la pantalla.
        """
        self.screen.blit(self.imagen, (self.coordenada.getCoordenadaX() * self.PIXELES, self.coordenada.getCoordenadaY() * self.PIXELES))

    def legalStartPosition(self, x: int, y: int) -> Punto:
        """
        Revisa si la posicion pasada por parámetro es válidad para una posicion inicial.
        Funcion recursiva.
        @param x: Coordenada en el eje X.
        @type x: int
        @param y: Coordenada en el eje Y.
        @type y: int
        @return: Devuelve una tupla (x: int, y: int) cuando está es válidad como una posicion inicial.
        @rtype: tuple(int, int)
        """

        #Is this tile a wall, True if not, False if it is a wall
        if self.mapa[y][x].isTransitable():
            return Punto(x, y)
        else:
            # Generamos dos números random y los pasamos por párametro.
            x = random.randrange(0, len(self.mapa[0]))
            y = random.randrange(0, len(self.mapa))
            return self.legalStartPosition(x, y)

