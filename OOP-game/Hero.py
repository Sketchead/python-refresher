from Weapon import *

class Hero:
    def __init__(self, health_points: int = 100, attack_damage: int = 10):
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.is_weapon_equipped = False
        self.weapon = None

    def equip_weapon(self, weapon: Weapon):
        if self.weapon is None and not self.is_weapon_equipped:
            self.weapon = weapon
            self.is_weapon_equipped = True
            self.attack_damage += weapon.attack_increase
            print(f"Equipped {weapon.weapon_type} with {weapon.attack_increase} attack increase.")

    def attack(self):
        print(f"The Hero attacks with {self.attack_damage} damage.")