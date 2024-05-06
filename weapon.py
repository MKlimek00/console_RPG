from dataclasses import dataclass

@dataclass()
class Weapon:
    name:str
    weapon_type: str
    damage: int
    value: int


iron_sword = Weapon("Iron Sword", "sharp", 10, 10)

short_bow = Weapon("Short bow", "ranged", 4, 8)

fists = Weapon("Fists", "blunt", 2, 0)