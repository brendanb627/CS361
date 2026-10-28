class Player:
    def __init__(self, name):
        self.name = name
        self.stats = Stats()
        self.armor = Armor(ArmorItem("iron helmet", 5), ArmorItem("iron chestplate", 3))
        self.weapon = Weapon("sword", "1d6")

    def damage(self, p):
        self.stats.hp -= p

    def compute_damage(base):
        # Pretend this is some complex thing with AC, armor, hp
        pass

    # And more functions here to handle stats, weapons, and armor

p = Player("Alfredo")


class Armor:
    def __init__(self, armor_items):
        self.armor_items = armor_items

    def compute_ac(self):
        pass
    def add_armor_item(self):
        pass

class ArmorItem:
    def __init__(self, name, armor_class):
        self.name = name
        self.armor_class = armor_class

class Stats:
    def __init__(self):
        self.hp = 10
        self.str = 9
        self.dex = 12
        self.con = 8
        self.int = 18
        self.wis = 10
        self.cha = 2

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def compute_damage(self):
        pass

