from enum import Enum

class Statistic(Enum):
    STRENGTH = 1
    INTELLIGENCE = 2
    CHARISMA = 3
    SPEED = 4

print(Statistic(2))