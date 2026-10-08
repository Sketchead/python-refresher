from Enemy import *
import random

class Zombie(Enemy):

    def __init__(self, health_points: int = 100, attack_damage: int = 10):
        super().__init__("Zombie", health_points, attack_damage)

    def talk(self):
        print("**Grumbling**")

    def spread_disease(self):
        print("The Zombie is trying to spread the infection")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.5
        if did_special_attack_work:
            self.health_points += 2
            print("The Zombie regeneretates 2 health points")
