from Zombie import *
from Ogre import *

def battle(e: Enemy):
    e.talk()
    e.attack()

zombie = Zombie(100, 10)
ogre = Ogre(150, 20)

#print(f'{zombie.get_type_of_enemy()} has {zombie.health_points} health points and {zombie.attack_damage} attack damage.')
#print(f'{ogre.get_type_of_enemy()} has {ogre.health_points} health points and {ogre.attack_damage} attack damage.')

battle(zombie)
battle(ogre)