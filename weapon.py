from dataclasses import dataclass
from statistic import Statistic

@dataclass()
class Weapon:
    name:str
    used_statistic : Statistic
    damage: int

    def __repr__(self) -> str:
        return f"{self.name}, damage: {self.damage}, uses: {self.used_statistic.name}"


iron_sword = Weapon("Iron Sword", Statistic.STRENGTH, 5)

short_bow = Weapon("Short bow", Statistic.DEXTERITY, 5)

fists = Weapon("Fists", Statistic.STRENGTH, 1)

magic_staff = Weapon("Magic staff", Statistic.INTELLIGENCE, 5)