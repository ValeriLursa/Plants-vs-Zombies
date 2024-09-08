import arcade
import Animation
import time
from Sun import Sun
from Pea import Pea

class Plant(Animation.Animation):
    def __init__(self, image, health, cost, lawns):
        super().__init__(image, 0.12)
        self.image = image
        self.health = health
        self.cost = cost
        self.row = 0
        self.column = 0
        self.lawns = lawns

    def update(self):
        if self.health <= 0:
            self.kill()
            self.lawns.remove((self.row, self.column))

    def planting(self, center_x, center_y, row, column):
        self.set_position(center_x, center_y)
        self.row = row
        self.column = column


class SunFlower(Plant):
    def __init__(self, sunlist, lawns):
        super().__init__("textures/plants/SunFlower/SunFlower_0.png", 80, 50, lawns)
        for i in range(1, 18):
            self.append_texture(arcade.load_texture(f"textures/plants/SunFlower/SunFlower_{i}.png"))
        self.sunlist = sunlist
        self.sun_spawn_time = time.time()

        self.scale = 1

    def update(self):
        super().update()
        if time.time() - self.sun_spawn_time >= 15:
            new_sun = Sun(self.center_x - 10, self.bottom)
            self.sun_spawn_time = time.time()
            self.sunlist.append(new_sun)



class PeaShooter(Plant):
    def __init__(self, pealist, zombielist, lawns):
        super().__init__("textures/plants/Peashooter/Peashooter_0.png", 100, 100, lawns)
        for i in range(1, 13):
            self.append_texture(arcade.load_texture(f"textures/plants/Peashooter/Peashooter_{i}.png"))
        self.pea_spawn_time = time.time()
        self.pealist = pealist
        self.zombie_on_line = False
        self.zombielist = zombielist

        self.scale = 1

    def update(self):
        super().update()
        self.zombie_on_line = False
        zombie_attack = 0
        for z in self.zombielist:
            if z.row == self.row:
                self.zombie_on_line = True
                zombie_attack = z
                break
        if time.time() - self.pea_spawn_time >= 2 and self.zombie_on_line:
            new_pea = Pea(self.right, self.top - 10, zombie_attack)
            self.pea_spawn_time = time.time()
            self.pealist.append(new_pea)



class WallNut(Plant):
    def __init__(self, nutlist, lawns):
        super().__init__("textures/plants/WallNut/WallNut/WallNut_0.png", 250, 50, lawns)
        self.full_nut = []
        self.cracked1_nut = []
        self.cracked2_nut = []

        for i in range(16):
            self.full_nut.append(arcade.load_texture(f"textures/plants/WallNut/WallNut/WallNut_{i}.png"))
        for i in range(11):
            self.cracked1_nut.append(arcade.load_texture(f"textures/plants/WallNut/WallNut_cracked1/WallNut_cracked1_{i}.png"))
        for i in range(15):
            self.cracked2_nut.append(arcade.load_texture(f"textures/plants/WallNut/WallNut_cracked2/WallNut_cracked2_{i}.png"))
    
        self.nutlist = nutlist
        self.nut_spawn_time = time.time()
        self.scale = 1
        self.textures = self.full_nut

    def update(self):
        super().update()

        if self.health < 200:
            self.textures = self.cracked1_nut

        if self.health < 100:
            self.textures = self.cracked2_nut


class TorchWood(Plant):
    def __init__(self, woodlist, lawns, pealist):
        super().__init__("plants/tree1.png", 120, 175, lawns)
        for i in range(1, 4):
            self.append_texture(arcade.load_texture(f"plants/tree{i}.png"))
        self.woodlist = woodlist
        self.wood_spawn_time = time.time()
        self.pealist = pealist

    def update(self):
        super().update()
        collist = arcade.check_for_collision_with_list(self, self.pealist)
        for i in collist:
            i.texture = arcade.load_texture("items/firebul.png")
            i.damage = 3