#!/usr/bin/env python
# coding=utf-8
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import sys

import pygame

from GUI.Boton import Boton


class GameMenu:

    def __init__(self, app, titulo, items, bg_color=(0, 0, 0), bg_imagen=None,
                 fuente=None, fuente_size=30, color=(255, 255, 255), hcolor=(255, 0, 0),
                 padding=40):

        self.app = app
        self.bg_imagen = bg_imagen
        self.titulo = titulo
        self.ancho = self.app.screen.get_width()
        self.alto = self.app.screen.get_height()
        self.bg_color = bg_color
        self.color = color
        self.hcolor = hcolor
        self.items = []
        self.cur_item = None
        self.mouse_visible = True
        self.padding = padding
        self.clock = pygame.time.Clock()

        for indice, item in enumerate(items):
            menu_item = Boton(item, fuente, self.padding)
            total_height = len(items) * menu_item.alto
            posX = int(self.ancho / 2) - int(menu_item.ancho / 2)
            posY = int(self.alto / 2) - int(total_height / 2) + ((indice * 2) + indice * menu_item.alto) + 50
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
        if self.items[self.cur_item].texto == "Salir":
            pygame.quit()
            sys.exit()
        elif self.items[self.cur_item].texto == "Jugar":
            self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(30)
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
            self.app.screen.fill((0, 0, 0))
            if self.bg_imagen:
                self.app.screen.blit(self.bg_imagen, (0, 0))

            if type(self.titulo) is str:
                self.app.DibujarTexto(self.titulo, 40, self.app.screen.get_width() / 2, 40)

            for item in self.items:
                if self.mouse_visible:
                    self.setMouseHover(item)
                self.app.screen.blit(item.label, item.posXY)
            pygame.display.flip()