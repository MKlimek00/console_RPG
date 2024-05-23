from weapon import fists, short_bow

class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self._health = health
        self.health_max = health
        self.weapon = fists

    @property
    def health(self) -> int:
        return self._health
    
    @health.setter
    def health(self, value:int) -> None:
        if value < 0:
            raise ValueError("Health cannot be negative")
        self._health = value
    
    def attack(self, target) -> None:
        if self._health is 0:
            return # raise DeadCharacterException
        try :
            target._health -= self.weapon.damage
        except ValueError:
            target._health = 0
        finally:
            print(f"{self.name} has attacked {target.name}. {target.name} has {target._health}/{target.health_max} HP left")
    
    def reset(self) -> None:
        self._health = self.health_max

class Hero(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name, health)
        self.stats : dict[str:int] = {"STRENGTH":1, "INTELLIGENCE":1, "CHARISMA":1}
        self.default_modifiers : dict[str:int] = {"STRENGTH":1, "INTELLIGENCE":1, "CHARISMA":1}
        self.modifiers: dict[str:int] = {"STRENGTH":1, "INTELLIGENCE":1, "CHARISMA":1}
        self.default_weapon = self.weapon

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

