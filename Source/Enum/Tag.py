#!/usr/bin/env python
# coding=utf-8

from enum import Enum
from enum import unique

@unique
class Tag( Enum ):
    """
    Enumerandos con valores únicos, contiene las TAG de objectos y entidades.
    """

    # ENTIDADES
    PACIFICO = "PACIFICO"
    JUGADOR = "JUGADOR"
    HOSTIL = "HOSTIL"

    # GENERAL {ENTIDADES / OBJECTOS}
    NONE = "NONE"

    # OBJECTOS
    PUERTA = "PUERTA"
    ARMADURA = "ARMADURA"
    POCION = "POCION"
    ARMAS = "ARMAS"