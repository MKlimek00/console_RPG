from character import Hero, Enemy
from weapon import fists, short_bow, iron_sword
from event import dragon_event, sword_event
import random
import utils
import copy

hero = Hero(name="Hero", health= 100)
hero.equip(iron_sword)
events = [dragon_event, sword_event]
game_over = False
while not game_over:
    print("1. choose next event\n2. close game")
    choice = utils.get_numeric("Your choice: ")
    while choice not in {1,2}:
        print("Wrong input, choose proper number")
        choice = utils.get_numeric("Your choice: ")
    if choice == 2:
        game_over = True
        print("See you next time")
    if choice == 1:
        event = copy.copy(random.choice(events))
        print(f"you are at {event.location} and it's {event.weather}")
        event.display_actions()
        event.choose_action(hero)
    utils.wait_before_proceeding()
    utils.clear_console()

