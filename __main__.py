#!/usr/bin/env python
# coding=utf-8
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

"""
Este archivo es el inicializador de la App.
"""

import pygame
from Source.GameScreens.GameStart import GameStart
from Source.GameScreens.GameMenu import GameMenu

# Constants for the playable field. Must be dividable with 16 (tile size in pixels)
SCREEN_ALTO: int = 512
SCREEN_ANCHO:  int = 1024

if __name__ == '__main__':

    # Creamos el objecto principal de la App.
    App = GameStart(SCREEN_ANCHO, SCREEN_ALTO)

    font = pygame.font.match_font("Ubuntu Mono")
    Menu = GameMenu(App, "My Game", ["Jugar", "Opciones", "Salir"], fuente=font, fuente_size=40 )
    Menu.run()

    # Iniciamos la App.
    App.OnInitGame(SCREEN_ANCHO, SCREEN_ALTO)
