from character import Hero, Character, MONSTERS, MONSTERS_PROBABILITIES
from utils import choice_menu, normalize_probabilities
from weapon import initial_weapons
from statistic import Statistic
import random


class Event:
    def __init__(self) -> None:
        self.actions: dict = {}

    def event_loop(self, hero: Hero) -> bool:
        end_event = False
        print(self.description)
        while not end_event:
            choice = choice_menu(self.actions)
            act = self.actions[choice]
            end_event = act(hero)

        return True if hero.health == 0 else False

    @property
    def hint(self) -> str:
        return "basic event, nothing happens"

    @property
    def description(self) -> str:
        return "basic event, nothing happens"

    def skill_check(self, hero: Hero, stat: Statistic, min_value: int) -> bool:
        if stat not in hero.stats.keys():
            return False
        return hero.stats[stat] >= min_value


class Combat_Event(Event):
    def __init__(self) -> None:
        super().__init__()
        self.enemy: Character = random.choices(
            MONSTERS, MONSTERS_PROBABILITIES, k=1)[0]
        self.actions: dict = {1: self.fight, 2: self.talk, 3: self.run}

    @property
    def description(self) -> str:
        return f"You have encountered {self.enemy.name}. What do you want to do?"

    @property
    def hint(self) -> str:
        stat: Statistic = random.choice(list(self.enemy.stats.keys()))
        value: int = self.enemy.stats[stat]
        return f"You will meet a monster whose {stat.name} is on lvl {value}"

    def fight(self, hero: Hero) -> bool:
        attack_queue: list[Character] = sorted(
            [hero, self.enemy], key=lambda x: x.stats[Statistic.SPEED], reverse=True)
        attack_queue[0].attack(attack_queue[1])
        if attack_queue[1].health > 0:
            attack_queue[1].attack(attack_queue[0])

        if hero.health == 0:
            return True
        if self.enemy.health == 0:
            self.reward(hero)
            return True
        return False

    def talk(self, hero: Hero) -> bool:
        if self.skill_check(hero, Statistic.CHARISMA, self.enemy.stats[Statistic.CHARISMA]):
            print(f"You convinced the {self.enemy.name} to surrender")
            return True
        else:
            print(f"You insulted {self.enemy.name}'s mother")
            self.enemy.attack(hero)
            return True if hero.health == 0 else False

    def run(self, hero: Hero) -> bool:
        if self.skill_check(hero, Statistic.SPEED, self.enemy.stats[Statistic.SPEED]*2):
            print("You succesfuly escaped the danger.")
            return True
        else:
            print(f"You slipped on a leaf while running and {
                  self.enemy.name} caught you.")
            self.enemy.attack(hero)
            return True if hero.health == 0 else False

    def reward(self, hero: Hero) -> None:
        rewards = {stat.value: stat.name for stat in Statistic}
        choice = choice_menu(rewards)
        hero.improve_statistic(Statistic(choice))
        hero.improve_max_health(5)


class Non_Combat_Event(Event):
    POSSIBLE_ENCOUNTERS = ["heal", "drop weapon", "equip weapon", "level up"]
    EFFECTS = {"heal": "hero.heal(0.4)",
               "drop weapon": "hero.drop_weapon()",
               "equip weapon": "hero.equip_weapon(random.choice(list(initial_weapons.values())))",
               "level up": "hero.improve_statistic(random.choice(list(Statistic)))"}

    def __init__(self) -> None:
        super().__init__()
        self.actions: dict = {1: self.take, 2: self.skip}

    @property
    def description(self) -> str:
        return "You can choose to get a random surprise or skip it."

    @property
    def hint(self) -> str:
        return "Surprise"

    def take(self, hero: Hero) -> bool:
        choice = random.choice(self.POSSIBLE_ENCOUNTERS)
        effect = self.EFFECTS[choice]
        print(f"Your random effect is: {choice}")
        exec(effect)
        return True

    def skip(self, hero: Hero) -> bool:
        print("You refused to take your chance")
        return True


def random_events(number_of_events: int, probabilities: list[float] = [0.8, 0.2]) -> list[Event]:
    probabilities = normalize_probabilities(probabilities)
    return random.choices([Combat_Event(), Non_Combat_Event()], probabilities, k=number_of_events)
