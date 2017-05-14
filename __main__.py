# -*- coding: utf-8 -*-

"""
Este archivo es el inicializar de la App.
"""

from Source import Main

# Constants for the playable field. Must be dividable with 16 (tile size in pixels)
MAPA_ALTURA = 512
MAPA_ANCHO = 1024

if __name__ == '__main__':

    Main.OnInitGame ( MAPA_ANCHO, MAPA_ALTURA )
