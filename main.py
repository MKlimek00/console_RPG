from character import Hero, Enemy
from weapon import fists, short_bow, iron_sword
from event import dragon_event, sword_event

hero = Hero(name="Hero", health= 100)
hero.equip(iron_sword)
event = dragon_event
# event = sword_event
while (hero.health > 0):
    print(f"you are at {event.location} and it's {event.weather}")
    event.display_actions()
    event.choose_action(hero)


print(f"Game over!")