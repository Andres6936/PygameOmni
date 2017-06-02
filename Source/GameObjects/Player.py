#!/usr/bin/env python
# coding=utf-8

import pygame

from Source.GameObjects.GameObject import MovableCharacter
from Source.GameObjects.GameObject import PIXELES

class Player( MovableCharacter ):
    """Class for playable character"""

    def __init__(self, screen, posicion, object_image, object_cave, dungeon_level):
        """
        Constructor
        send all parameters to super-class MovableCharacter
        """
        super(Player, self).__init__(screen, posicion, object_image, object_cave, dungeon_level)
        self.vitalidad = 150    # Vitalidad.
        self.defensa = 3        # Defensa reduce el daño recibido.
        self.attackPower = 10   # Attackpower increases damage done


    def handleKey(self, event, monsterList):
        """Handle the key-event when the user press down arrows. If it is a legal move, it move the player in that direction which user pressed (Arrows-keys)
        """
        if event.key == pygame.K_LEFT:
            if self.checkValidMove(self.getYposition(), (self.getXposition()-PIXELES), monsterList, None):
                self.Mover(-PIXELES, 0)

        elif event.key == pygame.K_RIGHT:
            if self.checkValidMove(self.getYposition(), (self.getXposition()+PIXELES), monsterList, None):
                self.Mover(PIXELES, 0)

        elif event.key == pygame.K_UP:
            if self.checkValidMove((self.getYposition()-PIXELES), self.getXposition(), monsterList, None):
                self.Mover(0, -PIXELES)

        elif event.key == pygame.K_DOWN:
            if self.checkValidMove((self.getYposition()+PIXELES), self.getXposition(), monsterList, None):
                self.Mover(0, PIXELES)