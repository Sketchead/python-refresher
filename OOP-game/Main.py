from Zombie import *
from Ogre import *
import random

def battle(e: Enemy, e2: Enemy):
    e.talk()
    e2.talk()

    while e.health_points > 0 and e2.health_points > 0:
        print('--------------------')
        e.special_attack()
        e2.special_attack()
        e2.attack()
        e.health_points -= e2.attack_damage
        print(f"{e.get_type_of_enemy()} has {e.health_points} health points left.")
        e.attack()
        e2.health_points -= e.attack_damage
        print(f"{e2.get_type_of_enemy()} has {e2.health_points} health points left.")
        print('--------------------')
        
    if e.health_points > 0:
        print(f"{e.get_type_of_enemy()} wins!")
    else: 
        print(f"{e2.get_type_of_enemy()} wins!")

zombie = Zombie(100, 10)
ogre = Ogre(150, 20)

#print(f'{zombie.get_type_of_enemy()} has {zombie.health_points} health points and {zombie.attack_damage} attack damage.')
#print(f'{ogre.get_type_of_enemy()} has {ogre.health_points} health points and {ogre.attack_damage} attack damage.')

battle(zombie, ogre)