from Enemy import *

enemy = Enemy()
enemy.type_of_enemy = "Zombie"
enemy.health_points = 100
enemy.attack_damage = 10

enemy.talk()
enemy.walk_forward()
enemy.attack()

print(f"Type of Enemy: {enemy.type_of_enemy} ")
print(f"Health Points: {enemy.health_points} ")
print(f"Attack Damage: {enemy.attack_damage} ")
