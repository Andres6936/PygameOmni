#!/usr/bin/env python
# coding=utf-8

import pygame

from Source.Enum.Constantes import Constantes

class MapRender():
    """
    Clase para renderizar el mapa de juego de la App.
    """

    PIXELES: int = Constantes.PIXELES.value
    MAPA_ALTO: int = Constantes.SCREEN_ALTO.value
    MAPA_ANCHO: int = Constantes.SCREEN_ANCHO.value

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
        for x in range(0, int(MapRender.MAPA_ALTO / MapRender.PIXELES)):
            for y in range(0, int(MapRender.MAPA_ANCHO / MapRender.PIXELES)):
                mapa[x][y].dibujar()