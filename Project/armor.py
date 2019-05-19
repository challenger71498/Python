import item
import enum


class ArmorType(enum.Enum):
    UNKNOWN = 0
    LIGHT = 1
    HEAVY = 2
    SHIELD = 3


class Armor(item.Item):
    armor = 0
    armor_type = ArmorType(0)
    armor_efficiency = 0

    health = 0

    def __init__(self, n, p, wei, w, h, x, y, a, arm_type, heal):
        super(Armor, self).__init__(n, p, wei, w, h, x, y)
        self.armor = a
        self.armor_type = arm_type
        self.health = heal



