#!/usr/bin/env python
# coding=utf-8

import random

from pygame import Surface
from Source.Core.Punto import Punto
from Source.GameObjects.GameObject import GameObject
from Source.GameObjects.Player import Player

class Monster( GameObject ):
    """A class for monsters/enemies"""

    def __init__(self, screen: Surface, coordenada: Punto, imagen: object, mapa: object, dungeon_level: int):
        """Constructor
           Send all parameters to super-class MovableCharacter
        """
        super(Monster, self).__init__(screen, coordenada, imagen, mapa)

        self.direction = self.DIRECTION[random.randint(0, len(self.DIRECTION)-1)]
        self.__vitalidad = 25 + (dungeon_level * 4) # Vitalidad.
        self.__defensa = 2 + (dungeon_level * 2)    # Defensa reduce el daño recibido.
        self.__ataqueFisico = 6 + (dungeon_level * 2)  #Attackpower increases damage done

    def getVitalidad(self) -> int:
        """
        Metodo que devuelve la vitalidad del Enemigo.
        @return: Valor de la vitalidad del Enemigo.
        @rtype: int
        """
        return self.__vitalidad

    def getDefensa(self) -> int:
        """
        Metodo que devuelve la defensa del Enemigo.
        @return: Valor de la defensa del Enemigo.
        @rtype: int
        """
        return self.__defensa

    def getAtaqueFisico(self) -> int:
        """
        Método que devuelve el valor del ataque fisico del Enemigo.
        @return: Valor del ataque fisico del Enemigo.
        @rtype: int
        """
        return self.__ataqueFisico

    def incrementarVitalidad(self, cantidad: int) -> None:
        """
        Metodo que incrementa la vitalidad del Enemigo, se suma el valor pasado por parametro a la vitalidad.
        @param cantidad : Valor que se suma a la vitalidad del Enemigo.
        @type cantidad: int
        """
        self.__vitalidad += cantidad

    def incrementarDefensa(self, cantidad: int) -> None:
        """
        Metodo que incrementa la defensa del Enemigo, se suma el valor pasado por parametro.
        @param cantidad : Valor que se suma a la defensa del Enemigo.
        @type cantidad: int
        """
        self.__defensa += cantidad

    def incrementarAtaqueFisico(self, cantidad: int) -> None:
        """
        Increase el valor del ataque fisico del Enemigo, se suma el valor pasado por parametro.
        @param cantidad: Valor que se suma al ataque fisico del Enemigo.
        @type cantidad: int
        """
        self.__ataqueFisico += cantidad

    def disminuirVitalidad(self, cantidad: int) -> None:
        """
        Disminuye la vitalidad del Enemigo de acuerdo al valor pasado por párametro.
        @param cantidad: Valor en el que se disminuye la vitalidad del Enemigo.
        @type cantidad: int
        """

        # ¿La vitalidad del Enemigo se encuentra por debajo de cero.?
        if (self.__vitalidad - cantidad) <= 0:
            self.__vitalidad = 0
        else:
            self.__vitalidad -= cantidad

    def isMovimientoValido(self, puntoDistinto: Punto, monsterList: list, player: Player) -> bool:
        """
        Método que verifica si el movimiento a realizar es válido.
        @return: True si el movimiento a realizar es válido, False en caso contrario.
        @rtype: bool
        """

        for m in monsterList:
            if m.coordenada.isIgual(puntoDistinto):
                return False

        if player is not None and player.coordenada.isIgual(puntoDistinto):
            return False

        return self.mapa[puntoDistinto.getCoordenadaX()][puntoDistinto.getCoordenadaY()].isTransitable()

    def walk(self, monsterList: list, player: Player):
        """Move a monster in a random direction, if it hit a wall or another monster, we choose a new random direction
        """
        if self.direction == 'L':
            if self.isMovimientoValido(Punto(self.coordenada.getCoordenadaY(), (self.coordenada.getCoordenadaX() - 1)), monsterList, player):
                self.mover(-1, 0)
            else:
                self.direction = self.DIRECTION[random.randint(0, len(self.DIRECTION)-1)]

        elif self.direction == 'R':
            if self.isMovimientoValido(Punto(self.coordenada.getCoordenadaY(), (self.coordenada.getCoordenadaX() + 1)), monsterList, player):
                self.mover(1, 0)
            else:
                self.direction = self.DIRECTION[random.randint(0, len(self.DIRECTION)-1)]

        elif self.direction == 'U':
            if self.isMovimientoValido(Punto((self.coordenada.getCoordenadaY() - 1), self.coordenada.getCoordenadaX()), monsterList, player):
                self.mover(0, -1)
            else:
                self.direction = self.DIRECTION[random.randint(0, len(self.DIRECTION)-1)]

        elif self.direction == 'D':
            if self.isMovimientoValido(Punto((self.coordenada.getCoordenadaY() + 1), self.coordenada.getCoordenadaX()), monsterList, player):
                self.mover(0, 1)
            else:
                self.direction = self.DIRECTION[random.randint(0, len(self.DIRECTION)-1)]


    def encontrarJugador(self, player: Player, monsterList: list):
        """Find out if a player is in range for a monster, if a player is in range of max 5 tiles. The monster move towards the player to attack it
           @return: 1 if the player is in range
           @return: -1 if the player is not in range
        """

        #Find out how far the player is
        costFromMonsterToPlayer = (abs(self.getCoordenadaX() - player.getCoordenadaX()) + abs(self.getCoordenadaY() - player.getCoordenadaY()))

        #Move towards the player if the player is in rage
        if costFromMonsterToPlayer <= 5:

            #Are the player to the left or to the rigt of the monster
            if self.getCoordenadaX() > player.getCoordenadaX():
                dirX = -1
            elif self.getCoordenadaX() < player.getCoordenadaX():
                dirX = 1
            else:
                dirX = 0

            #Are the player to the left  or to the rigt of the monster
            if self.getCoordenadaY() > player.getCoordenadaY():
                dirY = -1
            elif self.getCoordenadaY() < player.getCoordenadaY():
                dirY = 1
            else:
                dirY = 0

            #Can we move to the new position?
            if self.isMovimientoValido(Punto(self.getCoordenadaY(), self.getCoordenadaX() + dirX), monsterList, player):
                    self.mover(dirX, 0)
                    return 1
            elif self.isMovimientoValido(Punto(self.getCoordenadaY() + dirY, self.getCoordenadaX()), monsterList, player):
                    self.mover(0, dirY)
                    return 1
        else:
             return -1