#!/usr/bin/env python
# coding=utf-8

import pygame

from Source.GameObjects.GameObject import GameObject

class Player( GameObject ):
    """
    Clase para el caracter jugable.
    """

    # CONSTRUCTOR

    def __init__(self, screen, coordenada, imagen, mapa, dungeon_level):
        """
        Constructor
        send all parameters to super-class MovableCharacter
        """
        super(Player, self).__init__(screen, coordenada, imagen, mapa)

        self._vitalidad = 150    # Vitalidad.
        self.defensa = 3        # Defensa reduce el daño recibido.
        self.attackPower = 10   # Attackpower increases damage done

    # MÉTODOS

    def getVitalidad(self) -> int:
        """
        Metodo que devuelve la vitalidad del Jugador o Enemigo.
        @return: Valor de la vitalidad del Jugador o Enemigo.
        """
        return self._vitalidad

    def getDefensa(self) -> int:
        """
        Metodo que devuelve la defensa del Jugador o Enemigo.
        @return: Valor de la defensa del Jugador o Enemigo.
        """
        return self.defensa

    def getAttackPower(self):
        """Get attack power
           @return: Value of attack power for monster or player
        """
        return self.attackPower

    def incrementarVitalidad(self, cantidad):
        """
        Metodo que incrementa la vitalidad del Enemigo o Jugador, se suma el valor pasado por parametro.
        @param cantidad : Valor int que se suma a la vitalidad del Enemigo o Jugador.
        """
        self._vitalidad += cantidad

    def incrementarDefensa(self, cantidad):
        """
        Metodo que incrementa la defensa del Enemigo o Jugador, se suma el valor pasado por parametro.
        @param cantidad : Valor int que se suma a la defensa del Enemigo o Jugador.
        """
        self.defensa += cantidad

    def increaseAP(self, amount):
        """
        Increase attack power with value of amount
        """
        self.attackPower += amount

    def decreaseHP(self, amount):
        """Decrease hit power with amount, hitpower can't go lower than 0
        """

        #Does hitpoints get under 0?
        if (self._vitalidad - amount) <= 0:
            self._vitalidad = 0
        else:
            self._vitalidad -= amount

    def Mover( self, x, y ):
        """
        Metodo que cambia la posicion de los Enemigos y el Jugador para moverlos alrededor.
        @param x : Coordenada en el eje x.
        @param y : Coordenada en el eje y.
        """
        self.coordenada = ((self.getCoordenadaX() + x), (self.getCoordenadaY() + y))

    def checkValidMove(self, y, x, monsterList, player):
        """Check if a move is legal
           @return: False, if it is a monster, player or a wall in postion x and y
           @return: True, if it is a legal move
        """

        for m in monsterList:
            if (m.getCoordenadaX() == x) and (m.getCoordenadaY() == y):
                return False

        if player is not None and ((player.getCoordenadaX() == x) and player.getCoordenadaY() == y):
            return False

        return self.mapa[int(y / self.PIXELES)][int(x / self.PIXELES)].isTransitable()

    def handleKey(self, event, monsterList):
        """Handle the key-event when the user press down arrows. If it is a legal move, it move the player in that direction which user pressed (Arrows-keys)
        """
        if event.key == pygame.K_LEFT:
            if self.checkValidMove(self.getCoordenadaY(), (self.getCoordenadaX() - self.PIXELES), monsterList, None):
                self.Mover(-self.PIXELES, 0)

        elif event.key == pygame.K_RIGHT:
            if self.checkValidMove(self.getCoordenadaY(), (self.getCoordenadaX() + self.PIXELES), monsterList, None):
                self.Mover(self.PIXELES, 0)

        elif event.key == pygame.K_UP:
            if self.checkValidMove((self.getCoordenadaY() - self.PIXELES), self.getCoordenadaX(), monsterList, None):
                self.Mover(0, - self.PIXELES)

        elif event.key == pygame.K_DOWN:
            if self.checkValidMove((self.getCoordenadaY() + self.PIXELES), self.getCoordenadaX(), monsterList, None):
                self.Mover(0, self.PIXELES)