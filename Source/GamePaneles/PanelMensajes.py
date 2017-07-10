#!/usr/bin/env python
# coding=utf-8

from pygame import Rect
from pygame import Surface
from pygame import font

from Core.Utilidades.Color import Color
from Source.Enum.Constantes import Constantes


class PanelMensajes:
    """
    Clase PanelMensajes.
    """

    # CONSTANTES
    PANEL_MENSAJES_ALTO: int = 64
    """
    Alto en pixeles del Panel Mensajes.
    """

    PANEL_MENSAJES_ANCHO: int = 512
    """
    Ancho en pixeles del Panel Mensajes.
    """

    PANEL_MENSAJES_COOR_X: int = 0
    """
    Coordenada en X del Rectángulo.
    """

    PANEL_MENSAJES_COOR_Y: int = Constantes.SCREEN_ALTO.value
    """
    Coordenada en Y del Rectángulo.
    """

    # ATRIBUTOS
    screenApp: Surface = None
    """
    Ventana principal de la App.
    """

    fuenteTexto: font = None
    """
    Fuente del texto.
    """

    superficieRect: Rect = None
    """
    Superficie para dibujar texto.
    """


    # CONSTRCUTOR
    def __init__(self, screen: Surface):
        """
        Constructor de la Clase.
        Configuramos la ventana principal, fuente y la superficie.
        """

        global screenApp
        global fuenteTexto
        global superficieRect

        # Configuramos la screen principal de la App.
        screenApp = screen

        # Configuramos la fuente de texto.
        fuenteTexto = PanelMensajes.configurarFuente()

        # Configuramos el Rectángulo.
        superficieRect = PanelMensajes.configurarRect(self.PANEL_MENSAJES_COOR_X, self.PANEL_MENSAJES_COOR_Y, self.PANEL_MENSAJES_ANCHO, self.PANEL_MENSAJES_ALTO)

        # Rellenamos el panel con un color de fondo por defecto.
        screenApp.fill(Color.CARBON, superficieRect)

    @staticmethod
    def configurarFuente() -> font:
        """
        Configura y devuelve la fuente del texto.
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
    def mostrarMensaje(mensaje: str) -> None:
        """
        Muestra el mensaje del parametro directamente en el panel.
        @param mensaje: El mensaje.
        @type mensaje: str
        """

        global screenApp
        global fuenteTexto
        global superficieRect

        # Renderizamos el mensaje.
        message = fuenteTexto.render(mensaje, True, Color.ORANGE_RED)

        # Rellenamos el panel, borrando rastros anteriores.
        screenApp.fill(Color.CARBON, superficieRect)

        # Dibujamos el panel.
        screenApp.blit(message, superficieRect)
