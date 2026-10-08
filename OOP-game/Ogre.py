from Enemy import *
import random

class Ogre(Enemy):

    def __init__(self, health_points: int = 100, attack_damage: int = 10):
        super().__init__("Ogre", health_points, attack_damage)

    def talk(self):
        print("Ogre is slamming hands all around")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.2
        if did_special_attack_work:
            self.attack_damage += 4
            print("The Ogre increases its attack damage by 4")