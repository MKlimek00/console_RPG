from character import Hero, Enemy, Character, dragon
from weapon import iron_sword
from utils import get_numeric

class Event:
    def __init__(self, location: str, weather: str) -> None:
        self.location = location
        self.weather = weather
        self.actions : dict = {}
        self.event_ended: bool = False

    def event_loop(self, hero: Hero) -> None:
        while not self.event_ended:
            self.display_actions()
            choice = self.choose_action(hero)
            act = self.actions[choice]
            act(hero)
            

    def display_actions(self) -> None:
        for number, act in self.actions.items():
            print(f"{number}. {act.__name__}")

    # To można przenieśćdo utils
    def choose_action(self, hero: Hero)-> None:
        choice = get_numeric("Your choice: ")
        while choice not in self.actions.keys():
            print("Wrong input, choose proper number")
            choice = get_numeric("Your choice: ")
        
        return choice
        
        

    def reset(self):
        pass


class Combat_Event(Event):
    def __init__(self, location: str, weather: str, enemy: Enemy, skill_requirements: dict) -> None:
        super().__init__(location, weather)
        self.enemy: Enemy = enemy
        self.actions: dict = {1:self.fight, 2:self.talk, 3:self.run}
        self.skill_requirements: dict = skill_requirements
        self.turn_counter : int = 0

    def attack_queue(self, hero: Hero) -> list[Character]:
        #TODO
        # jak będą statystyki to dodać sortowanie listy
        return [hero, self.enemy]
    
    def reset(self) -> None:
        self.enemy.reset()
        self.turn_counter = 0

    def fight(self, hero: Hero) -> None:
        attack_queue : list[Character] = [hero, self.enemy]
        attack_queue[0].attack(attack_queue[1])
        attack_queue[1].attack(attack_queue[0])
        # while hero.health > 0 and self.enemy.health > 0:
        #     attack_queue[turn_counter%2].attack(attack_queue[(turn_counter+1)%2])
        #     print(f"{attack_queue[turn_counter%2].name} attacked {attack_queue[(turn_counter+1)%2].name}")
        #     print(f"{attack_queue[(turn_counter+1)%2].name} has {attack_queue[(turn_counter+1)%2].health}/{attack_queue[(turn_counter+1)%2].health_max} HP")
        #     turn_counter +=1

    def skill_check(self, hero: Hero, skill_name: str, min_skill_value: int) -> bool:
        #TODO
        # jak będą statystyki to dodać funkcjonalność
        return True

    def talk(self, hero: Hero) -> None:
        if self.skill_check(hero, "CHARISMA", 1):
            print("talk")
        else:
            print("you fucked up")

    def run(self, hero: Hero) -> None:
        print("run")

class Inventory_Event(Event):
    def __init__(self, location: str, weather: str, item) -> None:
        super().__init__(location, weather)
        self.item = item
        self.actions: dict = {1:self.take, 2:self.skip}

    def take(self, hero: Hero):
        print("take")

    def skip(self, hero: Hero):
        print("skip")

dragon_event = Combat_Event("Swamp", "Sunny", dragon, {"CHARISMA":3})
sword_event = Inventory_Event("Meadow", "Foggy", iron_sword)