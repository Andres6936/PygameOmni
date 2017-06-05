#!/usr/bin/env python
# coding=utf-8

from enum import Enum
from enum import unique

@unique
class EnumTags( Enum ):
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

    TAG_PUERTA_MADERA = "PUERTA MADERA"
    TAG_ARMADURA = "ARMADURA"
    TAG_POCION = "POCION"
    TAG_ARMAS = "ARMAS"