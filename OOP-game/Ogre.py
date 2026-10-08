
class Ogre(Enemy):

    def __init__(self, health_points: int = 100, attack_damage: int = 10):
        super().__init__("Zombie", health_points, attack_damage)

    def talk(self):
        print("Ogre is slamming hands all around")
