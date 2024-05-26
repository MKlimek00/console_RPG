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
            target._health = 0
            print(e)

    
    def reset(self) -> None:
        self._health = self.health_max

class Hero(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name, health)
        self.stats : dict[Statistic:int] = {stat:1 for stat in Statistic}
        self.stats[Statistic.SPEED] = 4
        self.modifiers: dict[Statistic:int] = {stat:1 for stat in Statistic}
        self.default_weapon = self.weapon

    @property
    def damage(self) -> int:
        return (self.weapon.damage + self.stats[Statistic.STRENGTH])*self.modifiers[Statistic.STRENGTH]
    
    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value:int) -> None:
        if value < 1:
            raise HeroDeathException
        if value > self.health_max:
            self._health = self.health_max
        else:
            self._health = value

    def equip(self, weapon) -> None:
        print(f"{self.name} equipped the {weapon.name}")
        self.weapon = weapon

    def drop(self) -> None:
        if self.weapon.name is fists.name:
            print(f"{self.name} can't drop the weapon, since he is not holding any")
            return
        print(f"{self.name} dropped the {self.weapon.name}")
        self.weapon = self.default_weapon

    def clear_modifiers(self) -> None:
        self.modifiers: dict[Statistic:int] = {stat:1 for stat in Statistic}
    
    def improve_statistic(self, stat : Statistic) -> None:
        self.stats[stat] += 1
        print(f"Your {stat.name} has improved to {self.stats[stat]}")
    
    def improve_max_health(self, added_value: int) -> None:
        self.health_max += added_value
        self.health += added_value

class Enemy(Character):
    def __init__(self, name: str, health: int, weapon) -> None:
        super().__init__(name, health)
        self.weapon = weapon
    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value:int) -> None:
        if value < 1:
            raise EnemyDeathException
        self._health = value

class HeroDeathException(Exception):
    def __init__(self, message = "You Died!") -> None:
        self.message = message
        super().__init__(self.message)

class EnemyDeathException(Exception):
    def __init__(self, message = "Enemy has been defeated!") -> None:
        self.message = message
        super().__init__(self.message)

dragon = Enemy("Dragon", 30, fists)

