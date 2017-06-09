#!/usr/bin/env python
# coding=utf-8

from enum import Enum

class EnumConstantes( Enum ):

    MAPA_ALTO: int = 512
    """
    Alto del mapa en pixeles.
    """

    MAPA_ANCHO: int = 1024
    """
    Ancho del mapa en pixeles.
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

    MAXIMO_ENEMIGOS_NIVEL: int = 15
    """
    Máximo de enemigos que pueden haber en un nivel del mapa.
    """