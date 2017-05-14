#!/usr/bin/env python
# coding=utf-8

from GameObject import GameObject

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
        self.itemName = nombre
        self.itemValue = valor

    def getPosition(self):
        """Get the position in tuple
           @return: tuple of x and y coordinate (in pixels)
        """
        return (self.getXposition(), self.getYposition())

    def useItem(self):
        """If a item is picked up
           @return: The value of that item
        """
        return self.itemValue

    def getItemName(self):
        """Get the name of the item
           @return: name of the item
        """
        return self.itemName