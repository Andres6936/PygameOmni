# -*- coding: utf-8 -*-
"""
    This file calculates the damage done in battle
    between monsters and player
"""

def playerAttack(monsters, player, direccion):
    """
    El jugador ataca a un enemigo. Calcula el daño hecho a un enemigo.
    @param monsters: the list of monsters
    @param player: the player object
    @param direccion: the attack direction
    @return: a tuple with two values, the first value is a boolean which is true/false depending
            on the monsters state after the attack (alive/dead). The second value is the damage done
    """

    if direccion == 'D':
        attackPosition = (player.getCoordenadaX(), player.getCoordenadaY() + 16)
    elif direccion == 'U':
        attackPosition = (player.getCoordenadaX(), player.getCoordenadaY() - 16)
    elif direccion == 'L':
        attackPosition = (player.getCoordenadaX() - 16, player.getCoordenadaY())
    elif direccion == 'R':
        attackPosition = (player.getCoordenadaX() + 16, player.getCoordenadaY())

    for m in monsters:
        if m.getCoordenada() == attackPosition:
            return calculateOutcome(m, player, monsters)

    #Nothing to attack
    return (False, 0)

def calculateOutcome(monster, player, monsters):
    """
    Calculate the outcome when a player attacks a monster
    @param monster: the monster getting attacked
    @param player: the player
    @param monsters: the list of monsters
    @return: a tuple with two values, the first value is a boolean which is true/false depending
            on the monsters state after the attack (alive/dead). The second value is the damage done
    """

    #The damage done is the difference between the players attack power and the monsters armor
    damageDone = player.getAttackPower() - monster.getDefensa()
    monster.decreaseHP(damageDone)
    if monster.getVitalidad() <= 0:
        monsters.remove(monster)
        return (True, damageDone) #monster died
    else:
        return (False, damageDone) #monster still lives

def calculateOutcome2(player, monster):
    """Calculate the outcome when a monster attacks a player
       @param player: the player
       @param monster: the monster
       @return: the difference between the monsters attack power and the players armor
    """

    return monster.getAttackPower() - player.getDefensa()


def monsterAttack(monsters, player):
    """The monsters attack the player
       @param monsters: the list of monster objects
       @param player: the player object
       @return: a tuple with two values, the first value is a boolean which is true/false depending
                on the player state after the attack (alive/dead). The second value is the damage done
       """

    damageDone = 0

    #all monsters adjacent to the player attack
    for m in monsters:

        monsterPos = m.getCoordenada()

        if playerIsAdjacent(m, player):
            damageDone += calculateOutcome2(player, m)

    #player loses HP
    player.decreaseHP(damageDone)

    return (player.getVitalidad() <= 0, damageDone)

def playerIsAdjacent(monster, player):
    """Check if the player is adjacent to a monster
       @param monster: the monster object
       @param player: the player object
       @return True if player is adjacent, false if not
    """

    if (monster.getCoordenadaX() + 16, monster.getCoordenadaY()) == player.getCoordenada() or \
                (monster.getCoordenadaX() - 16, monster.getCoordenadaY()) == player.getCoordenada() or \
                (monster.getCoordenadaX(), monster.getCoordenadaY() + 16) == player.getCoordenada() or \
                (monster.getCoordenadaX(), monster.getCoordenadaY() - 16) == player.getCoordenada():
        return True
    else:
         return False


