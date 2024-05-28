from character import HERO
from weapon import initial_weapons
from event import random_events
import utils

# SETUP
GAME_OVER = False
hero = HERO
EVENTS_PER_TURN = 3
MAIN_GAME_ACTIONS = {1 : "go to the next event", 2 : "close game"}

# Start of the game
utils.clear_console()
print(f"Hello {hero.name}!\nTo start the game choose your first weapon.")
choice = utils.choice_menu(initial_weapons)
hero.equip_weapon(initial_weapons[choice])

while not GAME_OVER:
    utils.wait_before_proceeding()
    utils.clear_console()
    if hero.stats_sum > 10:
        print("Congratulations. You've won!")
        break
    print("What do you want to do now?")
    choice = utils.choice_menu(MAIN_GAME_ACTIONS)
    if choice == 1:
        events = random_events(EVENTS_PER_TURN)
        events_choice = {num : event.hint for num, event in enumerate(events, 1)}
        chosen_event = events[utils.choice_menu(events_choice)-1]
        GAME_OVER = chosen_event.event_loop(hero)

    if choice == 2:
        GAME_OVER = True

if hero.health == 0:
    print("GAME OVER!")
else:
    print("See you next time")

utils.wait_before_proceeding()
utils.clear_console()


