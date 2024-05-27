from character import Hero, DRAGON
from weapon import fists, short_bow, iron_sword, magic_staff
from event import dragon_event, sword_event
from statistic import Statistic
import random
import utils
import copy

# utils.clear_console()
game_over = False
hero = Hero(name="Hero", health= 20, stats={stat : 1 for stat in Statistic})
events = [dragon_event]#, sword_event]
initial_weapons = {1:iron_sword, 2:short_bow, 3:magic_staff}

choice = utils.choice_menu(initial_weapons)
hero.equip(initial_weapons[choice])

main_game_actions = {1 : "go to the next event", 2 : "close game"}
while not game_over:
    choice = utils.choice_menu(main_game_actions)
    if choice == 1:
        event = copy.copy(random.choice(events))
        game_over = event.event_loop(hero)

    if choice == 2:
        game_over = True

if hero.health == 0:
    print("GAME OVER!")
else:
    print("See you next time")

utils.wait_before_proceeding()
utils.clear_console()


