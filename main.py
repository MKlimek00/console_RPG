from character import Hero, Enemy
from weapon import fists, short_bow, iron_sword

hero = Hero(name="Hero", health= 100)
hero.equip(iron_sword)
enemy = Enemy(name="enemy", health= 100, weapon= short_bow)

while (enemy.health > 0 and hero.health > 0):
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")
    hero.drop()
    input()

print(f"endgame")