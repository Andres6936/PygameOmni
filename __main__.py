#!/usr/bin/env python
# coding=utf-8
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

"""
Este archivo es el inicializador de la App.
"""

from Source.Main import Main

# Constants for the playable field. Must be dividable with 16 (tile size in pixels)
MAPA_ALTURA: int = 512
MAPA_ANCHO:  int = 1024

if __name__ == '__main__':

    # Creamos el objecto principal de la App.
    App = Main()

    # Iniciamos la App.
    App.OnInitGame( MAPA_ANCHO, MAPA_ALTURA )
