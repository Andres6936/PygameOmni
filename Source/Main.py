# -*- coding: utf-8 -*-

"""
   This is the file where all the magic happens. It contains methods for setting up
   and running the game, aswell as creating different game objects.
"""

import random
import sys
import time
import pygame

from Source.Enum.EnumImage import EnumImage
from Source.GameScreen import Gamescreen
from Source.GameSystemBatalla import SystemBattle
from Source.GameMundo import MapGene
from Source.GameMundo.MapFactory import Factory

# CONSTANTES DE LA APP

MONSTER_COUNT:      int = 15
STATS_BOX_WIDTH:    int = 200
STATS_BOX_OFFSET:   int = 10
MESSAGE_BOX_HEIGHT: int = 64

# ATRIBUTOS DE LA APP

dungeonLevel: int = 1 #dungeon level starts at 1


def OnInitGame( MAP_WIDTH: int, MAP_HEIGHT: int ):
    """
    This method initializes and sets up the game
    @param MAP_WIDTH: the map(playable area) width
    @param MAP_HEIGHT: the map(playable area) height
    """

    global dungeonLevel

    # Inicializamos los modulos de Pygame.
    pygame.init()

    #Get a screen object to draw on
    #Total screen size is MAP_WIDTH + 265 (stats box) and MAP_HEIGHT + 128 (message box)
    screen = pygame.display.set_mode((MAP_WIDTH + STATS_BOX_WIDTH, MAP_HEIGHT + MESSAGE_BOX_HEIGHT), 0, 32)

    pygame.display.set_caption("INF3331 Roguelike Project")

    # Create the first cave. This can take a couple of seconds to make
    cave = MapGene.run_mapgen( MAP_WIDTH, MAP_HEIGHT, screen )

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
    OnRunGame(screen, cave, player, monster_tiles, MAP_HEIGHT, MAP_WIDTH)

def removeMonster(monsters):
    """Remove dead monsters from the monster list
       @param monsters: list of monsters
    """

    for m in monsters:
        if m.getVitalidad() <= 0:
            monsters.remove(m)

def OnRunGame(screen: object, cave: object, player: object, monster_tiles: list, MAPA_ALTO: int, MAPA_ANCHO: int):
    """
    Run the game and the contains the main game loop
    @param screen: the game screen to draw
    @type screen: object
    @param cave: the map
    @type cave: object
    @param player: the player object
    @type player: object
    @param monster_tiles: monster images
    @type monster_tiles: list
    @param MAPA_ALTO: the map heith (playable area) in pixels
    @type MAPA_ALTO: int
    @param MAPA_ANCHO: the map width (playable area) in pixels
    @type MAPA_ANCHO: int
    """

    global dungeonLevel

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
                if event.key == pygame.K_DOWN or \
                    event.key == pygame.K_UP or \
                    event.key == pygame.K_LEFT or \
                    event.key == pygame.K_RIGHT:
                        player.handleKey(event, monsters)
                        gameMessage = monsterMoveAndAttack(monsters, player, screen, MAPA_ALTO, MAPA_ANCHO, MESSAGE_BOX_HEIGHT)

                elif event.key == pygame.K_s:
                    #Use item
                    gameMessage = monsterMoveAndAttack(monsters, player, screen, MAPA_ALTO, MAPA_ANCHO, MESSAGE_BOX_HEIGHT)

                    for item in items:
                        if item.getCoordenada() == player.getCoordenada():
                            if item.getNombre() == "Puerta de Madera":
                                #Increase dungeonlevel
                                dungeonLevel += 1
                                #make new cave
                                cave = MapGene.run_mapgen(MAPA_ANCHO, MAPA_ALTO, screen)
                                #update player object
                                player.update(cave, (random.randrange(0, MAPA_ANCHO, 16), random.randrange(0,
                                                                                                           MAPA_ALTO, 16)))
                                #make new monster list
                                monsters = Factory().OnFactoryMonsters(screen, cave, monster_tiles, dungeonLevel)
                                items = Factory().OnFactoryItems(screen, cave)
                                gameMessage = "Nuevo nivel de mazmorra! " + gameMessage

                            elif item.getNombre() == "weapon":
                                player.increaseAP(item.usarBonusItem())
                                gameMessage = "Has recogido una espada! Tu poder de ataque se incrementa en " + str(item.usarBonusItem()) \
                                               + "! " + gameMessage
                                items.remove(item)

                            elif item.getNombre() == "armor":
                                player.incrementarDefensa(item.usarBonusItem())
                                gameMessage = "Has recogido una pieza de armadura! Tu armadura se incrementa en " + str(item.usarBonusItem()) \
                                               + "! " + gameMessage
                                items.remove(item)

                            elif item.getNombre() == "food":
                                player.incrementarVitalidad(item.usarBonusItem())
                                gameMessage = "Has recogido una pocion! Hit points increased by " + str(item.usarBonusItem()) \
                                               + "! " + gameMessage

                                items.remove(item)


                #player attack (A key pressed)
                elif event.key == pygame.K_a:

                    attackDir = 'D' #DEFAULT DIRECTION

                    Gamescreen.OnMessageBox(screen, MAPA_ALTO, MESSAGE_BOX_HEIGHT, MAPA_ANCHO, "Donde quieres atacar?")
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
                    monsterAttackMessage = monsterMoveAndAttack(monsters, player, screen, MAPA_ALTO, MAPA_ANCHO, MESSAGE_BOX_HEIGHT)

                    if battleresult[0]:
                        gameMessage = "Golpeas al enemigo por {0}! Has matado al enemigo! ".format(str(battleresult[1])) + \
                        monsterAttackMessage
                    elif battleresult[1] == 0:
                        gameMessage = "No hay nada que golpear aqui! {0}".format(monsterAttackMessage)
                    else:
                        gameMessage = "Golpeas al enemigo por {0}! {1}".format(str(battleresult[1]), monsterAttackMessage)


                    removeMonster(monsters)

                #Dig down wall(D key pressed)
                elif event.key == pygame.K_d:

                    Gamescreen.OnMessageBox(screen, MAPA_ALTO, MESSAGE_BOX_HEIGHT, MAPA_ANCHO, "Donde quieres cavar?")
                    pygame.display.flip()

                    pygame.event.set_blocked(pygame.KEYUP) #Block KEYUP so its not added to the event queue
                    digWhere = pygame.event.wait()         #Wait for an event

                    try:
                        if digWhere.key == pygame.K_DOWN:
                            MapGene.updateCave(screen, cave, 'D', player.getCoordenadaX(), player.getCoordenadaY())
                            gameMessage = "You dig down"

                        elif digWhere.key == pygame.K_UP:
                            MapGene.updateCave(screen, cave, 'U', player.getCoordenadaX(), player.getCoordenadaY())
                            gameMessage = "You dig up"

                        elif digWhere.key == pygame.K_LEFT:
                            MapGene.updateCave(screen, cave, 'L', player.getCoordenadaX(), player.getCoordenadaY())
                            gameMessage = "You dig left"

                        elif digWhere.key == pygame.K_RIGHT:
                            MapGene.updateCave(screen, cave, 'R', player.getCoordenadaX(), player.getCoordenadaY())
                            gameMessage = "You dig right"

                        gameMessage = monsterMoveAndAttack(monsters, player, screen, MAPA_ALTO, MAPA_ANCHO, MESSAGE_BOX_HEIGHT)
                    except:
                        print ("DEBUG: Event bugged out")

                break #only one event is handled at a time, so break out of the event loop after one event is finished

        #Divide by 16 to get correct tile index
        for y in range(0, int(MAPA_ALTO / 16)):
            for x in range(0, int(MAPA_ANCHO / 16)):
                cave[y][x].dibujar()

        #draw player, monsters and items
        player.dibujar()

        for m in monsters:
            m.dibujar()

        for i in items:
            i.dibujar()

        #Make stats box and display it
        Gamescreen.OnInitStatBox(screen, player, dungeonLevel, MAPA_ANCHO, MAPA_ALTO, STATS_BOX_WIDTH)
        Gamescreen.OnMessageBox(screen, MAPA_ALTO, MESSAGE_BOX_HEIGHT, MAPA_ANCHO, gameMessage)

        #Display
        pygame.display.flip()

def monsterMoveAndAttack(monsters, player, screen, MAP_HEIGHT, MAP_WIDTH, MESSAGE_BOX_HEIGHT):
    """Monsters can move and attack the player
       @param monsters: list of monsters
       @param player: the played object
       @param screen: the screen to draw on
       @param MAP_HEIGHT: the mapheight(playable area) in pixels
       @param MAP_WIDTH: the mapwidth(playable area) in pixels
       @param MESSAGE_BOX_HEIGHT: the height of the message box rectangle
    """

    global dungeonLevel

    #go through the monsters one at a time
    for m in monsters:
        checkIfFoundPlayer = m.findPlayer(player, monsters)

        #if -1 is returned, the player is not nearby
        if checkIfFoundPlayer == -1:
            m.walk(monsters, player)

    #Monster attack!
    monsterAttackResult = SystemBattle.monsterAttack(monsters, player)

    #player died
    if monsterAttackResult[0]:

        Gamescreen.OnInitStatBox(screen, player, dungeonLevel, MAP_WIDTH, MAP_HEIGHT, STATS_BOX_WIDTH)
        Gamescreen.OnMessageBox(screen, MAP_HEIGHT, MESSAGE_BOX_HEIGHT, MAP_WIDTH, "The monster(s) around you " \
                "slaughtered you for " + str(monsterAttackResult[1]) + " HP! Tu mueres!")
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

