import arcade
import random
import time
from Constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SCALE, CELL_WIDTH, CELL_HEIGHT, FILD_LEFT, FILD_BOTTOM, SUN_PRICE, FILD_TOP, SPAWN_ZOMBIE_DELAY, ZOMBIE_COUNT
from Plants import Plant, SunFlower, PeaShooter, WallNut, TorchWood
from Sun import Sun
from Zombies_modules.OrdinaryZombie import OrdinaryZombie
from Zombies_modules.ConeheadZombie import ConeheadZombie



class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture("textures/background.jpg")
        self.menu = arcade.load_texture("textures/menu_vertical.png")
        self.end = arcade.load_texture("textures/end.png")
        self.logo = arcade.load_texture("textures/logo.png")

        self.plants = arcade.SpriteList()
        self.sunslist = arcade.SpriteList()
        self.pealist = arcade.SpriteList()
        self.zombielist = arcade.SpriteList()
        self.zombie_spawn_time = time.time()
        self.nutlist = arcade.SpriteList()
        self.woodlist = arcade.SpriteList()
        self.seed = None
        self.lawns = []
        self.suns = 15000
        self.kills = 0
        self.game = True
        self.win = False
        self.count_zombie_list = 0
        self.time_start_game = time.time()
        self.timer = self.time_start_game
        self.setup()

    def lawn_x(self, x):
        a = (x - FILD_LEFT) // CELL_WIDTH + 1

        if 230 <= x <= 320:
            a = 1
        if 320 <= x <= 400:
            a = 2
        if 400 <= x <= 475:
            a = 3
        if 475 <= x <= 560:
            a = 4
        if 560 <= x <= 630:
            a = 5
        if 630 <= x <= 715:
            a = 6
        if 715 <= x <= 785:
            a = 7
        if 785 <= x <= 865:
            a = 8
        if 865 <= x <= 965:
            a = 9
        center_x = FILD_LEFT + (CELL_WIDTH * a - CELL_WIDTH / 2)
        # print(a)
        return center_x, a


        # right_x = FILD_LEFT + CELL_WIDTH
        # a = 1
        # while right_x <= x:
            # right_x += CELL_WIDTH
            # a += 1
# 
        # center_x = right_x - CELL_WIDTH / 2
        # print(a)
        # return center_x, a

    def lawn_y(self, y):
        a = (y - FILD_BOTTOM) // CELL_HEIGHT + 1
        if a > 5:
            a = 5
        center_y = FILD_BOTTOM + (CELL_HEIGHT * a - CELL_HEIGHT / 2)
        return center_y, a

    def setup(self):
        pass

    def on_draw(self):
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        arcade.draw_texture_rectangle(self.menu.width/2*SCALE, SCREEN_HEIGHT/2, self.menu.width*SCALE, SCREEN_HEIGHT, self.menu)
        if self.suns >= 100:
            arcade.draw_text(text=f"{self.suns}", start_x=34, start_y=490, color=(0, 128, 0), font_size=30)
        elif self.suns < 100 and self.suns > 10:
            arcade.draw_text(text=f"{self.suns}", start_x=44, start_y=490, color=(0, 128, 0), font_size=30)
        else: 
            arcade.draw_text(text=f"{self.suns}", start_x=54, start_y=490, color=(0, 128, 0), font_size=30)
        arcade.draw_text(text=f"Счет: {self.kills}", start_x=250, start_y=550, color=(128, 0, 0), font_size=30)
        self.plants.draw()
        self.sunslist.draw()
        self.pealist.draw()
        self.zombielist.draw()
        self.nutlist.draw()
        self.woodlist.draw()

        if self.seed is not None:
            self.seed.draw()

        if not self.game:
            arcade.draw_texture_rectangle(center_x = SCREEN_WIDTH / 2, center_y = SCREEN_HEIGHT / 2, width = SCREEN_WIDTH, height = SCREEN_HEIGHT, texture = self.end)
        
        if self.win:
            arcade.draw_texture_rectangle(center_x = SCREEN_WIDTH / 2, center_y = SCREEN_HEIGHT / 2, width = SCREEN_WIDTH, height = SCREEN_HEIGHT, texture = self.logo)


    def update(self, delta_time):
        if self.game:
            self.plants.update_animation(delta_time)
            self.plants.update()

            self.sunslist.update()
            self.pealist.update()
            self.nutlist.update()
            self.woodlist.update()

            self.zombielist.update()
            self.zombielist.update_animation(delta_time)

            gametime = time.time()
            # print (time.time() - self.timer)

            if self.kills >= 20 or time.time() - self.timer > 60 * 10 or self.zombielist == 0:
                self.win = True
                self.game = False
                return

            # спавн зомби
            if time.time() - self.zombie_spawn_time > SPAWN_ZOMBIE_DELAY and self.kills < ZOMBIE_COUNT:
                center_y, row = self.lawn_y(random.randint(FILD_BOTTOM, FILD_TOP))
                # zombie_type = random.randint(0, 1)
                zombie_type = 0
                if zombie_type == 0:
                    self.zombielist.append(OrdinaryZombie(row, center_y, self.plants, self.game, self.kills))
                elif zombie_type == 1:
                    self.zombielist.append(ConeheadZombie(row, center_y, self.plants, self.game, self.kills))
                self.zombie_spawn_time = time.time()
                self.count_zombie_list = len(self.zombielist)
                if len(self.zombielist) < self.count_zombie_list:
                    self.kills += 1
                    print(self.kills)

            for i in self.zombielist:
                if i.right < FILD_LEFT:
                    self.game = False

    def on_mouse_press(self, x, y, button, modifiers):
        # print(x, y)
        if self.game:
            if 13 <= x <= 113:
                if 374 <= y <= 480:
                    self.seed = SunFlower(self.sunslist, self.lawns)
    
            if 13 <= x <= 113:
                if 261 <= y <= 367:
                    self.seed = PeaShooter(self.pealist, self.zombielist, self.lawns)
    
            if 13 <= x <= 113:
                if 146 <= y <= 252:
                    self.seed = WallNut(self.nutlist, self.lawns)
    
            if 13 <= x <= 113:
                if 30 <= y <= 136:
                    self.seed = TorchWood(self.woodlist, self.lawns, self.pealist)
    
            
            if self.seed is not None:
                self.seed.center_x = x
                self.seed.center_y = y
                self.seed.alpha = 150
    
            for i in self.sunslist:
                if i.left <= x <= i.right and i.bottom <= y <= i.top:
                    i.kill()
                    self.suns += SUN_PRICE
    
    def on_mouse_motion(self, x, y, dx, dy):
        if self.seed is not None:
            self.seed.center_x = x
            self.seed.center_y = y

    def on_mouse_release(self, x, y, button, modifiers):
        if self.seed is not None:
            if 247 <= x <= 947 and 34 <= y <= 520:
                center_x, column = self.lawn_x(x)
                center_y, row = self.lawn_y(y)
                if (row, column) in self.lawns or self.suns < self.seed.cost:
                    self.seed = None
                    return
                self.lawns.append((row, column))
                self.suns -= self.seed.cost
                self.seed.planting(center_x, center_y, row, column)
                self.seed.alpha = 255
                self.plants.append(self.seed)
                self.seed = None

            else:
                self.seed.kill()


game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()