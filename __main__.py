#!/usr/bin/env python
# coding=utf-8
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

from Source.GameScreens.GameStart import GameStart

# Constants for the playable field. Must be dividable with 16 (tile size in pixels)
SCREEN_ALTO: int = 512
SCREEN_ANCHO:  int = 1024

if __name__ == '__main__':
    sceneManager = GameStart(SCREEN_ANCHO, SCREEN_ALTO)
    while sceneManager.isRunning:
        sceneManager.Clear()
        sceneManager.Update()
        sceneManager.Draw()
