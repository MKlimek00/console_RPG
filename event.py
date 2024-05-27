from character import Hero, Character, DRAGON
from weapon import iron_sword
from utils import get_numeric, choice_menu
from statistic import Statistic

class Event:
    def __init__(self) -> None:
        self.actions : dict = {}

    def event_loop(self, hero: Hero) -> bool:
        end_event = False
        while not end_event:
            choice = choice_menu(self.actions)
            act = self.actions[choice]
            end_event = act(hero)
        self.reset()
        if hero.health == 0:
            return True
        self.reward(hero)
        return False
    
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
    def __init__(self, enemy: Character) -> None:
        super().__init__()
        self.enemy: Character = enemy
        self.actions: dict = {1:self.fight, 2:self.talk, 3:self.run}
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
        hero.improve_max_health(5)

class Non_Combat_Event(Event):
    possible_encouters = {"heal", "drop weapon", "equip weapon"}
    def __init__(self, item) -> None:
        super().__init__()
        self.item = item
        self.actions: dict = {1:self.take, 2:self.skip}

    def take(self, hero: Hero):
        print("take")
        return True

    def skip(self, hero: Hero):
        print("skip")
        return True

dragon_event = Combat_Event(DRAGON)
sword_event = Non_Combat_Event(iron_sword)