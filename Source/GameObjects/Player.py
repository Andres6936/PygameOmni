#!/usr/bin/env python
# coding=utf-8

import pygame
from pygame import Surface

from Core.Utilidades.Punto import Punto
from Source.GameObjects.GameObject import GameObject


class Player( GameObject ):
    """
    Clase para el caracter Jugador.
    """

    # CONSTRUCTOR
    def __init__(self, screen: Surface, coordenada: Punto, imagen: object, mapa: object, dungeon_level: int):
        """
        Constructor de Clase.
        Envia todos los parametros a la super-class GameObjects.
        """
        super(Player, self).__init__(screen, coordenada, imagen, mapa)

        self.__vitalidad: int = 150   # Vitalidad.
        self.__defensa: int = 3       # Defensa reduce el daño recibido.
        self.__ataqueFisico: int = 10 # Attackpower increases damage done

    # MÉTODOS

    def getVitalidad(self) -> int:
        """
        Metodo que devuelve la vitalidad del Jugador.
        @rtype: int
        @return: Valor de la vitalidad del Jugador.
        """
        return self.__vitalidad

    def getDefensa(self) -> int:
        """
        Metodo que devuelve la defensa del Jugador.
        @rtype: int
        @return: Valor de la defensa del Jugador.
        """
        return self.__defensa

    def getAtaqueFisico(self) -> int:
        """
        Método que devuelve el valor del ataque fisico del Jugador.
        @rtype: int
        @return: Valor del ataque fisico del jugador.
        """
        return self.__ataqueFisico

    def incrementarVitalidad(self, cantidad: int) -> None:
        """
        Metodo que incrementa la vitalidad del Jugador, se suma el valor pasado por parametro.
        @param cantidad : Valor que se suma a la vitalidad del Jugador.
        @type cantidad: int
        """
        self.__vitalidad += cantidad

    def incrementarDefensa(self, cantidad: int) -> None:
        """
        Metodo que incrementa la defensa del Jugador, se suma el valor pasado por parametro.
        @param cantidad : Valor que se suma a la defensa del Jugador.
        @type cantidad: int
        """
        self.__defensa += cantidad

    def incrementarAtaqueFisico(self, cantidad: int) -> None:
        """
        Incrementa el ataque fisico del Jugador, se suma el valor pasado por parametro.
        @param cantidad: Valor que se suma al ataque fisico del Jugador.
        @type cantidad: int
        """
        self.__ataqueFisico += cantidad

    def disminuirVitalidad(self, cantidad: int) -> None:
        """
        Disminuye la vitalidad del Jugador de acuerdo a la cantidad pasada por parametro.
        @param cantidad: Valor en que se disminuye la vitalidad del Jugador.
        @type cantidad: int
        """

        # ¿La vitalidad del Jugador se encuentra por debajo de cero (0).?
        if (self.__vitalidad - cantidad) <= 0:
            self.__vitalidad = 0
        else:
            self.__vitalidad -= cantidad

    def isMovimientoValido(self, destino: Punto, monsterList: list) -> bool:
        """
        Método que verifica si el movimiento a realizar es válido.
        @return: True si el movimiento a realizar es válido, False en caso contrario.
        @rtype: bool
        """

        for m in monsterList:
            if m.getCoordenadaX() is destino.getCoordenadaX() and m.getCoordenadaY() is destino.getCoordenadaY():
                return False

        return self.mapa[destino.getCoordenadaY()][destino.getCoordenadaX()].isTransitable()

    def handleKey(self, event, monsterList):
        """
        Handle the key-event when the user press down arrows. If it is a legal move, it move the player in that direction which user pressed (Arrows-keys)
        """

        # Si el jugador presiona la tecla [Izquierda]
        if event.key == pygame.K_LEFT:
            if self.isMovimientoValido(Punto(self.getCoordenadaX() - 1, (self.getCoordenadaY())), monsterList):
                self.mover(-1, 0)

        # Si el jugador presiona la tecla [Derecha]
        elif event.key == pygame.K_RIGHT:
            if self.isMovimientoValido(Punto(self.getCoordenadaX() + 1, (self.getCoordenadaY())), monsterList):
                self.mover( 1, 0)

        # Si el jugador presiona la tecla [Arriba]
        elif event.key == pygame.K_UP:
            if self.isMovimientoValido(Punto((self.getCoordenadaX()), self.getCoordenadaY() - 1), monsterList):
                self.mover(0, -1)

        # Si el jugador presiona la tecla [Abajo]
        elif event.key == pygame.K_DOWN:
            if self.isMovimientoValido(Punto((self.getCoordenadaX()), self.getCoordenadaY() + 1), monsterList):
                self.mover(0,  1)