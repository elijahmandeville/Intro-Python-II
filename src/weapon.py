class Weapon:
    def __init__(self, name, wepDamage, level):
        self.name = name
        self.wepDamage = wepDamage
        self.level = level

    def __str__(self):
        return f"{self.name}; a level {self.level} weapon dealing {self.wepDamage} damage"
