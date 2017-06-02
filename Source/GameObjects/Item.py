#!/usr/bin/env python
# coding=utf-8

from Source.GameObjects.GameObject import GameObject

class Item( GameObject ):
    """
    Clase para los Items.
    """

    def __init__(self, screen, posicion, object_image, object_cave, nombre, valor):
        """
        Constructor
        Send all parameter except name and value to super-class GameObject
        """
        super(Item, self).__init__(screen, posicion, object_image, object_cave)
        self.itemNombre = nombre
        self.itemValor = valor

    def getPosition(self):
        """Get the position in tuple
           @return: tuple of x and y coordinate (in pixels)
        """
        return (self.getXposition(), self.getYposition())

    def UsarItem(self):
        """If a item is picked up
           @return: The value of that item
        """
        return self.itemValor

    def GetItemNombre(self):
        """
        Metodo que devuelve el nombre del Item.
        @return: Nombre del Item.
        """
        return self.itemNombre