import arcade
import time
from Animation import Animation
from Constants import SCREEN_HEIGHT, SCREEN_WIDTH, ZOMBIE_SPEED, FILD_LEFT


class Zombie(Animation):
    def __init__(self, image, health, row, center_y, plantlist, game, kills):
        super().__init__(image, 1)
        
        self.health = health
        self.row = row
        self.set_position(SCREEN_WIDTH + 50, center_y)
        self.change_x = ZOMBIE_SPEED
        self.zombie_spawn_time = time.time()
        self.eating = False
        self.plantlist = plantlist
        self.game = game
        self.kills = kills

    def update(self):
        if not self.eating:
            self.center_x -= self.change_x
        if self.health <= 0 or self.right < 0:
            self.kill()
            self.kills += 1
            print(self.kills)
        self.eating = False
        plants = arcade.check_for_collision_with_list(self, self.plantlist)
        for p in plants:
            if self.row == p.row:
                self.eating = True
                p.health -= 0.5
        if self.right < FILD_LEFT:
            self.game = False