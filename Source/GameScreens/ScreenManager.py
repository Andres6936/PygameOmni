# -*- coding: utf-8 -*-

"""
   This is the file where all the magic happens. It contains methods for setting up
   and running the game, aswell as creating different game objects.
"""

import pygame

from Source.Enum.Constantes import Constantes
from Source.GameScreens.IScreen import IScreen
from Source.GameScreens.NextScene import NextScene
from Source.GameScreens.ScreenInGame import ScreenInGame
from Source.GameScreens.ScreenMenu import ScreenMenu


class ScreenManager:
    STATS_BOX_WIDTH: int = 200
    MESSAGE_BOX_HEIGHT: int = 64
    PIXELES: int = Constantes.PIXELES.value

    def __init__(self, SCREEN_ANCHO: int, SCREEN_ALTO: int):
        pygame.init()
        font = pygame.font.match_font("Ubuntu Mono")

        self.isRunning: bool = True
        self.screenWidth: int = SCREEN_ANCHO
        self.screenHeight: int = SCREEN_ALTO

        # Creamos la ventana principal de la App.
        self.screen = pygame.display.set_mode(
            (SCREEN_ANCHO + self.STATS_BOX_WIDTH,
             SCREEN_ALTO + self.MESSAGE_BOX_HEIGHT), 0, 32)

        # Le damos un titulo a la ventana.
        pygame.display.set_caption("Experimental 0.0.6 Estable")

        # Lazy loading of screen
        self.screenInGame: IScreen | None = None
        self.screenMenu: IScreen = ScreenMenu(
            self,"My Game", ["Jugar", "Opciones", "Salir"],
            fuente=font, fuente_size=40)
        # Reference the first scene in the start of app
        self.currentScene: IScreen = self.screenMenu

    def __del__(self):
        # Call pygame.quit when the lifetime of object is over,
        # also called destructor.
        pygame.quit()

    def IsRunning(self) -> bool:
        return self.isRunning

    def Clear(self):
        self.currentScene.Clear()

    def Draw(self):
        self.currentScene.Draw()

    def Update(self):
        nextScene = self.currentScene.Update()
        if nextScene == NextScene.EXIT:
            self.isRunning = False
        elif nextScene == NextScene.IN_GAME:
            self.screenInGame = ScreenInGame(self)
            # Reference the new scene
            self.currentScene = self.screenInGame

    def Surface(self):
        return self.screen

    def ScreenWidth(self):
        return self.screenWidth

    def ScreenHeight(self):
        return self.screenHeight

    def DibujarTexto(self, texto, size, x, y, center=True):
        fuenteName = pygame.font.SysFont("arial", 30)
        textoSurface = fuenteName.render(texto, True, (255, 255, 255))
        textoRect = textoSurface.get_rect()
        if center:
            textoRect.midtop = (x, y)
        else:
            textoRect.topleft = (x, y)
        return self.screen.blit(textoSurface, textoRect)
