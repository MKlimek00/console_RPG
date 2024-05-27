from character import HERO
from weapon import initial_weapons
from event import Combat_Event, Non_Combat_Event
import random
import utils

# utils.clear_console()
game_over = False
hero = HERO

choice = utils.choice_menu(initial_weapons)
hero.equip_weapon(initial_weapons[choice])

main_game_actions = {1 : "go to the next event", 2 : "close game"}
while not game_over:
    utils.wait_before_proceeding()
    utils.clear_console()
    if hero.stats_sum > 20:
        print("Congratulations. You've won!")
        break
    choice = utils.choice_menu(main_game_actions)
    if choice == 1:
        events = random.choices([Combat_Event(), Non_Combat_Event()], [0.8, 0.2], k=3)
        events_choice = {num : event.hint for num, event in enumerate(events, 1)}
        chosen_event = events[utils.choice_menu(events_choice)-1]
        game_over = chosen_event.event_loop(hero)

    if choice == 2:
        game_over = True

if hero.health == 0:
    print("GAME OVER!")
else:
    print("See you next time")

utils.wait_before_proceeding()
utils.clear_console()


