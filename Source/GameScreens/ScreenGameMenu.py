#!/usr/bin/env python
# coding=utf-8
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import pygame
import sys

from Source.GameScreens.MenuItem import MenuItem

class GameMenu:

    def __init__(self, juego, titulo, items, bg_color=(0, 0, 0), bg_imagen=None,
                 fuente=None, fuente_size=30, color=(255, 255, 255), hcolor=(255, 0, 0),
                 padding=40):

        self.juego = juego
        self.bg_imagen = bg_imagen
        self.titulo = titulo
        self.ancho = self.game.screen.get_width()
        self.alto = self.game.screen.get_height()
        self.bg_color = bg_color
        self.color = color
        self.hcolor = hcolor
        self.items = []
        self.cur_item = None
        self.mouse_visible = True
        self.padding = padding

        for indice, item in enumerate(items):
            menu_item = MenuItem(item, fuente, fuente_size, color, self.padding)
            total_height = len(items) * menu_item.alto
            posX = (self.ancho / 2) - (menu_item.ancho / 2)
            posY = (self.alto / 2) - (total_height / 2) + ((indice * 2) + indice * menu_item.alto) + 50
            menu_item.setPosicionXY(posX, posY)
            self.items.append(menu_item)

    def setMouseHover(self, item):
        # Resaltamos el item que se encuentra sobre el mouse.
        if item.isSeleccionadoMouse():
            item.setColor(self.hcolor)
            self.cur_item = self.items.index(item)
        else:
            item.setColor(self.color)

    def setKeyBSeleccionado(self, key):
        # Resaltamos el item del menu que ha sido seleccionado por tecla.
        for item in self.items:
            item.setColor(self.color)

        if self.cur_item is None:
            self.cur_item = 0
        else:
            if key == pygame.K_RETURN:
                self.go()
            elif key == pygame.K_UP:
                self.cur_item -= 1
            elif key == pygame.K_DOWN:
                self.cur_item += 1

            self.cur_item = self.cur_item % len(self.items)

        self.items[self.cur_item].setColor(self.hcolor)

    def go(self):
        # Ejecutamos la acción del item seleccionado.
        if self.cur_item is None:
            return
        if self.items[self.cur_item].text == "Salir":
            pygame.quit()
            sys.exit()
        elif self.items[self.cur_item].text == "Jugar":
            self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.game.clock.tick(30)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif evento.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_RETURN]:
                        self.mouse_visible = False
                        self.setKeyBSeleccionado(evento.key)
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    for item in self.items:
                        if item.isSeleccionadoMouse():
                            self.go()

            if pygame.mouse.get_rel() != (0, 0):
                self.mouse_visible = True
                self.cur_item = None

            pygame.mouse.set_visible(self.mouse_visible)
            self.game.screen.fill((0, 0, 0))
            if self.bg_imagen:
                self.game.screen.blit(self.bg_imagen, (0, 0))

            if type(self.titulo) is str:
                self.game.draw_text(self.titulo, 40, self.game.screen.get_width() / 2, 40)

            for item in self.items:
                if self.mouse_visible:
                    self.setMouseHover(item)
                self.game.screen.blit(item.label, item.posXY)
            pygame.display.flip()