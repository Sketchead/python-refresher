from Zombie import *
from Ogre import *
from Hero import *
from Weapon import *
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

def hero_battle(hero: Hero, enemy: Enemy):

    while hero.health_points > 0 and enemy.health_points > 0:
        print('--------------------')
        enemy.special_attack()
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        print(f"Hero has {hero.health_points} health points left.")
        hero.attack()
        enemy.health_points -= hero.attack_damage
        print(f"{enemy.get_type_of_enemy()} has {enemy.health_points} health points left.")
        print('--------------------')
        
    if hero.health_points > 0:
        print(f"Hero wins!")
    else: 
        print(f"{enemy.get_type_of_enemy()} wins!")

zombie = Zombie(100, 10)
ogre = Ogre(150, 20)

atx = Hero(100, 8)
pimiento_axe = Weapon("Pimiento Axe", 30)
atx.equip_weapon(pimiento_axe)
#print(f'{zombie.get_type_of_enemy()} has {zombie.health_points} health points and {zombie.attack_damage} attack damage.')
#print(f'{ogre.get_type_of_enemy()} has {ogre.health_points} health points and {ogre.attack_damage} attack damage.')

hero_battle(atx, ogre)
