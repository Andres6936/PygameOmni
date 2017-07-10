#!/usr/bin/env python
# coding=utf-8
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

# Importancion de modulos

import pygame

from Core.Utilidades.Color import Color
from pygame.font import Font

class Boton:

    def __init__(self, texto: str = None, funcion: object = None, padding: int = 0):

        self.texto: str = texto
        self.fuente: Font = pygame.font.SysFont("arial", 30)
        self.fuente_size: int = 30

        self.funcion: object = None

        self.color: Color = Color.BLANCO

        self.label = self.fuente.render(self.texto, True, self.color)
        self.rect = self.label.get_rect()
        self.rect.inflate_ip(0, padding)

        self.ancho: int = self.rect.width
        self.alto: int = self.rect.height
        self.size: tuple = (self.ancho, self.alto)

        self.posX: int = 0
        self.posY: int = 0
        self.posXY: tuple = (0, 0)

    def setPosicionXY(self, x: int, y: int) -> None:
        self.posXY = (x, y)
        self.posX = x
        self.posY = y

    def setColor(self, nColor) -> None:
        self.color = nColor
        self.label = self.fuente.render(self.texto, True, self.color)

    def isSeleccionadoMouse(self):
        posMouseX, posMouseY = pygame.mouse.get_pos()
        if (self.posX <= posMouseX <= self.posX + self.ancho) and \
            (self.posY <= posMouseY <= self.posY + self.alto):
            return True
        return False