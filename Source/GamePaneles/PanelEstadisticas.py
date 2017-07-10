# -*- coding: utf-8 -*-
"""
    This file contains methods for drawing the rectangle areas displaying the stats and game messages.
"""

from pygame import Rect
from pygame import font

from Core.Utilidades.Color import Color
from Enum.Constantes import Constantes
from Source.GameObjects.Player import Player


class PanelEstadisticas:
    """
    Clase PanelEstadisticas.
    """

    # CONSTANTES
    PANEL_ESTADISTICAS_ALTO: int = Constantes.SCREEN_ALTO.value
    """
    Alto en pixeles del Panel Estadisticas.
    """

    PANEL_ESTADISTICAS_ANCHO: int = 200
    """
    Ancho en pixeles del Panel Estadisticas.
    """

    PANEL_ESTADISTICAS_COOR_X: int = Constantes.SCREEN_ANCHO.value
    """
    Coordenada en X del Rectángulo.
    """

    PANEL_ESTADISTICAS_COOR_Y: int = 0
    """
    Coordenada en Y del Rectángulo.
    """

    # ATRIBUTOS
    screenApp = None
    """
    Ventana principal de la App.
    """

    fuenteTexto = None
    """
    Fuente del texto.
    """

    superficieRect = None
    """
    Superficie para dibujar texto.
    """


    # CONSTRUCTOR
    def __init__(self, screen):
        """
        Constructor de la clase.
        """

        global screenApp
        global fuenteTexto
        global superficieRect

        # Configuramos la screen principal de la App.
        screenApp = screen

        # Configuramos la fuente de texto.
        fuenteTexto = PanelEstadisticas.configurarFuente()

        # Configuramos el Rectángulo.
        superficieRect = PanelEstadisticas.configurarRect(self.PANEL_ESTADISTICAS_COOR_X, self.PANEL_ESTADISTICAS_COOR_Y, self.PANEL_ESTADISTICAS_ANCHO, self.PANEL_ESTADISTICAS_ALTO)

        # Rellenamos el panel con un color de fondo por defecto.
        screenApp.fill(Color.CARBON, superficieRect)

    @staticmethod
    def configurarFuente() -> font:
        """
        Configura la fuente del texto.
        @return: Fuente
        @rtype: FontType
        """
        return font.SysFont(name='arial', size=20)

    @staticmethod
    def configurarRect(panelCoorX: int, panelCoorY: int, panelAncho: int, panelAlto: int) -> Rect:
        """
        Configura y devuelve un Rectángulo como una superficie para dibujar texto.
        @param panelCoorX: Coordenada en X del Rectángulo.
        @type panelCoorX: int
        @param panelCoorY: Coordenada en Y del Rectángulo.
        @type panelCoorY: int
        @param panelAncho: Ancho del Rectángulo.
        @type panelAncho: int
        @param panelAlto: Alto del Rectángulo.
        @type panelAlto: int
        @return: Rectángulo que se usara como superficie para dibujar texto.
        @rtype: RectType
        """
        return Rect(panelCoorX, panelCoorY, panelAncho, panelAlto)

    @staticmethod
    def mostrarEstadisticas(player: Player, nivelMazmorra: int):

        global screenApp
        global fuenteTexto
        global superficieRect

        # Llamamos los métodos correspondientes para obtener la info. del Jugador.
        vitalidad: str = PanelEstadisticas.getEstadisticaVitalidad(player)
        ataque_fisico: str = PanelEstadisticas.getEstadisticaAtaqueFisico(player)
        defensa: str = PanelEstadisticas.getEstadisticaDefensa(player)

        mostrar_vitalidad = fuenteTexto.render("Vitalidad: {0}".format(vitalidad), True, Color.ROJO)
        mostrar_ataque_fisico = fuenteTexto.render("Ataque Fisico: {0}".format(ataque_fisico), True, Color.BLANCO)
        mostrar_defensa = fuenteTexto.render("Defensa: {0}".format(defensa), True, Color.BLANCO)
        mostrar_nivel_mazmorra = fuenteTexto.render("Nivel Mazmorra: {0}".format(str(nivelMazmorra)), True, Color.VERDE)

        screenApp.fill(Color.CARBON, superficieRect)
        screenApp.blit(mostrar_vitalidad, superficieRect)
        screenApp.blit(mostrar_ataque_fisico, superficieRect.move(0, mostrar_vitalidad.get_height()))
        screenApp.blit(mostrar_defensa, superficieRect.move(0, mostrar_vitalidad.get_height() + mostrar_ataque_fisico.get_height()))
        screenApp.blit(mostrar_nivel_mazmorra, superficieRect.move(0, mostrar_vitalidad.get_height() + mostrar_ataque_fisico.get_height() + mostrar_defensa.get_height()))

    @staticmethod
    def getEstadisticaVitalidad(player) -> str:
        """
        Método que devuelve la vitalidad del Jugador.
        @param player: El Jugador.
        @return: String(str) que representa la vitalidad del Jugador.
        @rtype: str
        """
        return str(player.getVitalidad())

    @staticmethod
    def getEstadisticaAtaqueFisico(player) -> str:
        """
        Método que devuelve el ataque fisico del Jugador.
        @param player: El Jugador
        @return: String(str) que representa el ataque fisico del Jugador.
        @rtype: str
        """
        return str(player.getAtaqueFisico())

    @staticmethod
    def getEstadisticaDefensa(player) -> str:
        """
        Método que devuelve la defensa del Jugador.
        @param player: El Jugador
        @return: String(str) que representa la defensa del Jugador.
        @rtype: str
        """
        return str(player.getDefensa())