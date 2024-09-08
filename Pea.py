import arcade
from Constants import PEA_SPEED, PEA_DAMAGE, SCREEN_WIDTH


class Pea(arcade.Sprite):
    def __init__(self, center_x, center_y, zombie_attack):
        super().__init__("items/bul.png", 0.12)
        self.change_x = PEA_SPEED
        self.center_x = center_x
        self.center_y = center_y
        self.damage = PEA_DAMAGE  
        self.zombie_attack = zombie_attack  

    def update(self):
        self.center_x += self.change_x
        if self.left >= SCREEN_WIDTH:
            self.kill()
        if arcade.check_for_collision(self, self.zombie_attack):
            self.zombie_attack.health -= self.damage
            self.kill()
            # print(self.zombie_attack.health)