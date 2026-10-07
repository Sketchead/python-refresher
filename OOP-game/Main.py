from Enemy import *

enemy = Enemy("Zombie", 100, 10)

enemy.talk()
enemy.walk_forward()
enemy.attack()

print(f"Type of Enemy: {enemy.get_type_of_enemy()} ")
print(f"Health Points: {enemy.health_points} ")
print(f"Attack Damage: {enemy.attack_damage} ")
