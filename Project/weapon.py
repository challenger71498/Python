import item
import enum


class DamageType(enum.Enum):
    UNKNOWN = 0
    GUN = 1
    EXPLOSIVE = 2
    PIERCING = 3
    LASER = 4


class Weapon(item.Item):
    damage = 0
    damage_type = DamageType(0)

    def __init__(self, n, p, wei, w, h, x, y, d, dam_type):
        super(Weapon, self).__init__(n, p, wei, w, h, x, y)
        self.damage = d
        self.damage_type = dam_type

