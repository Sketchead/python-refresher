class Enemy:
    type_of_enemy: str
    health_points: int
    attack_damage: int

    def talk(self):
        print(f"I am a {self.type_of_enemy}!")

    def walk_forward(self):
        print(f"The {self.type_of_enemy} is walking forward.")

    def attack(self):
        print(f"The {self.type_of_enemy} attacks with {self.attack_damage} damage.")
