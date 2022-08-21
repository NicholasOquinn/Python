class Pokemon:
    """ This class creates a Pokemon with different stat types.
    attributes: name, hp, attack, defense, special_attack, special_defense, speed.
    """
    def __init__(self, name, hp, attack, defense, special_attack, special_defense, speed):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
    def __str__(self):
        return f"{self.name} \nHP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}, Special Attack: {self.special_attack}, " \
               f"Special Defense: {self.special_defense}, Speed: {self.speed}"

pikachu = Pokemon("Pikachu", 25, 15, 15, 16, 26, 25)
mewtwo = Pokemon("Mewtwo", 32, 14, 16, 22, 28, 22)
squirtle = Pokemon("Squirtle", 22, 16, 15, 21, 17, 22)

