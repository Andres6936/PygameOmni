#!/usr/bin/env python
# coding=utf-8

import pygame

from Source.Enum.Constantes import Constantes

class MapRender():
    """
    Clase para renderizar el mapa de juego de la App.
    """

    PIXELES: int = Constantes.PIXELES.value
    MAPA_ALTO: int = Constantes.MAPA_ALTO.value
    MAPA_ANCHO: int = Constantes.MAPA_ANCHO.value

    # CONSTRUCTOR DE CLASE
    def __init__(self):
        """
        Constructor de la clase U{MapRender}.
        """
        pass

    # MÉTODOS

    def dibujarMapa(self, mapa: list) -> None:
        """
        Dibuja el mapa de la App.
        @param mapa: El mapa a dibujar.
        @type mapa: list
        """
        for y in range(0, int(self.MAPA_ALTO)):
            for x in range(0, int(self.MAPA_ANCHO)):
                mapa[y][x].dibujar()