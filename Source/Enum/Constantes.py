#!/usr/bin/env python
# coding=utf-8

from enum import Enum

class Constantes( Enum ):

    SCREEN_ALTO: int = 512
    """
    Alto de la ventana principal en pixeles.
    """

    SCREEN_ANCHO: int = 1024
    """
    Ancho de la ventana principal en pixeles.
    """

    MAPA_ALTO: int = 32
    """
    Alto del mapa de la App.
    """

    MAPA_ANCHO: int = 64
    """
    Ancho del mapa de la App.
    """

    PIXELES: int = 16
    """
    Alto y ancho de cada sprite en pixeles.
    """

    MAXIMO_ARMADURA_NIVEL: int = 3
    """
    Número máximo de armaduras por nivel.
    """

    MAXIMO_ESPADA_NIVEL: int = 3
    """
    Número máximo de espadas por nivel.
    """

    MAXIMO_POCION_NIVEL: int = 4
    """
    Número máximo de pociones por nivel.
    """

    MAXIMO_ENEMIGOS_NIVEL: int = 1
    """
    Máximo de enemigos que pueden haber en un nivel del mapa.
    """
