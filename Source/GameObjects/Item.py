#!/usr/bin/env python
# coding=utf-8

from Source.GameObjects.GameObject import GameObject

class Item( GameObject ):
    """
    Clase para los Items.
    """

    def __init__(self, screen, coordenada, imagen, mapa, nombre, bonus):
        """
        Constructor
        Send all parameter except name and value to super-class GameObject
        """
        super(Item, self).__init__(screen, coordenada, imagen, mapa)

        self.itemNombre = nombre
        self.itemBonus = bonus

    def getCoordenada(self):
        """
        Get the position in tuple
        @return: tuple of x and y coordinate (in pixels)
        """
        return (self.getCoordenadaX(), self.getCoordenadaY())

    def getNombre(self):
        """
        Metodo que devuelve el nombre del Item.
        @return: Nombre del Item.
        """
        return self.itemNombre

    def usarBonusItem(self):
        """
        Si el Item es recogido.
        @return: El valor de bonus del Item.
        """
        return self.itemBonus