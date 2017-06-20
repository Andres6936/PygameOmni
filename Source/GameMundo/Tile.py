#!/usr/bin/env python
# coding=utf-8

from pygame import Surface

class Tile:
    """
    This class is for wall and ground tile objects.
    """

    # CONSTRUCTOR
    def __init__(self, transitable: bool, digable: bool, coordenada: tuple, screen: Surface, imagen: object):
        """
        Constructor de la clase Tile.
        @param transitable: True si el Tile es transitable, False en caso contrario.
        @param digable: true if tile is digable, false if not
        @param coordenada: tuple representing this tiles position in pixels
        @param screen: the screen to draw on
        @param imagen: La imagen del Tile.
        """
        self.transitable: bool = transitable
        self.digable: bool = digable
        self.coordenada: tuple = coordenada
        self.screen: Surface = screen
        self.imagen: object = imagen

    # MÉTODOS

    def dibujar(self):
        """Draw the tile image on the screen"""
        self.screen.blit(self.imagen, self.coordenada)

    def isTransitable(self) -> bool:
        """
        Check if this tile is passable or not
        @return: True si el Tile es transitable, False en caso contrario.
        """
        return self.transitable

    def isDigable(self) -> bool:
        """
        Check if this tile is digable
        @return: true if this tile is digable, false if not
        """
        return self.digable

    def actualizarTile(self, transitable: bool, nuevaImagen: object) -> None:
        """
        Update the tile
        @param transitable: new passable value
        @param nuevaImagen: new tile image
        """
        self.transitable = transitable
        self.imagen = nuevaImagen

    def getCoordenadaX(self) -> int:
        """Get the tiles x-cord
           @return: x-cord of tile
        """
        return self.coordenada[0]

    def getCoordenadaY(self) -> int:
        """Get the tiles y-cord
           @return: y-cord of tile
        """
        return self.coordenada[1]