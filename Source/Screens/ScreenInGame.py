import pygame
import random

from Core.Utilidades.Punto import Punto
from Source.Enum.EnumImage import EnumImage
from Source.Enum.Tag import Tag
from Source.GameMundo.FactoryEntidades import Factory
from Source.GameMundo.Mazmorra import Mazmorra
from Source.GamePaneles.PanelEstadisticas import PanelEstadisticas
from Source.GamePaneles.PanelMazmorra import PanelMazmorra
from Source.GamePaneles.PanelMensajes import PanelMensajes
from Source.Screens.IScreen import IScreen
from Source.Screens.NextScene import NextScene
from Source.GameSystemBatalla import SystemBattle


class ScreenInGame(IScreen):

    def __init__(self, sceneManager):
        self.sceneManager = sceneManager
        self.screen = sceneManager.Surface()
        self.screenWidth = sceneManager.ScreenWidth()
        self.screenHeight = sceneManager.ScreenHeight()

        # El nivel de la mazmorra empieza en 1.
        self.mazmorraLevel: int = 1

        # Iniciamos la mazmorra.
        mazmorra = Mazmorra().InitMazmorra(self.screen)

        # Inicializamos los paneles y la interfaz.
        self.panelMazmorra = PanelMazmorra(mazmorra)
        self.panelMensajes = PanelMensajes(self.screen)
        self.panelEstadisticas = PanelEstadisticas(self.screen)

        # load monster images
        monster_images = [
            EnumImage.CUCARACHA_GIGANTE.value,
            EnumImage.GUSANO_CEREBRO.value,
            EnumImage.MUMMY.value,
            EnumImage.OGRO_MAGO.value,
            EnumImage.DRAGON_ROJO.value
        ]

        self.monster_tiles = [pygame.image.load(img).convert_alpha() for img in monster_images]

        # create player object
        self.player = Factory().onFactoryJugador(self.screen, mazmorra, self.mazmorraLevel)

        # Make list of monsters
        self.monsters = Factory().OnFactoryMonsters(self.screen, mazmorra, self.monster_tiles, self.mazmorraLevel)
        self.items = Factory().OnFactoryItems(self.screen, mazmorra)

        self.gameMessage: str = ""

    def Update(self) -> NextScene:
        global mazmorra

        for event in pygame.event.get():

            # player clicked close button
            if event.type == pygame.QUIT:
                return NextScene.EXIT

            # a key has been pressed
            if event.type == pygame.KEYDOWN:

                # move player
                self.player.handleKey(event, self.monsters)
                gameMessage = self.monsterMoveAndAttack(self.monsters, self.player, self.screen)

                if event.key == pygame.K_s:
                    # Use item
                    gameMessage = self.monsterMoveAndAttack(self.monsters, self.player, self.screen)

                    for item in self.items:
                        if item.coordenada.equals(self.player.coordenada):
                            if item.getTag() == Tag.PUERTA.value:
                                # Increase dungeonlevel
                                # make new cave
                                self.mazmorraLevel += 1
                                cave = Mazmorra().InitMazmorra(self.screen)
                                # El nuevo mundo lo pasamos por parametro.
                                self.panelMazmorra.setMundo(cave)
                                # update player object
                                self.player.update(cave, Punto(random.randrange(0, self.screenWidth / 16),
                                                               random.randrange(0, self.screenHeight / 16)))
                                # make new monster list
                                monsters = Factory().OnFactoryMonsters(self.screen, cave, self.monster_tiles,
                                                                       self.mazmorraLevel)
                                items = Factory().OnFactoryItems(self.screen, cave)
                                gameMessage = "Nuevo nivel de mazmorra! " + gameMessage
                                self.panelMensajes.mostrarMensaje(gameMessage)

                            elif item.getTag() == Tag.ARMAS.value:
                                self.player.incrementarAtaqueFisico(item.usarBonusItem())
                                gameMessage = "Has recogido una espada! Tu poder de ataque se incrementa en " + str(
                                    item.usarBonusItem()) \
                                              + "! " + gameMessage
                                items.remove(item)
                                self.panelMensajes.mostrarMensaje(gameMessage)

                            elif item.getTag() == Tag.ARMADURA.value:
                                self.player.incrementarDefensa(item.usarBonusItem())
                                gameMessage = "Has recogido una pieza de armadura! Tu armadura se incrementa en " + str(
                                    item.usarBonusItem()) \
                                              + "! " + gameMessage
                                items.remove(item)
                                self.panelMensajes.mostrarMensaje(gameMessage)

                            elif item.getTag() == Tag.POCION.value:
                                self.player.incrementarVitalidad(item.usarBonusItem())
                                gameMessage = "Has recogido una pocion! Hit points increased by " + str(
                                    item.usarBonusItem()) \
                                              + "! " + gameMessage

                                items.remove(item)
                                self.panelMensajes.mostrarMensaje(gameMessage)


                # player attack (A key pressed)
                elif event.key == pygame.K_a:

                    attackDir = 'D'  # DEFAULT DIRECTION

                    self.panelMensajes.mostrarMensaje("Donde quieres atacar?")
                    pygame.display.flip()
                    pygame.event.set_blocked(pygame.KEYUP)  # Block KEYUP so its not added to the event queue
                    attackWhere = pygame.event.wait()  # Wait for an event

                    # get attack direction
                    if attackWhere.key == pygame.K_DOWN:
                        attackDir = 'D'

                    elif attackWhere.key == pygame.K_UP:
                        attackDir = 'U'

                    elif attackWhere.key == pygame.K_LEFT:
                        attackDir = 'L'

                    elif attackWhere.key == pygame.K_RIGHT:
                        attackDir = 'R'

                    # calculate battle outcome
                    battleresult = SystemBattle.playerAttack(self.monsters, self.player, attackDir)
                    monsterAttackMessage = self.monsterMoveAndAttack(self.monsters, self.player, self.screen)

                    if battleresult[0]:
                        gameMessage = "Golpeas al enemigo por {0}! Has matado al enemigo! ".format(
                            str(battleresult[1])) + \
                                      monsterAttackMessage
                        self.panelMensajes.mostrarMensaje(gameMessage)

                    elif battleresult[1] == 0:
                        gameMessage = "No hay nada que golpear aqui! {0}".format(monsterAttackMessage)
                        self.panelMensajes.mostrarMensaje(gameMessage)

                    else:
                        gameMessage = "Golpeas al enemigo por {0}! {1}".format(str(battleresult[1]),
                                                                               monsterAttackMessage)
                        self.panelMensajes.mostrarMensaje(gameMessage)

                    self.removeMonster(self.monsters)

                # Dig down wall(D key pressed)
                elif event.key == pygame.K_d:

                    self.panelMensajes.mostrarMensaje("Donde quieres cavar?")
                    pygame.display.flip()

                    pygame.event.set_blocked(pygame.KEYUP)  # Block KEYUP so its not added to the event queue
                    digWhere = pygame.event.wait()  # Wait for an event

                    try:
                        if digWhere.key == pygame.K_DOWN:
                            Mazmorra().actualizarMazmorra(self.screen, mazmorra, 'D',
                                                          self.player.coordenada.getCoordenadaX(),
                                                          self.player.coordenada.getCoordenadaY())
                            gameMessage = "You dig down"
                            self.panelMensajes.mostrarMensaje(gameMessage)

                        elif digWhere.key == pygame.K_UP:
                            Mazmorra().actualizarMazmorra(self.screen, mazmorra, 'U',
                                                          self.player.coordenada.getCoordenadaX(),
                                                          self.player.coordenada.getCoordenadaY())
                            gameMessage = "You dig up"
                            self.panelMensajes.mostrarMensaje(gameMessage)

                        elif digWhere.key == pygame.K_LEFT:
                            Mazmorra().actualizarMazmorra(self.screen, mazmorra, 'L',
                                                          self.player.coordenada.getCoordenadaX(),
                                                          self.player.coordenada.getCoordenadaY())
                            gameMessage = "You dig left"
                            self.panelMensajes.mostrarMensaje(gameMessage)

                        elif digWhere.key == pygame.K_RIGHT:
                            Mazmorra().actualizarMazmorra(self.screen, mazmorra, 'R',
                                                          self.player.coordenada.getCoordenadaX(),
                                                          self.player.coordenada.getCoordenadaY())
                            gameMessage = "You dig right"
                            self.panelMensajes.mostrarMensaje(gameMessage)

                        gameMessage = self.monsterMoveAndAttack(self.monsters, self.player, self.screen)
                    except:
                        print("DEBUG: Event bugged out")

                break  # only one event is handled at a time, so break out of the event loop after one event is finished
        return NextScene.NONE

    def Draw(self):
        # get clock so we can control frames per second
        clock = pygame.time.Clock()
        clock.tick(30)  # Limit the screen to 5 FPS

        # Divide by 16 to get correct tile index
        self.panelMazmorra.dibujarMapa()

        # draw player, monsters and items
        self.player.dibujar()

        for m in self.monsters:
            m.dibujar()

        for i in self.items:
            i.dibujar()

        # Make stats box and display it
        self.panelEstadisticas.mostrarEstadisticas(self.player, self.mazmorraLevel)

        # Display
        pygame.display.flip()

    def Clear(self):
        pass

    def monsterMoveAndAttack(self, monsters: list, player, screen):
        """
        Monsters can move and attack the player
        @param monsters: list of monsters
        @param player: the played object
        @param screen: the screen to draw on
        """

        global panelMensajes
        global panelEstadisticas

        # go through the monsters one at a time
        for m in monsters:
            checkIfFoundPlayer = m.encontrarJugador(player, monsters)

            # if -1 is returned, the player is not nearby
            if checkIfFoundPlayer == -1:
                m.walk(monsters, player)

        # Monster attack!
        monsterAttackResult = SystemBattle.monsterAttack(monsters, player)

        # player died
        if monsterAttackResult[0]:

            panelEstadisticas.mostrarEstadisticas(player, self.mazmorraLevel)
            panelMensajes.mostrarMensaje(
                "The monster(s) around you slaughtered you for {0} HP! Tu mueres!".format(str(monsterAttackResult[1])))
            pygame.display.flip()
            self.sceneManager.OnGameOver()
        # player still alive
        else:
            if monsterAttackResult[1] != 0:
                return "El enemigo te golpea por " + str(monsterAttackResult[1]) + " HP!"
            else:
                return ""

    def removeMonster(self, monsters):
        """Remove dead monsters from the monster list
           @param monsters: list of monsters
        """

        for m in monsters:
            if m.getVitalidad() <= 0:
                monsters.remove(m)
