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

    def OnFactoryMonsters(self, screen, mapa, MONSTERS_TILES: list, dungeonLevel: int):
        """
        Los enemigos cambian sus estadistidas y son asesinados en cada nivel, asi que creamos nuevos enemigos cada
        nuevo nivel que el jugador avance.
        @param screen: La ventana de juego para dibujar.
        @param mapa: El mapa.
        @param MONSTERS_TILES: Imagenes de los enemigos.
        @param dungeonLevel: El nivel actual de la mazmorra.
        @return: Lista con los enemigos creados.
        """

        monsters: list = []

        MAX_ENEMIGOS_NIVEL: int = EnumConstantes.MAXIMO_ENEMIGOS_NIVEL.value

        for i in range( MAX_ENEMIGOS_NIVEL ):
            monsters.append(Monster(
                screen,
                coordenada= (random.randrange(0, self.MAPA_ANCHO, self.PIXELES), random.randrange(0, self.MAPA_ALTO, self.PIXELES)),
                imagen= MONSTERS_TILES[random.randint(0, len(MONSTERS_TILES) - 1)],
                mapa= mapa,
                dungeon_level = dungeonLevel ))

        return monsters

    @staticmethod
    def OnFactoryItems(screen, mapa):
        """
        Creamos los diferentes items y los añadimos a una lista.
        @param screen: Ventana de la App del juego para dibujar.
        @param mapa: El mapa de la App
        @return: Lista de items.
        """

        MAX_ARMADURA_NIVEL = EnumConstantes.MAXIMO_ARMADURA_NIVEL.value
        MAX_ESPADA_NIVEL = EnumConstantes.MAXIMO_ESPADA_NIVEL.value
        MAX_POCION_NIVEL = EnumConstantes.MAXIMO_POCION_NIVEL.value

        items: list = []

        for i in range(MAX_ARMADURA_NIVEL):
            items.append(Factory().onFactoryArmadura(screen, mapa))

        for i in range(MAX_ESPADA_NIVEL):
            items.append(Factory().onFactoryEspada(screen, mapa))

        for i in range(MAX_POCION_NIVEL):
            items.append(Factory().onFactoryPocion(screen, mapa))

        items.append(Factory().onFactoryPuertaMadera(screen, mapa))

        return items

    def onFactoryArmadura(self, screen, mapa):

        rutaImagen = EnumImage.ARMADURA.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        x = random.randrange(0, self.MAPA_ANCHO, self.PIXELES)
        y = random.randrange(0, self.MAPA_ALTO, self.PIXELES)

        armadura = Item(
            screen=screen,
            coordenada=(x, y),
            imagen=imagen,
            mapa=mapa,
            nombre="armor",
            bonus=1
        )

        return armadura

    def onFactoryEspada(self, screen, mapa):

        rutaImagen = EnumImage.ESPADA.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        x = random.randrange(0, self.MAPA_ANCHO, self.PIXELES)
        y = random.randrange(0, self.MAPA_ALTO, self.PIXELES)

        espada = Item(
            screen=screen,
            coordenada=(x, y),
            imagen=imagen,
            mapa=mapa,
            nombre="weapon",
            bonus=1)

        return espada

    def onFactoryPocion(self, screen, mapa):

        rutaImagen = EnumImage.POCION.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        x = random.randrange(0, self.MAPA_ANCHO, self.PIXELES)
        y = random.randrange(0, self.MAPA_ALTO, self.PIXELES)

        pocion = Item(
            screen=screen,
            coordenada=(x, y),
            imagen=imagen,
            mapa=mapa,
            nombre="food",
            bonus=20)

        return pocion

    def onFactoryPuertaMadera(self, screen, mapa):

        rutaImagen = EnumImage.PUERTA_MADERA.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        x = random.randrange(0, self.MAPA_ANCHO, self.PIXELES)
        y = random.randrange(0, self.MAPA_ALTO, self.PIXELES)

        puertaMadera = Item(
            screen=screen,
            coordenada=(x, y),
            imagen=imagen,
            mapa=mapa,
            nombre="Puerta de Madera",
            bonus=0)

        return puertaMadera

    def onFactoryOgroMago(self, screen, mapa, dungeonLevel):

        rutaImagen = EnumImage.OGRO_MAGO.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        x = random.randrange(0, self.MAPA_ANCHO, self.PIXELES)
        y = random.randrange(0, self.MAPA_ALTO, self.PIXELES)

        ogroMago = Monster(
            screen=screen,
            coordenada=(x, y),
            imagen=imagen,
            mapa=mapa,
            dungeon_level=dungeonLevel)

        return ogroMago

    def onFactoryMummy(self, screen, mapa, dungeonLevel):

        rutaImagen = EnumImage.MUMMY.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        x = random.randrange(0, self.MAPA_ANCHO, self.PIXELES)
        y = random.randrange(0, self.MAPA_ALTO, self.PIXELES)

        mummy = Monster(
            screen=screen,
            coordenada=(x, y),
            imagen=imagen,
            mapa=mapa,
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
            coordenada=(x, y),
            imagen=imagen,
            mapa=mapa,
            dungeon_level=dungeonLevel)

        return jugador
