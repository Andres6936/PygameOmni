# -*- coding: utf-8 -*-

"""
   This is the file where all the magic happens. It contains methods for setting up
   and running the game, aswell as creating different game objects.
"""

import random
import sys
import time
import pygame

from pygame import Surface
from Source.Core.Punto import Punto
from Source.GameObjects.Player import Player
from Source.Enum.Constantes import Constantes
from Source.Enum.EnumImage import EnumImage
from Source.Enum.Tag import Tag
from Source.GameScreen.PanelEstadisticas import PanelEstadisticas
from Source.GameScreen.PanelMensajes import PanelMensajes
from Source.GameSystemBatalla import SystemBattle
from Source.GameMundo.MapRender import MapRender
from Source.GameMundo.Mazmorra import Mazmorra
from Source.GameMundo.FactoryEntidades import Factory

# CONSTANTES DE LA APP
STATS_BOX_WIDTH:    int = 200
STATS_BOX_OFFSET:   int = 10
MESSAGE_BOX_HEIGHT: int = 64

PIXELES: int = Constantes.PIXELES.value

# ATRIBUTOS DE LA APP
dungeonLevel: int = 1 #dungeon level starts at 1

# Iniciamos los paneles.
panelMensajes: PanelMensajes = None
panelEstadisticas: PanelEstadisticas = None

def OnInitGame(SCREEN_ANCHO: int, SCREEN_ALTO: int) -> None:
    """
    Inicializa y configura el juego al iniciar la App.
    @param SCREEN_ANCHO: the map(playable area) width
    @type SCREEN_ANCHO: int
    @param SCREEN_ALTO: the map(playable area) height
    @type SCREEN_ALTO: int
    """

    global dungeonLevel

    # Inicializamos los modulos de Pygame.
    pygame.init()

    #Get a screen object to draw on
    #Total screen size is MAP_WIDTH + 265 (stats box) and MAP_HEIGHT + 128 (message box)
    screen = pygame.display.set_mode((SCREEN_ANCHO + STATS_BOX_WIDTH, SCREEN_ALTO + MESSAGE_BOX_HEIGHT), 0, 32)

    pygame.display.set_caption("INF3331 Roguelike Project")

    # Create the first cave. This can take a couple of seconds to make
    cave = Mazmorra().InitMazmorra(screen)

    #load monster images
    monster_images = [
        EnumImage.CUCARACHA_GIGANTE.value,
        EnumImage.GUSANO_CEREBRO.value,
        EnumImage.MUMMY.value,
        EnumImage.OGRO_MAGO.value,
        EnumImage.DRAGON_ROJO.value
    ]

    monster_tiles = [pygame.image.load(img).convert_alpha() for img in monster_images]

    #create player object
    player = Factory().onFactoryJugador(screen, cave, dungeonLevel)

    #Run game
    OnRunGame(screen, cave, player, monster_tiles, SCREEN_ALTO, SCREEN_ANCHO)

def removeMonster(monsters):
    """Remove dead monsters from the monster list
       @param monsters: list of monsters
    """

    for m in monsters:
        if m.getVitalidad() <= 0:
            monsters.remove(m)

def OnRunGame(screen: Surface, cave: object, player: Player, monster_tiles: list, SCREEN_ALTO: int, SCREEN_ANCHO: int):
    """
    Run the game and the contains the main game loop
    @param screen: the game screen to draw
    @type screen: SurfaceType
    @param cave: the map
    @type cave: object
    @param player: the player object
    @type player: Player
    @param monster_tiles: monster images
    @type monster_tiles: list
    @param SCREEN_ALTO: the map heith (playable area) in pixels
    @type SCREEN_ALTO: int
    @param SCREEN_ANCHO: the map width (playable area) in pixels
    @type SCREEN_ANCHO: int
    """

    global dungeonLevel
    global panelMensajes
    global panelEstadisticas

    # Inicializamos los paneles.
    panelMensajes = PanelMensajes(screen)
    panelEstadisticas = PanelEstadisticas(screen)

    #Make list of monsters
    monsters = Factory().OnFactoryMonsters(screen, cave, monster_tiles, dungeonLevel)
    items = Factory().OnFactoryItems(screen, cave)

    #get clock so we can control frames per second
    clock = pygame.time.Clock()
    gameMessage: str = ""

    #Main game loop - should probably be refactored (if time)
    while True:

        clock.tick(5) #Limit the screen to 5 FPS

        #go through events
        for event in pygame.event.get():

            #player clicked close button
            if event.type == pygame.QUIT:
                OnExitApp()

            #a key has been pressed
            if event.type == pygame.KEYDOWN:

                #move player
                player.handleKey(event, monsters)
                gameMessage = monsterMoveAndAttack(monsters, player, screen, SCREEN_ALTO, SCREEN_ANCHO, MESSAGE_BOX_HEIGHT)

                if event.key == pygame.K_s:
                    #Use item
                    gameMessage = monsterMoveAndAttack(monsters, player, screen, SCREEN_ALTO, SCREEN_ANCHO, MESSAGE_BOX_HEIGHT)

                    for item in items:
                        if item.coordenada.equals(player.coordenada):
                            if item.getTag() == Tag.PUERTA.value:
                                #Increase dungeonlevel
                                #make new cave
                                dungeonLevel += 1
                                cave = Mazmorra().InitMazmorra(screen)
                                #update player object
                                player.update(cave, Punto(random.randrange(0, SCREEN_ANCHO / 16), random.randrange(0, SCREEN_ALTO / 16)))
                                #make new monster list
                                monsters = Factory().OnFactoryMonsters(screen, cave, monster_tiles, dungeonLevel)
                                items = Factory().OnFactoryItems(screen, cave)
                                gameMessage = "Nuevo nivel de mazmorra! " + gameMessage
                                panelMensajes.mostrarMensaje( gameMessage )

                            elif item.getTag() == Tag.ARMAS.value:
                                player.incrementarAtaqueFisico(item.usarBonusItem())
                                gameMessage = "Has recogido una espada! Tu poder de ataque se incrementa en " + str(item.usarBonusItem()) \
                                               + "! " + gameMessage
                                items.remove(item)
                                panelMensajes.mostrarMensaje( gameMessage )

                            elif item.getTag() == Tag.ARMADURA.value:
                                player.incrementarDefensa(item.usarBonusItem())
                                gameMessage = "Has recogido una pieza de armadura! Tu armadura se incrementa en " + str(item.usarBonusItem()) \
                                               + "! " + gameMessage
                                items.remove(item)
                                panelMensajes.mostrarMensaje( gameMessage )

                            elif item.getTag() == Tag.POCION.value:
                                player.incrementarVitalidad(item.usarBonusItem())
                                gameMessage = "Has recogido una pocion! Hit points increased by " + str(item.usarBonusItem()) \
                                               + "! " + gameMessage

                                items.remove(item)
                                panelMensajes.mostrarMensaje( gameMessage )


                #player attack (A key pressed)
                elif event.key == pygame.K_a:

                    attackDir = 'D' #DEFAULT DIRECTION

                    panelMensajes.mostrarMensaje( "Donde quieres atacar?")
                    pygame.display.flip()
                    pygame.event.set_blocked(pygame.KEYUP)      #Block KEYUP so its not added to the event queue
                    attackWhere = pygame.event.wait()           #Wait for an event

                    #get attack direction
                    if attackWhere.key == pygame.K_DOWN:
                        attackDir = 'D'

                    elif attackWhere.key == pygame.K_UP:
                        attackDir = 'U'

                    elif attackWhere.key == pygame.K_LEFT:
                        attackDir = 'L'

                    elif attackWhere.key == pygame.K_RIGHT:
                        attackDir = 'R'

                    #calculate battle outcome
                    battleresult = SystemBattle.playerAttack(monsters, player, attackDir)
                    monsterAttackMessage = monsterMoveAndAttack(monsters, player, screen, SCREEN_ALTO, SCREEN_ANCHO, MESSAGE_BOX_HEIGHT)

                    if battleresult[0]:
                        gameMessage = "Golpeas al enemigo por {0}! Has matado al enemigo! ".format(str(battleresult[1])) + \
                        monsterAttackMessage
                        panelMensajes.mostrarMensaje( gameMessage )

                    elif battleresult[1] == 0:
                        gameMessage = "No hay nada que golpear aqui! {0}".format(monsterAttackMessage)
                        panelMensajes.mostrarMensaje( gameMessage )

                    else:
                        gameMessage = "Golpeas al enemigo por {0}! {1}".format(str(battleresult[1]), monsterAttackMessage)
                        panelMensajes.mostrarMensaje( gameMessage )

                    removeMonster(monsters)

                #Dig down wall(D key pressed)
                elif event.key == pygame.K_d:

                    panelMensajes.mostrarMensaje( "Donde quieres cavar?" )
                    pygame.display.flip()

                    pygame.event.set_blocked(pygame.KEYUP) #Block KEYUP so its not added to the event queue
                    digWhere = pygame.event.wait()         #Wait for an event

                    try:
                        if digWhere.key == pygame.K_DOWN:
                            Mazmorra().actualizarMazmorra(screen, cave, 'D', player.coordenada.getCoordenadaX(), player.coordenada.getCoordenadaY())
                            gameMessage = "You dig down"
                            panelMensajes.mostrarMensaje( gameMessage )

                        elif digWhere.key == pygame.K_UP:
                            Mazmorra().actualizarMazmorra(screen, cave, 'U', player.coordenada.getCoordenadaX(), player.coordenada.getCoordenadaY())
                            gameMessage = "You dig up"
                            panelMensajes.mostrarMensaje( gameMessage )

                        elif digWhere.key == pygame.K_LEFT:
                            Mazmorra().actualizarMazmorra(screen, cave, 'L', player.coordenada.getCoordenadaX(), player.coordenada.getCoordenadaY())
                            gameMessage = "You dig left"
                            panelMensajes.mostrarMensaje( gameMessage )

                        elif digWhere.key == pygame.K_RIGHT:
                            Mazmorra().actualizarMazmorra(screen, cave, 'R', player.coordenada.getCoordenadaX(), player.coordenada.getCoordenadaY())
                            gameMessage = "You dig right"
                            panelMensajes.mostrarMensaje( gameMessage )

                        gameMessage = monsterMoveAndAttack(monsters, player, screen, SCREEN_ALTO, SCREEN_ANCHO, MESSAGE_BOX_HEIGHT)
                    except:
                        print ("DEBUG: Event bugged out")

                break #only one event is handled at a time, so break out of the event loop after one event is finished

        #Divide by 16 to get correct tile index
        MapRender().dibujarMapa(cave)

        #draw player, monsters and items
        player.dibujar()

        for m in monsters:
            m.dibujar()

        for i in items:
            i.dibujar()

        #Make stats box and display it
        panelEstadisticas.mostrarEstadisticas(player, dungeonLevel)

        #Display
        pygame.display.flip()

def monsterMoveAndAttack(monsters: list, player: Player, screen: Surface, MAP_HEIGHT, MAP_WIDTH, MESSAGE_BOX_HEIGHT):
    """
    Monsters can move and attack the player
    @param monsters: list of monsters
    @param player: the played object
    @param screen: the screen to draw on
    @param MAP_HEIGHT: the mapheight(playable area) in pixels
    @param MAP_WIDTH: the mapwidth(playable area) in pixels
    @param MESSAGE_BOX_HEIGHT: the height of the message box rectangle
    """

    global dungeonLevel
    global panelMensajes
    global panelEstadisticas

    #go through the monsters one at a time
    for m in monsters:
        checkIfFoundPlayer = m.encontrarJugador(player, monsters)

        #if -1 is returned, the player is not nearby
        if checkIfFoundPlayer == -1:
            m.walk(monsters, player)

    #Monster attack!
    monsterAttackResult = SystemBattle.monsterAttack(monsters, player)

    #player died
    if monsterAttackResult[0]:

        panelEstadisticas.mostrarEstadisticas(player, dungeonLevel)
        panelMensajes.mostrarMensaje("The monster(s) around you slaughtered you for {0} HP! Tu mueres!".format(str(monsterAttackResult[1])))
        pygame.display.flip()
        OnGameOver()
    #player still alive
    else:
        if monsterAttackResult[1] != 0:
            return "El enemigo te golpea por " + str(monsterAttackResult[1]) + " HP!"
        else:
            return ""

def OnGameOver():
    """
    Este metodo es llamado cuando el Jugador muere.
    Esperamos 5 segundos antes de salir del programa.
    """
    time.sleep(5)
    OnExitApp()

def OnExitApp():
    """
    Salimos de la App.
    """
    sys.exit(0)

