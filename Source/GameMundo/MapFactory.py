#!/usr/bin/env python
# coding=utf-8

import random
import pygame

from Source.GameObjects.Player import Player
from Source.GameObjects.Item import Item
from Source.GameObjects.GameObject import Monster
from Source.Enum.EnumImage import EnumImage
from Source.Enum.EnumConstantes import EnumConstantes

class Factory:
    """
    Clase que se encarga de generar y fabricar los objectos y entidades.
    """

    # ATRIBUTOS

    MONSTER_COUNT: int = 15
    """
    Máximo de enemigos que pueden haber en un mapa.
    """

    PIXELES: int = EnumConstantes.PIXELES.value
    """
    Obtenemos el valor de la constante PIXELES.
    """

    MAPA_ANCHO: int = EnumConstantes.MAPA_ANCHO.value
    """
    Ancho total del mapa en pixeles.
    """

    MAPA_ALTO: int = EnumConstantes.MAPA_ALTO.value
    """
    Alto total del mapa en pixeles.
    """

    # CONSTRUCTOR

    def __init__(self):
        pass

    # MÉTODO

    def OnFactoryMonsters(self, screen, cave, MONSTERS_TILES: list, dungeonLevel: int):
        """
        Los enemigos cambian sus estadistidas y son asesinados en cada nivel, asi que creamos nuevos enemigos cada
        nuevo nivel que el jugador avance.
        @param screen: La ventana de juego para dibujar.
        @param cave: El mapa.
        @param MAPA_ANCHO: El ancho del mapa (area jugable) en pixeles.
        @param MAPA_ALTO: El alto del mapa (area jugable) en pixeles.
        @param MONSTERS_TILES: Imagenes de los enemigos.
        @param dungeonLevel: El nivel actual de la mazmorra.
        @return: Lista con los enemigos creados.
        """

        monsters: list = []

        for i in range( self.MONSTER_COUNT ):
            monsters.append(Monster(
                screen,
                posicion= (random.randrange(0, self.MAPA_ANCHO, self.PIXELES), random.randrange(0, self.MAPA_ALTO, self.PIXELES)),
                object_image = MONSTERS_TILES[random.randint(0, len(MONSTERS_TILES) - 1)],
                object_cave = cave,
                dungeon_level = dungeonLevel ))

        return monsters

    def onFactoryArmadura(self, screen, mapa):

        rutaImagen = EnumImage.ARMADURA.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        x = random.randrange(0, self.MAPA_ANCHO, self.PIXELES)
        y = random.randrange(0, self.MAPA_ALTO, self.PIXELES)

        armadura = Item(
            screen=screen,
            posicion=(x, y),
            object_image=imagen,
            object_cave=mapa,
            nombre="armor",
            valor=1
        )

        return armadura

    def onFactoryEspada(self, screen, mapa):

        rutaImagen = EnumImage.ESPADA.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        x = random.randrange(0, self.MAPA_ANCHO, self.PIXELES)
        y = random.randrange(0, self.MAPA_ALTO, self.PIXELES)

        espada = Item(
            screen=screen,
            posicion=(x, y),
            object_image=imagen,
            object_cave=mapa,
            nombre="weapon",
            valor=1)

        return espada

    def onFactoryPocion(self, screen, mapa):

        rutaImagen = EnumImage.POCION.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        x = random.randrange(0, self.MAPA_ANCHO, self.PIXELES)
        y = random.randrange(0, self.MAPA_ALTO, self.PIXELES)

        pocion = Item(
            screen=screen,
            posicion=(x, y),
            object_image=imagen,
            object_cave=mapa,
            nombre="food",
            valor=20)

        return pocion

    def onFactoryPuertaMadera(self, screen, mapa):

        rutaImagen = EnumImage.PUERTA_MADERA.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        x = random.randrange(0, self.MAPA_ANCHO, self.PIXELES)
        y = random.randrange(0, self.MAPA_ALTO, self.PIXELES)

        puertaMadera = Item(
            screen=screen,
            posicion=(x, y),
            object_image=imagen,
            object_cave=mapa,
            nombre="Puerta de Madera",
            valor=0)

        return puertaMadera

    def onFactoryOgroMago(self, screen, mapa, dungeonLevel):

        rutaImagen = EnumImage.OGRO_MAGO.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        x = random.randrange(0, self.MAPA_ANCHO, self.PIXELES)
        y = random.randrange(0, self.MAPA_ALTO, self.PIXELES)

        ogroMago = Monster(
            screen=screen,
            posicion=(x, y),
            object_image=imagen,
            object_cave=mapa,
            dungeon_level=dungeonLevel)

        return ogroMago

    def onFactoryMummy(self, screen, mapa, dungeonLevel):

        rutaImagen = EnumImage.MUMMY.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        x = random.randrange(0, self.MAPA_ANCHO, self.PIXELES)
        y = random.randrange(0, self.MAPA_ALTO, self.PIXELES)

        mummy = Monster(
            screen=screen,
            posicion=(x, y),
            object_image=imagen,
            object_cave=mapa,
            dungeon_level=dungeonLevel)

        return mummy

    def onFactoryDragonRojo(self):
        pass

    def onFactoryGusanoCerebro(self):
        pass

    def onFactoryCucarachaGigante(self):
        pass

    def onFactoryJugador(self, screen, mapa, dungeonLevel):

        rutaImagen = EnumImage.JUGADOR.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        x = random.randrange(0, self.MAPA_ANCHO, self.PIXELES)
        y = random.randrange(0, self.MAPA_ALTO, self.PIXELES)

        jugador = Player(
            screen=screen,
            posicion=(x, y),
            object_image=imagen,
            object_cave=mapa,
            dungeon_level=dungeonLevel)

        return jugador
