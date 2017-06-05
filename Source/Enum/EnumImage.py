#!/usr/bin/env python
# coding=utf-8

from enum import Enum
from enum import unique


@unique
class EnumImage( Enum ):
    """
    Enumerando con valores únicos que contiene la ruta de las imagenes de los objectos usados
    en el juego.
    """

    # ENEMIGOS

    CUCARACHA_GIGANTE = "Graficas/Ikoner/Enemigos/giant_cockroach.png"
    GUSANO_CEREBRO = "Graficas/Ikoner/Enemigos/brain_worm.png"
    DRAGON_ROJO = "Graficas/Ikoner/Enemigos/red_dragon.png"
    OGRO_MAGO = "Graficas/Ikoner/Enemigos/ogre_mage.png"
    MUMMY = "Graficas/Ikoner/Enemigos/mummy.png"

    # JUGADOR

    JUGADOR = "Graficas/Ikoner/Player/player.png"

    # OBJECTOS

    PUERTA_MADERA = "Graficas/Ikoner/Items/Tiles/wooden_door.png"
    ARMADURA = "Graficas/Ikoner/Items/Armaduras/armor.png"
    POCION = "Graficas/Ikoner/Items/Pociones/potion.png"
    ESPADA = "Graficas/Ikoner/Items/Armas/sword.png"
