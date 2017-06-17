#!/usr/bin/env python
# coding=utf-8

import pygame

from pygame import Surface
from Source.Enum.EnumImage import EnumImage
from Source.Enum.Constantes import Constantes
from Source.GameMundo.Tile import Tile

class FactoryTiles:

    def onFactoryMuroLadrilloNegroIndestructible(self, screen: Surface, x: int, y: int):

        rutaImagen = EnumImage.MURO_LADRILLO_NEGRO.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        tile = Tile(transitable=False,
                    digable=False,
                    coordenada=(y * 16, x * 16),
                    screen=screen,
                    imagen=imagen)

        return tile

    def onFactoryMuroLadrilloNegro(self, screen, x, y):

        rutaImagen = EnumImage.MURO_LADRILLO_NEGRO.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        tile = Tile(transitable=False,
                    digable=True,
                    coordenada=(y * 16, x * 16),
                    screen=screen,
                    imagen=imagen)

        return tile

    def onFactorySueloFertil(self, screen, x, y):

        rutaImagen = EnumImage.SUELO_FERTIL.value
        imagen = pygame.image.load(rutaImagen).convert_alpha()

        tile = Tile(transitable=True,
                    digable=True,
                    coordenada=(y * 16, x * 16),
                    screen=screen,
                    imagen=imagen)

        return tile