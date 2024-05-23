from character import Hero, Enemy, dragon
from weapon import fists, short_bow, iron_sword
from event import dragon_event, sword_event
import random
import utils
import copy

hero = Hero(name="Hero", health= 20)
hero.equip(iron_sword)
events = [dragon_event, sword_event]
game_over = False
utils.clear_console()
while not game_over:
    print("1. choose next event\n2. close game")
    choice = utils.get_numeric("Your choice: ")
    while choice not in {1,2}:
        print("Wrong input, choose proper number")
        choice = utils.get_numeric("Your choice: ")
    if choice == 1:
        event = copy.copy(random.choice(events))
        game_over = event.event_loop(hero)

    if choice == 2:
        game_over = True
        print("See you next time")

    utils.wait_before_proceeding()
    utils.clear_console()


