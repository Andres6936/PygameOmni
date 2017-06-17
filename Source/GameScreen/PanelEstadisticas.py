# -*- coding: utf-8 -*-
"""
    This file contains methods for drawing the rectangle areas displaying the stats and game messages.
"""

from pygame import Rect
from pygame import Surface
from pygame import font

from Core.Color import Color
from Source.GameObjects.Player import Player


class PanelEstadisticas():

    @staticmethod
    def OnInitStatBox(screen: Surface, player: Player, dungeon_level: int, box_x_start: int, box_heigth: int, box_width: int) -> None:
        """
        Create the box displaying the stats
        @param screen: the screen to draw on
        @type screen: SurfaceType
        @param player: the player object
        @type player: Player
        @param dungeon_level: the current dungeon level
        @type dungeon_level: int
        @param box_x_start: rectangle upper left corner x-coordinate
        @type box_x_start: int
        @param box_heigth: height of rectangle
        @type box_heigth: int
        @param box_width: width of rectangle
        @type box_width: int
        """

        # Configuramos la fuente de texto.
        fuente = PanelEstadisticas().configurarFuente()

        #create the rectangle
        stats_box = Rect(box_x_start, 0, box_width, box_heigth)

        # Llamamos los métodos correspondientes para obtener la info. del Jugador.
        vitalidad: str = PanelEstadisticas().getEstadisticaVitalidad(player)
        ataque_fisico: str = PanelEstadisticas().getEstadisticaAtaqueFisico(player)
        defensa: str = PanelEstadisticas().getEstadisticaDefensa(player)

        #render game info
        mostrar_vitalidad = fuente.render("Vitalidad: {0}".format(vitalidad), True, Color.ROJO)
        mostrar_ataque_fisico = fuente.render("Ataque Fisico: {0}".format(ataque_fisico), True, Color.BLANCO)
        mostrar_defensa = fuente.render("Defensa: {0}".format(defensa), True, Color.BLANCO)
        mostrar_nivel_mazmorra = fuente.render("Nivel Mazmorra: {0}".format(str(dungeon_level)), True, Color.VERDE)

        #For each line of text, draw it on the screen and move the rectangle for the next line
        screen.fill(Color.NEGRO, stats_box)
        screen.blit(mostrar_vitalidad, stats_box)
        screen.blit(mostrar_ataque_fisico, stats_box.move(0, mostrar_vitalidad.get_height()))
        screen.blit(mostrar_defensa, stats_box.move(0, mostrar_vitalidad.get_height() + mostrar_ataque_fisico.get_height()))
        screen.blit(mostrar_nivel_mazmorra, stats_box.move(0, mostrar_vitalidad.get_height() + mostrar_ataque_fisico.get_height() + mostrar_defensa.get_height()))

    def configurarFuente(self):
        """
        Configura la fuente del texto.
        @return: Fuente
        @rtype: FontType
        """
        return font.SysFont(name='arial', size=20)

    def getEstadisticaVitalidad(self, player) -> str:
        """
        Método que devuelve la vitalidad del Jugador.
        @param player: El Jugador.
        @return: String(str) que representa la vitalidad del Jugador.
        @rtype: str
        """
        return str(player.getVitalidad())

    def getEstadisticaAtaqueFisico(self, player) -> str:
        """
        Método que devuelve el ataque fisico del Jugador.
        @param player: El Jugador
        @return: String(str) que representa el ataque fisico del Jugador.
        @rtype: str
        """
        return str(player.getAtaqueFisico())

    def getEstadisticaDefensa(self, player) -> str:
        """
        Método que devuelve la defensa del Jugador.
        @param player: El Jugador
        @return: String(str) que representa la defensa del Jugador.
        @rtype: str
        """
        return str(player.getDefensa())