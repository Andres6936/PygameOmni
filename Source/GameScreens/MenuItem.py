#!/usr/bin/env python
# coding=utf-8
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

# Importancion de modulos

import pygame
from pygame.font import Font

class MenuItem(Font):

    def __init__(self, texto, fuente, fuente_size=30, color=(255, 255, 255), padding=0):

        Font.__init__(self, fuente, fuente_size)

        self.texto = texto
        self.fuente_size = fuente_size
        self.color = color
        self.label = self.render(self.texto, True, self.color)
        self.rect = self.label.get_rect()
        self.rect.inflate_ip(0, padding)
        self.ancho = self.rect.width
        self.alto = self.rect.height
        self.size = (self.ancho, self.alto)
        self.posX = 0
        self.posY = 0
        self.posXY = (0, 0)

    def setPosicionXY(self, x, y):
        self.posXY = (x, y)
        self.posX = x
        self.posY = y

    def setColor(self, nColor):
        self.color = nColor
        self.label = self.render(self.texto, True, self.color)

    def isSeleccionadoMouse(self):
        posMouseX, posMouseY = pygame.mouse.get_pos()
        if (self.posX <= posMouseX <= self.posX + self.ancho) and \
            (self.posY <= posMouseY <= self.posY + self.alto):
            return True
        return False