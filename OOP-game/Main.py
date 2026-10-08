from Enemy import *

zombie = Enemy("Zombie", 100, 10)
goblin = Enemy("Goblin", 60, 15)

zombie.talk()
zombie.walk_forward()
zombie.attack()

print(f"Type of Enemy: {zombie.get_type_of_enemy()} ")
print(f"Health Points: {zombie.health_points} ")
print(f"Attack Damage: {zombie.attack_damage} ")
