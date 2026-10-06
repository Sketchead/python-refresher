class Enemy:
    def __init__(
        self, type_of_enemy: str, health_points: int = 10, attack_damage: int = 10
    ):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f"I am a {self.type_of_enemy}!")

    def walk_forward(self):
        print(f"The {self.type_of_enemy} is walking forward.")

    def attack(self):
        print(f"The {self.type_of_enemy} attacks with {self.attack_damage} damage.")
