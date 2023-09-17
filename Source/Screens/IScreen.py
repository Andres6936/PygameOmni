#!/usr/bin/env python
# coding=utf-8
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

from abc import ABC, abstractmethod

from Source.Screens.NextScene import NextScene


class IScreen(ABC):
    @abstractmethod
    def Update(self) -> NextScene:
        pass

    @abstractmethod
    def Draw(self):
        pass

    @abstractmethod
    def Clear(self):
        pass
