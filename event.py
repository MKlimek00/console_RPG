from character import Hero, Enemy, dragon
from weapon import iron_sword
from utils import get_numeric

class Event:
    def __init__(self, location: str, weather: str) -> None:
        self.location = location
        self.weather = weather
        self.actions:dict = {}

    def display_actions(self) -> None:
        for number, act in self.actions.items():
            print(f"{number}. {act.__name__}")

    def choose_action(self)-> None:
        choice = get_numeric("Your choice: ")
        while choice not in self.actions.keys():
            print("Wrong input, choose proper number")
            choice = get_numeric("Your choice: ")
        
        act = self.actions[choice]
        act()


class Combat_Event(Event):
    
    def __init__(self, location: str, weather: str, enemy: Enemy, ) -> None:
        super().__init__(location, weather)
        self.enemy = enemy
        self.actions: dict = {1:self.fight, 2:self.talk, 3:self.run}

    def fight(self):
        print("fight")

    def talk(self):
        print("talk")

    def run(self):
        print("run")

class Inventory_Event(Event):
    def __init__(self, location: str, weather: str, item) -> None:
        super().__init__(location, weather)
        self.item = item
        self.actions: dict = {1:self.take, 2:self.skip}

    def take(self):
        print("take")

    def skip(self):
        print("skip")

dragon_event = Combat_Event("Swamp", "Sunny", dragon)
sword_event = Inventory_Event("Meadow", "Foggy", iron_sword)