from character import Hero, Enemy, Character, dragon
from weapon import iron_sword
from utils import get_numeric, choice_menu
from statistic import Statistic

class Event:
    def __init__(self, location: str, weather: str) -> None:
        self.location = location
        self.weather = weather
        self.actions : dict = {}

    def event_loop(self, hero: Hero) -> bool:
        end_event = False
        while not end_event:
            choice = choice_menu(self.actions)
            act = self.actions[choice]
            end_event = act(hero)
        self.reset()

        self.reward(hero)

        return True if hero.health == 0 else False
    
    def reward(self, hero: Hero): None
    pass
        
    def skill_check(self, hero: Hero, skill_name: str, min_skill_value: int) -> bool:
        #TODO
        # jak będą statystyki to dodać funkcjonalność
        #arg list używać kwargs**
        return True

    def reset(self):
        self.event_ended = False
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

    def fight(self, hero: Hero) -> bool:
        attack_queue : list[Character] = [hero, self.enemy]
        attack_queue[0].attack(attack_queue[1])
        attack_queue[1].attack(attack_queue[0])

        return True if hero.health == 0 or self.enemy.health == 0 else False

    def talk(self, hero: Hero) -> bool:
        if self.skill_check(hero, "CHARISMA", 1):
            print("talk")
            return True
        else:
            print("you fucked up")
            self.enemy.attack(hero)
            return True if hero.health == 0 else False
        

    def run(self, hero: Hero) -> bool:
        if self.skill_check(hero, "CHARISMA", 1):
            print("run")
            return True
        else:
            print("you fucked up")
            self.enemy.attack(hero)
            return True if hero.health == 0 else False
    
    def reward(self, hero:Hero) -> None:
        rewards = {stat.value : stat.name for stat in Statistic}
        choice = choice_menu(rewards)
        hero.improve_statistic(Statistic(choice))

class Inventory_Event(Event):
    def __init__(self, location: str, weather: str, item) -> None:
        super().__init__(location, weather)
        self.item = item
        self.actions: dict = {1:self.take, 2:self.skip}

    def take(self, hero: Hero):
        print("take")
        return True

    def skip(self, hero: Hero):
        print("skip")
        return True

dragon_event = Combat_Event("Swamp", "Sunny", dragon, {"CHARISMA":3})
sword_event = Inventory_Event("Meadow", "Foggy", iron_sword)
print(type(dragon_event.fight))