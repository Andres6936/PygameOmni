#!/usr/bin/env python
# coding=utf-8

from pygame import Surface
from Source.GameObjects.GameObject import GameObject
from Source.Enum.Tag import Tag
from Source.Core.Punto import Punto

class Item( GameObject ):
    """
    Clase para los Items.
    """

    def __init__(self, screen: Surface, coordenada: Punto, imagen: object, mapa: object, tag: Tag, nombre: str, bonus: int):
        """
        Constructor
        Send all parameter except name and value to super-class GameObject
        """
        super(Item, self).__init__(screen, coordenada, imagen, mapa)

        self.__tag: Tag = tag
        self.__itemNombre: str = nombre
        self.__itemBonus: int = bonus

    def getTag(self) -> Tag:
        """
        Devuelve la Tag del enemigo.
        @return: Tag del enemigo
        @rtype: str
        """
        return self.__tag

    def getNombre(self) -> str:
        """
        Metodo que devuelve el nombre del Item.
        @return: Nombre del Item.
        @rtype: str
        """
        return self.__itemNombre

    def usarBonusItem(self) -> int:
        """
        Si el Item es recogido.
        @return: El valor de bonus del Item.
        @rtype: int
        """
        return self.__itemBonus