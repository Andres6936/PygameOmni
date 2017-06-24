#!/usr/bin/env python
# coding=utf-8

import pygame

from Source.Enum.Constantes import Constantes

class InterfazOmni:
    """
    Clase para renderizar el mapa de juego de la App.
    """

    # CONSTANTES DE LA CLASE
    PIXELES: int = Constantes.PIXELES.value
    """
    Ancho y Alto en pixeles de una imagen.
    """

    MAPA_ALTO: int = Constantes.MAPA_ALTO.value
    """
    Alto del mapa de la App.
    """

    MAPA_ANCHO: int = Constantes.MAPA_ANCHO.value
    """
    Ancho del mapa de la App.
    """

    # ATRIBUTOS DE LA CLASE
    mundo = None
    """
    Mapa principal de la App, en el cual los eventos suceden.
    El mundo es un array de Tiles donde la magia sucede.
    """

    # CONSTRUCTOR DE CLASE
    def __init__(self, mapa):
        """
        Constructor de la clase U{InterfazOmni}.
        """
        global mundo

        # Configuramos el mapa, mundo o mazmorras.
        mundo = mapa

    # MÉTODOS

    def setMundo(self, nuevoMundo) -> None:
        """
        Establece un nuevo mundo.
        @param nuevoMundo: El nuevo mundo que será dibujado.
        """

        global mundo

        # Establecemos un nuevo mundo.
        mundo = nuevoMundo

    def dibujarMapa(self) -> None:
        """
        Dibuja el mapa de la App.
        """

        global mundo

        for y in range(0, self.MAPA_ALTO):
            for x in range(0, self.MAPA_ANCHO):
                mundo[y][x].dibujar()