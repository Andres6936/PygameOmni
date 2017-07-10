#!/usr/bin/env python
# coding=utf-8

import random

import pygame

from Core.Utilidades.Punto import Punto
from Source.Enum.Constantes import Constantes
from Source.Enum.EnumImage import EnumImage
from Source.Enum.Tag import Tag
from Source.GameObjects.Item import Item
from Source.GameObjects.Monster import Monster
from Source.GameObjects.Player import Player


class Factory:
    """
    Clase que se encarga de generar y fabricar los objectos y entidades.
    """

    # ATRIBUTOS

    PIXELES: int = Constantes.PIXELES.value
    """
    Obtenemos el valor de la constante PIXELES.
    """

    MAPA_ANCHO: int = Constantes.MAPA_ANCHO.value
    """
    Ancho total del mapa en pixeles.
    """

    MAPA_ALTO: int = Constantes.MAPA_ALTO.value
    """
    Alto total del mapa en pixeles.
    """

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

        MAX_ENEMIGOS_NIVEL: int = Constantes.MAXIMO_ENEMIGOS_NIVEL.value

        for i in range( MAX_ENEMIGOS_NIVEL ):
            monsters.append(Monster(
                screen,
                coordenada= Punto(random.randrange(0, self.MAPA_ANCHO), random.randrange(0, self.MAPA_ALTO)),
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

        MAX_ARMADURA_NIVEL = Constantes.MAXIMO_ARMADURA_NIVEL.value
        MAX_ESPADA_NIVEL = Constantes.MAXIMO_ESPADA_NIVEL.value
        MAX_POCION_NIVEL = Constantes.MAXIMO_POCION_NIVEL.value

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

        x = random.randrange(0, self.MAPA_ANCHO)
        y = random.randrange(0, self.MAPA_ALTO)

        armadura = Item(
            screen=screen,
            coordenada=Punto(x, y),
            imagen=imagen,
            mapa=mapa,
            tag=Tag.ARMADURA.value,
            nombre="armor",
            bonus=1
        )

        return armadura

    def onFactoryEspada(self, screen, mapa):

        rutaImagen = EnumImage.ESPADA.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        x = random.randrange(0, self.MAPA_ANCHO)
        y = random.randrange(0, self.MAPA_ALTO)

        espada = Item(
            screen=screen,
            coordenada=Punto(x, y),
            imagen=imagen,
            mapa=mapa,
            tag=Tag.ARMAS.value,
            nombre="weapon",
            bonus=1)

        return espada

    def onFactoryPocion(self, screen, mapa):

        rutaImagen = EnumImage.POCION.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        x = random.randrange(0, self.MAPA_ANCHO)
        y = random.randrange(0, self.MAPA_ALTO)

        pocion = Item(
            screen=screen,
            coordenada=Punto(x, y),
            imagen=imagen,
            mapa=mapa,
            tag=Tag.POCION.value,
            nombre="food",
            bonus=20)

        return pocion

    def onFactoryPuertaMadera(self, screen, mapa):

        rutaImagen = EnumImage.PUERTA_MADERA.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        x = random.randrange(0, self.MAPA_ANCHO)
        y = random.randrange(0, self.MAPA_ALTO)

        puertaMadera = Item(
            screen=screen,
            coordenada=Punto(x, y),
            imagen=imagen,
            mapa=mapa,
            tag=Tag.PUERTA.value,
            nombre="Puerta de Madera",
            bonus=0)

        return puertaMadera

    def onFactoryOgroMago(self, screen, mapa, dungeonLevel):

        rutaImagen = EnumImage.OGRO_MAGO.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        x = random.randrange(0, self.MAPA_ANCHO)
        y = random.randrange(0, self.MAPA_ALTO)

        ogroMago = Monster(
            screen=screen,
            coordenada=Punto(x, y),
            imagen=imagen,
            mapa=mapa,
            dungeon_level=dungeonLevel)

        return ogroMago

    def onFactoryMummy(self, screen, mapa, dungeonLevel):

        rutaImagen = EnumImage.MUMMY.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        x = random.randrange(0, self.MAPA_ANCHO)
        y = random.randrange(0, self.MAPA_ALTO)

        mummy = Monster(
            screen=screen,
            coordenada=Punto(x, y),
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

        x = random.randrange(0, self.MAPA_ANCHO)
        y = random.randrange(0, self.MAPA_ALTO)

        jugador = Player(
            screen=screen,
            coordenada=Punto(x, y),
            imagen=imagen,
            mapa=mapa,
            dungeon_level=dungeonLevel)

        return jugador
