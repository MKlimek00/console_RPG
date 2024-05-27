from statistic import Statistic
from weapon import Weapon, fists
from math import floor

class Character:
    def __init__(self, name:str, health:int, stats: dict[Statistic:int]) -> None:
        self.name = name
        self._health = health
        self.health_max = health
        self.stats = stats

    @property
    def damage(self) -> int:
        if Statistic.STRENGTH in self.stats.keys():
            return self.stats[Statistic.STRENGTH]
        else: return 1
    
    @property
    def health(self) -> int:
        return self._health
    
    @health.setter
    def health(self, value:int) -> None:
        if value < 0:
            self._health = 0
        elif value > self.health_max:
            self._health = self.health_max
        else:
            self._health = value
    
    @property
    def death_message(self) -> str:
        return f"{self.name} has been deafeated"

    def attack(self, target) -> bool:
        target.health -= self.damage
        print(f"{self.name} has attacked {target.name}. {target.name} has {target.health}/{target.health_max} HP left")
        
        if target.health == 0:
            print(target.death_message)
            return True
        
        return False
    
    def reset(self) -> None:
        self.health = self.health_max

class Hero(Character):
    def __init__(self, name: str, health: int, stats: dict):
        super().__init__(name, health, stats)
        self.weapon : Weapon = fists

    @property
    def damage(self) -> int:
        if self.weapon.used_statistic in self.stats.keys():
            return self.weapon.damage + self.stats[self.weapon.used_statistic]
        elif Statistic.STRENGTH in self.stats.keys():
            return self.stats[Statistic.STRENGTH]
        else : return 1

    def equip(self, weapon) -> None:
        print(f"{self.name} equipped the {weapon.name}")
        self.weapon = weapon

    def drop(self) -> None:
        if self.weapon.name is fists.name:
            print(f"{self.name} can't drop the weapon, since he is not holding any")
            return
        print(f"{self.name} dropped the {self.weapon.name}")
        self.weapon = fists

    def improve_statistic(self, stat : Statistic) -> None:
        self.stats[stat] += 1
        print(f"Your {stat.name} has improved to {self.stats[stat]}")
    
    def improve_max_health(self, added_value: int) -> None:
        self.health_max += added_value
        self.health += added_value
        print(f"You've gained {added_value} max HP")

    def heal(self, fraction: float) -> None:
        health_before = self.health
        self.health += floor(fraction*self.health_max)
        print(f"You've healed {self.health - health_before} HP")

DRAGON = Character(name="Dragon", health=30, stats={Statistic.STRENGTH:3, Statistic.INTELLIGENCE:5, Statistic.SPEED:2})
