import arcade
from Zombie import Zombie


class ConeheadZombie(Zombie):
    def __init__(self, row, center_y, plantlist, game, kills):
        super().__init__("zombies/ConeheadZombie/ConeheadZombie_0.png", 20, row, center_y, plantlist, game, kills)
        for i in range(21):
            self.append_texture(arcade.load_texture(f"zombies/ConeheadZombie/ConeheadZombie_{i}.png"))