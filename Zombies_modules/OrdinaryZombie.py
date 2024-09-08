import arcade
from Zombie import Zombie


class OrdinaryZombie(Zombie):
    # def __init__(self, row, center_y, plantlist, game, kills):
    #     super().__init__("zombies/OrdinaryZombie/Zombie_0.png", 12, row, center_y, plantlist, game, kills)
    #     self.zombie = []
    #     self.attack = []
    #     q = "textures/zombies/OrdinaryZombie/"
    #     for i in range(22):
    #         self.append_texture(arcade.load_texture(f"zombies/OrdinaryZombie/Zombie_{i}.png"))
    #         # self.zombie.append(arcade.load_texture(f"textures/zombies/OrdinaryZombie/Zombie/Zombie_{i}.png"))

    #     for i in range(21):
    #         self.attack.append(arcade.load_texture(f"{q}ZombieAttack/ZombieAttack_{i}.png"))
    #     print("зомби создан")
    #     # self.textures = self.zombie

    # def update(self):
    #     # if arcade.check_for_collision_with_list(self, self.plantlist):
    #         # self.textures = self.attack
    #         pass

    def __init__(self, row, center_y, plantlist, game, kills):
        super().__init__('zombies/OrdinaryZombie/Zombie_0.png', 12, row, center_y, plantlist, game, kills)
        self.zombiestart = []
        self.zombieattack = []
        for i in range(22):
            # self.append_texture(arcade.load_texture(f'zombies/OrdinaryZombie/Zombie_{i}.png'))
            # self.append_texture(arcade.load_texture(f'textures/zombies/OrdinaryZombie/Zombie/Zombie_{i}.png'))
            self.zombiestart.append(arcade.load_texture(f'textures/zombies/OrdinaryZombie/Zombie/Zombie_{i}.png'))
            
        for i in range(21):
            self.zombieattack.append(arcade.load_texture(f'textures/zombies/OrdinaryZombie/ZombieAttack/ZombieAttack_{i}.png'))

        self.textures = self.zombiestart
    
    def update(self):
        super().update()
        print(arcade.check_for_collision_with_list(self, self.plantlist))
        if arcade.check_for_collision_with_list(self, self.plantlist):
            self.textures = self.zombieattack
        else:
            self.textures = self.zombiestart
        