from weapon import fists, short_bow, Weapon
from statistic import Statistic

class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self._health = health
        self.health_max = health
        self.weapon : Weapon = fists

    @property
    def health(self) -> int:
        return self._health
    
    @health.setter
    def health(self, value:int) -> None:
        if value < 0:
            raise ValueError("Health cannot be negative")
        self._health = value

    @property
    def damage(self) -> int:
        return self.weapon.damage
    
    def attack(self, target) -> None:
        if self._health == 0:
            return # raise DeadCharacterException
        try :
            target.health -= self.damage
            print(f"{self.name} has attacked {target.name}. {target.name} has {target._health}/{target.health_max} HP left")
        except Exception as e:
            target.health = 0
            print(f"{target.name} has been defeated")

            
    
    def reset(self) -> None:
        self._health = self.health_max

class Hero(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name, health)
        self.stats : dict[Statistic:int] = {Statistic.STRENGTH:1, Statistic.INTELLIGENCE:1, Statistic.CHARISMA:1}
        self.modifiers: dict[Statistic:int] = {Statistic.STRENGTH:1, Statistic.INTELLIGENCE:1, Statistic.CHARISMA:1}
        self.default_weapon = self.weapon

    @property
    def damage(self) -> int:
        return (self.weapon.damage + self.stats[Statistic.STRENGTH])*self.modifiers[Statistic.STRENGTH]

    def equip(self, weapon) -> None:
        print(f"{self.name} equipped the {weapon.name}")
        self.weapon = weapon

    def drop(self) -> None:
        if self.weapon.name is fists.name:
            print(f"{self.name} can't drop the weapon, since he is not holding any")
            return
        print(f"{self.name} dropped the {self.weapon.name}")
        self.weapon = self.default_weapon


class Enemy(Character):
    def __init__(self, name: str, health: int, weapon) -> None:
        super().__init__(name, health)
        self.weapon = weapon

dragon = Enemy("Dragon", 30, fists)

