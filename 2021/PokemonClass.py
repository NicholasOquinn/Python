class Pokemon:

    """ This Pokemon Class is for representing and manipulating Pokemon Stats

    Attributes: name: Pokemon's name
                hp: Pokemon's health points
                attack: Pokemon's attack points
                defense: Pokemon's defense points
                special_attack: Pokemon's special attack points
                special defense: Pokemon's special defense points
                speed: Pokemon's speed points
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

poliwag = Pokemon("Poliwag", 40, 50, 40, 40, 40, 90)
gloom = Pokemon("Gloom", 60, 65, 70, 85, 75, 40)
hitmonlee = Pokemon("Hitmonlee", 50, 120, 53, 35, 110, 87)

print(poliwag, "\n")
print(gloom, "\n")
print(hitmonlee)


 