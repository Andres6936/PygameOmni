# -*- coding: utf-8 -*-

"""
Roguelike cave generator using cellular automata.
Based on the algorithm in the article found here:
http://roguebasin.roguelikedevelopment.org/index.php/Cellular_Automata_Method_for_Generating_Random_Cave-Like_Levels
"""

import pygame
import random

from Source.GameMundo.Tile import Tile
from Source.Enum.EnumConstantes import EnumConstantes

PIXELES: int = EnumConstantes.PIXELES.value

# Constants for the cave map generator
# These settings can be changed to generate different kinds of maps.
# Try changing these to see the different results
# Standard settings (6, 5, 0, 40)
ITERATIONS = 6
WALLFACTOR = 5  # CA rule one
WALLFACTOR2 = 0  # CA rule two
FILLFACTOR = 40  # 45% of the tiles will initially be ground tiles

WALL_TILE = 'Graficas/Ikoner/Tiles/Muros/wall_16.png'
GROUND_TILE = 'Graficas/Ikoner/Tiles/Suelos/ground3_16.png'


def calculateNearbyWalls(tile, cave):
    """Calculate number of adjacent walls
       @param cave: the map
       @return: number of adjacent walls
    """

    numwalls = 0

    """Loop through the 8 adjacent tiles surrounding"""
    for y in range(-1, 2 * 1):
        for x in range(-1, 2 * 1):

            # skip self
            if y == 0 and y == x:
                continue
            if not cave[int(tile.getCoordenadaY() / 16) + y][int(tile.getCoordenadaX() / 16) + x].isTransitable():
                numwalls += 1

    return numwalls


def generate(MAPA_ANCHO: int, MAPA_ALTO: int, wall_image, ground_image, screen):
    """Generate the cave using cellular automata. The rules are as follows:
       If a tile has at least WALLFACTOR adjacent walls, make it a wall.
       If a tile has WALLFACTOR2 adjacent wall tiles, make it a wall
       All other tiles are ground tiles
       The cave generator can take a few seconds to complete, depending on map size.
       A problem with this generator is that the cave can be disconnected.
       With the current settings, most the caves generated seems ok
       @param MAPA_ANCHO: map width
       @param MAPA_ALTO: map height
       @param wall_image: image for wall tiles
       @param ground_image: image for ground tiles
       @param screen: the game screen to draw on
       @return: the generated cave
       """

    # The cavemap is a 2D list of tile objects
    cave = [[None for x in range(0, MAPA_ANCHO, PIXELES)] for y in range(0, MAPA_ALTO, PIXELES)]

    # Init cave. The cave edges are wall tiles, the rest are random
    for y in range(0, int(MAPA_ALTO / PIXELES)):
        for x in range(0, int(MAPA_ANCHO / PIXELES)):
            # Make walls around border
            if x == 0 or y == 0 or y == (MAPA_ALTO / PIXELES) - 1 or x == (MAPA_ANCHO / PIXELES) - 1:
                cave[y][x] = Tile(transitable=False, digable=False, coordenada=(x * 16, y * 16), screen=screen,
                                  imagen=wall_image)
            # Make ground tile
            elif random.randint(0, 100) > FILLFACTOR:
                cave[y][x] = Tile(transitable=True, digable=True, coordenada=(x * 16, y * 16), screen=screen,
                                  imagen=ground_image)
            # Make wall tile
            else:
                cave[y][x] = Tile(transitable=False, digable=True, coordenada=(x * 16, y * 16), screen=screen,
                                  imagen=wall_image)

    # Iteratively build the cave
    for iteration in range(ITERATIONS):

        # lists of tiles to be updated
        tilesToWall = []
        tilesToGround = []

        for y in range(0, int(MAPA_ALTO / 16)):
            for x in range(0, int(MAPA_ANCHO / 16)):

                # Dont do anything to border walls
                if x == 0 or y == 0 or y == (MAPA_ALTO / 16) - 1 or x == (MAPA_ANCHO / 16) - 1:
                    continue

                # Calculate number of adjacent wall tiles
                adjacentWalls = calculateNearbyWalls(cave[y][x], cave)
                if adjacentWalls >= WALLFACTOR or adjacentWalls == WALLFACTOR2:
                    tilesToWall.append(cave[y][x])
                else:
                    tilesToGround.append(cave[y][x])

        # Update tiles
        for tile in tilesToWall:
            tile.updateTile(False, wall_image)
        for tile in tilesToGround:
            tile.updateTile(True, ground_image)

    return cave


def run_mapgen(MAPA_ANCHO: int, MAPA_ALTO: int, screen):
    """Load map tiles, make a call to generate and return the cave represented by a 2D list of Tile objects
       @param MAPA_ANCHO: the map width in pixels
       @param MAPA_ALTO: the map height in pixels
       @return the generated cave
    """

    wall_image = pygame.image.load(WALL_TILE).convert_alpha()
    ground_image = pygame.image.load(GROUND_TILE).convert_alpha()

    # This can take a couple of seconds to make
    return generate(MAPA_ANCHO, MAPA_ALTO, wall_image, ground_image, screen)


def updateCave(screen, cave, direction, xpos, ypos):
    """Update the cave if a user wants to dig down a wall
       @param screen: the screen to draw on
       @param cave: the cave to change
       @param direction: dig direction
       @param xpos: xcord to the tile to update
       @param ypos: ycord to the tile to update
       """

    ground_image = pygame.image.load(GROUND_TILE).convert_alpha()

    if direction == 'D' and cave[int(ypos / 16) + 1][int(xpos / 16)].isDigable():  # Dig down
        cave[int(ypos / 16) + 1][int(xpos / 16)].updateTile(True, ground_image)

    elif direction == 'U' and cave[int(ypos / 16) - 1][int(xpos / 16)].isDigable():  # Dig up
        cave[int(ypos / 16) - 1][int(xpos / 16)].updateTile(True, ground_image)

    elif direction == 'L' and cave[int(ypos / 16)][int(xpos / 16) - 1].isDigable():  # Dig up
        cave[int(ypos / 16)][int(xpos / 16) - 1].updateTile(True, ground_image)

    elif direction == 'R' and cave[int(ypos / 16)][int(xpos / 16) + 1].isDigable():  # Dig up
        cave[int(ypos / 16)][int(xpos / 16) + 1].updateTile(True, ground_image)
