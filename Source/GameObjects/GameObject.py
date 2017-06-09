# -*- coding: utf-8 -*-

import random

from pygame.sprite import Sprite
from Source.Enum.EnumConstantes import EnumConstantes


class GameObject( Sprite ):
    """
    Un clase generica que contiene los metodos de los diferentes objectos del juego.
    """

    # CONSTANTES DE CLASE
    PIXELES: int = EnumConstantes.PIXELES.value  # width and height of a tile
    DIRECTION: list = ['L', 'R', 'D', 'U']  # Left, right, down, up

    # CONSTRUCTOR DE LA CLASE
    def __init__(self, screen: object, coordenada: tuple, imagen: object, mapa: object):
        """ 
        Constructor
        @param screen: the screen to draw on
        @param coordenada: La posicion del objecto representado por una tupla de dos valores (x, y).
        @param imagen: La imagen del objecto.
        @param mapa: El mapa.
        """
        self.screen = screen
        self.imagen = imagen
        self.mapa = mapa
        self.coordenada = self.legalStartPosition(coordenada[0], coordenada[1])

    # MÉTODOS

    def update(self, mapa, coordenada):
        """
        Actualiza el Objecto de juego.
        @param mapa: El mapa.
        @param coordenada: Una tupla de dos valores (x, y) que contiene la nueva posicion del Objecto.
        """
        self.mapa = mapa
        self.coordenada = self.legalStartPosition(coordenada[0], coordenada[1])

    def dibujar(self):
        """
        Metodo para el objecto en la pantalla.
        """
        self.screen.blit(self.imagen, self.coordenada)

    def getCoordenadaX(self) -> int:
        """
        Metodo que devuelve la posicion en el eje x del Tile (en Pixeles).
        @rtype: int
        @return: La coordenada x (en pixeles).
        """
        return self.coordenada[0]

    def getCoordenadaY(self) -> int:
        """
        Metodo que devuelve la posicion en el eje y del Tile (en Pixeles).
        @rtype: int
        @return: La coordenada y (en pixeles).
        """
        return self.coordenada[1]

    def getCoordenada(self) -> tuple:
        """
        Metodo que devuelve la posicion de un objecto en una tupla de dos valores (x, y).
        @rtype: tuple (int, int)
        @return: Tupla de dos valores (x, y) donde x representa el eje x & donde y representa el eje y. (en pixeles).
        """
        return (self.getCoordenadaX(), self.getCoordenadaY())

    def legalStartPosition(self, x: int, y: int):
        """
        Revisa si la posicion pasada por parámetro es válidad para una posicion inicial.
        Funcion recursiva.
        @param x: Coordenada en el eje X.
        @param y: Coordenada en el eje Y.
        @type x: int
        @type y: int
        @return: Devuelve una tupla (x: int, y: int) cuando está es válidad como una posicion inicial.
        @return: call legalStartPosition-method again if it wasn't legal to start in that position
        """

        #Is this tile a wall, True if not, False if it is a wall
        if self.mapa[ int(y/self.PIXELES)][ int(x/self.PIXELES)].isTransitable():
            return (x, y)
        else:
            return self.legalStartPosition(random.randrange(0, len(self.mapa[0]) * self.PIXELES, self.PIXELES),
                                           random.randrange(0, len(self.mapa) * self.PIXELES, self.PIXELES))

class MovableCharacter( GameObject ):
    """Class for movable objects"""

    def __init__(self, screen, coordenada, imagen, mapa, dungeon_level):
        """Constructor
           send all parameters to super-class GameObject
        """
        super(MovableCharacter, self).__init__(screen, coordenada, imagen, mapa)


    def Mover( self, x, y ):
        """
        Metodo que cambia la posicion de los Enemigos y el Jugador para moverlos alrededor.
        @param x : Coordenada en el eje x.
        @param y : Coordenada en el eje y.
        """
        self.coordenada = ((self.getCoordenadaX() + x), (self.getCoordenadaY() + y))

    def getVitalidad(self) -> int:
        """
        Metodo que devuelve la vitalidad del Jugador o Enemigo.
        @return: Valor de la vitalidad del Jugador o Enemigo.
        """
        return self.vitalidad

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
        self.vitalidad += cantidad

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
        if (self.vitalidad - amount) <= 0:
            self.vitalidad = 0
        else:
            self.vitalidad -= amount

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


class Monster( MovableCharacter ):
    """A class for monsters/enemies"""

    def __init__(self, screen, coordenada, imagen, mapa, dungeon_level):
        """Constructor
           Send all parameters to super-class MovableCharacter
        """
        super(Monster, self).__init__(screen, coordenada, imagen, mapa, dungeon_level)

        self.direction = self.DIRECTION[random.randint(0, len(self.DIRECTION)-1)]
        self.vitalidad = 25 + (dungeon_level * 4) # Vitalidad.
        self.defensa = 2 + (dungeon_level * 2)    # Defensa reduce el daño recibido.
        self.attackPower = 6 + (dungeon_level*2)  #Attackpower increases damage done

    def walk(self, monsterList, player):
        """Move a monster in a random direction, if it hit a wall or another monster, we choose a new random direction
        """
        if self.direction == 'L':
            if self.checkValidMove(self.getCoordenadaY(), (self.getCoordenadaX() -self.PIXELES), monsterList, player):
                self.Mover(-self.PIXELES, 0)
            else:
                self.direction = self.DIRECTION[random.randint(0, len(self.DIRECTION)-1)]

        elif self.direction == 'R':
            if self.checkValidMove(self.getCoordenadaY(), (self.getCoordenadaX() + self.PIXELES), monsterList, player):
                self.Mover(self.PIXELES, 0)
            else:
                self.direction = self.DIRECTION[random.randint(0, len(self.DIRECTION)-1)]

        elif self.direction == 'U':
            if self.checkValidMove((self.getCoordenadaY() -self.PIXELES), self.getCoordenadaX(), monsterList, player):
                self.Mover(0, -self.PIXELES)
            else:
                self.direction = self.DIRECTION[random.randint(0, len(self.DIRECTION)-1)]

        elif self.direction == 'D':
            if self.checkValidMove((self.getCoordenadaY() +self.PIXELES), self.getCoordenadaX(), monsterList, player):
                self.Mover(0, self.PIXELES)
            else:
                self.direction = self.DIRECTION[random.randint(0, len(self.DIRECTION)-1)]


    def findPlayer(self, player, monsterList):
        """Find out if a player is in range for a monster, if a player is in range of max 5 tiles. The monster move towards the player to attack it
           @return: 1 if the player is in range
           @return: -1 if the player is not in range
        """

        #Find out how far the player is
        costFromMonsterToPlayer = (abs((self.getCoordenadaX() / self.PIXELES) - (player.getCoordenadaX() / self.PIXELES)) + abs((self.getCoordenadaY() / self.PIXELES) - (player.getCoordenadaY() / self.PIXELES)))

        #Move towards the player if the player is in rage
        if costFromMonsterToPlayer <= 5:

            #Are the player to the left or to the rigt of the monster
            if self.getCoordenadaX() > player.getCoordenadaX():
                dirX = -self.PIXELES
            elif self.getCoordenadaX() < player.getCoordenadaX():
                dirX = self.PIXELES
            else:
                dirX = 0

            #Are the player to the left  or to the rigt of the monster
            if self.getCoordenadaY() > player.getCoordenadaY():
                dirY = -self.PIXELES
            elif self.getCoordenadaY() < player.getCoordenadaY():
                dirY = self.PIXELES
            else:
                dirY = 0

            #Can we move to the new position?
            if self.checkValidMove(self.getCoordenadaY(), self.getCoordenadaX() + dirX, monsterList, player):
                    self.Mover(dirX, 0)
                    return 1
            elif self.checkValidMove(self.getCoordenadaY() + dirY, self.getCoordenadaX(), monsterList, player):
                    self.Mover(0, dirY)
                    return 1
        else:
             return -1