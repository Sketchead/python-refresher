class Enemy:
    def __init__(
        self, type_of_enemy: str, health_points: int = 10, attack_damage: int = 10
    ):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def talk(self):
        print(f"I am a {self.__type_of_enemy}!")

    def walk_forward(self):
        print(f"The {self.__type_of_enemy} is walking forward.")

    def attack(self):
        print(f"The {self.__type_of_enemy} attacks with {self.attack_damage} damage.")

    def special_attack(self):
        print(f"The {self.__type_of_enemy} has no special attack")
