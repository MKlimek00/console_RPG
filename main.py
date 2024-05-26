from character import Hero, Enemy, dragon
from weapon import fists, short_bow, iron_sword
from event import dragon_event, sword_event
import random
import utils
import copy

hero = Hero(name="Hero", health= 20)
hero.equip(iron_sword)
events = [dragon_event]#, sword_event]
game_over = False
utils.clear_console()
main_game_actions = {1 : "go to the next event", 2 : "close game"}
while not game_over:
    choice = utils.choice_menu(main_game_actions)
    if choice == 1:
        event = copy.copy(random.choice(events))
        game_over = event.event_loop(hero)

    if choice == 2:
        game_over = True
        print("See you next time")

    utils.wait_before_proceeding()
    utils.clear_console()


