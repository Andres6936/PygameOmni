# -*- coding: utf-8 -*-

"""
Roguelike cave generator using cellular automata.
Based on the algorithm in the article found here:
http://roguebasin.roguelikedevelopment.org/index.php/Cellular_Automata_Method_for_Generating_Random_Cave-Like_Levels
"""

import pygame
import random

from pygame import Surface
from Source.GameMundo.FactoryTiles import FactoryTiles
from Source.Enum.Constantes import Constantes

class Mazmorra:

    # CONSTANTES
    MAPA_ALTO: int = Constantes.MAPA_ALTO.value
    """
    Alto del mapa.
    """

    MAPA_ANCHO: int = Constantes.MAPA_ANCHO.value
    """
    Ancho del mapa.
    """

    PIXELES: int = Constantes.PIXELES.value
    """
    Alto y ancho de una imagen en pixeles.
    """

    # Constants for the cave map generator
    # These settings can be changed to generate different kinds of maps.
    # Try changing these to see the different results
    # Standard settings (6, 5, 0, 40)
    ITERATIONS: int = 6
    WALLFACTOR: int = 5  # CA rule one
    WALLFACTOR2: int = 0  # CA rule two
    FILLFACTOR: int = 40  # 45% of the tiles will initially be ground tiles

    WALL_TILE = 'Graficas/Ikoner/Tiles/Muros/wall_16.png'
    GROUND_TILE = 'Graficas/Ikoner/Tiles/Suelos/ground3_16.png'

    # ATRIBUTOS
    screen: Surface = None
    """
    Interfaz principal de la App.
    """

    factoryTiles: FactoryTiles = None
    """
    Instanciamos la clase FactoryTiles para crear los distintos Tiles de la App.
    """

    # CONSTRUCTOR
    def __init__(self):
        """
        Constructor de la clase.
        """

        global factoryTiles
        global screen

        screen = None
        factoryTiles = FactoryTiles()

        print("Constructor Mazmorra")

    # MÉTODOS

    def InitMazmorra(self, screen: Surface):
        """
        Load map tiles, make a call to generate and return the cave represented by a 2D list of Tile objects
        @return the generated cave
        """

        wall_image = pygame.image.load(self.WALL_TILE).convert_alpha()
        ground_image = pygame.image.load(self.GROUND_TILE).convert_alpha()

        # This can take a couple of seconds to make
        return self.GenerarMazmorra(wall_image, ground_image, screen)

    def GenerarMazmorraVacia(self) -> list:
        """
        Genera una matriz vacia que será la representacion de nuestro mapa.
        @return: Matriz vacia que representa nuestro mapa.
        """

        # Matriz vacia.
        mazmorra: list = [[None for y in range(0, self.MAPA_ANCHO)] for x in range(0, self.MAPA_ALTO)]

        return mazmorra

    def GenerarMazmorra(self, wall_image, ground_image, screen):
        """
        Generate the mazmorra using cellular automata. The rules are as follows:
        If a tile has at least WALLFACTOR adjacent walls, make it a wall.
        If a tile has WALLFACTOR2 adjacent wall tiles, make it a wall
        All other tiles are ground tiles
        The mazmorra generator can take a few seconds to complete, depending on map size.
        A problem with this generator is that the mazmorra can be disconnected.
        With the current settings, most the caves generated seems ok
        @param wall_image: image for wall tiles
        @param ground_image: image for ground tiles
        @param screen: the game screen to draw on
        @return: the generated mazmorra
        """

        # The cavemap is a 2D list of tile objects
        mazmorra: list = self.GenerarMazmorraVacia()

        # Init mazmorra. The mazmorra edges are wall tiles, the rest are random
        for x in range(0, self.MAPA_ALTO):
            for y in range(0, self.MAPA_ANCHO):
                # Make walls around border
                if y == 0 or x == 0 or x == self.MAPA_ALTO - 1 or y == self.MAPA_ANCHO - 1:
                    mazmorra[x][y] = FactoryTiles().onFactoryMuroLadrilloNegroIndestructible(screen, x, y)
                # Make ground tile
                elif random.randint(0, 100) > self.FILLFACTOR:
                    mazmorra[x][y] = FactoryTiles().onFactorySueloFertil(screen, x, y)
                # Make wall tile
                else:
                    mazmorra[x][y] = FactoryTiles().onFactoryMuroLadrilloNegro(screen, x, y)

        # Iteratively build the mazmorra
        for iteration in range(self.ITERATIONS):

            # lists of tiles to be updated
            tilesToWall = []
            tilesToGround = []

            for x in range(0, self.MAPA_ALTO):
                for y in range(0, self.MAPA_ANCHO):

                    # Dont do anything to border walls
                    if y == 0 or x == 0 or x == self.MAPA_ALTO - 1 or y == self.MAPA_ANCHO - 1:
                        continue

                    # Calculate number of adjacent wall tiles
                    adjacentWalls = self.CalcularCercaniaConMuros(mazmorra[x][y], mazmorra)
                    if adjacentWalls >= self.WALLFACTOR or adjacentWalls == self.WALLFACTOR2:
                        tilesToWall.append(mazmorra[x][y])
                    else:
                        tilesToGround.append(mazmorra[x][y])

            # Update tiles
            for tile in tilesToWall:
                tile.actualizarTile(False, wall_image)
            for tile in tilesToGround:
                tile.actualizarTile(True, ground_image)

        return mazmorra

    def CalcularCercaniaConMuros(self, tile, mazmorra):
        """
        Calcular cercania con muros.
        Calcula el número de muros adyacentes.
        """
        numwalls = 0

        """Loop through the 8 adjacent tiles surrounding"""
        for y in range(-1, 2 * 1):
            for x in range(-1, 2 * 1):

                # skip self
                if y == 0 and y == x:
                    continue
                if not mazmorra[int(tile.getCoordenadaY() / 16) + y][int(tile.getCoordenadaX() / 16) + x].isTransitable():
                    numwalls += 1

        return numwalls

    def actualizarMazmorra(self, screen, cave, direction, xpos, ypos):
        """Update the cave if a user wants to dig down a wall
           @param screen: the screen to draw on
           @param cave: the cave to change
           @param direction: dig direction
           @param xpos: xcord to the tile to update
           @param ypos: ycord to the tile to update
           """

        ground_image = pygame.image.load(self.GROUND_TILE).convert_alpha()

        if direction == 'D' and cave[int(ypos / 16) + 1][int(xpos / 16)].isDigable():  # Dig down
            cave[int(ypos / 16) + 1][int(xpos / 16)].actualizarTile(True, ground_image)

        elif direction == 'U' and cave[int(ypos / 16) - 1][int(xpos / 16)].isDigable():  # Dig up
            cave[int(ypos / 16) - 1][int(xpos / 16)].actualizarTile(True, ground_image)

        elif direction == 'L' and cave[int(ypos / 16)][int(xpos / 16) - 1].isDigable():  # Dig up
            cave[int(ypos / 16)][int(xpos / 16) - 1].actualizarTile(True, ground_image)

        elif direction == 'R' and cave[int(ypos / 16)][int(xpos / 16) + 1].isDigable():  # Dig up
            cave[int(ypos / 16)][int(xpos / 16) + 1].actualizarTile(True, ground_image)